import logging
import json
import os
from datetime import datetime

import coreapi
import coreschema
import requests
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema

from .models import Invoice, Schedule, Settings
from .serializers import InvoiceSerializer
from ..user.models import Student, Teacher

logger = logging.getLogger(__name__)


class InvoiceViewSetSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ["post", "put"]:
            extra_fields = [
                coreapi.Field("amount_in_cents", schema=coreschema.Integer()),
                coreapi.Field("payment_method"),
                coreapi.Field("reference"),
                coreapi.Field("referral"),
                coreapi.Field("schedule_id", schema=coreschema.Integer()),
                coreapi.Field("wompi_id"),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class InvoiceViewSet(viewsets.ViewSet):
    serializer_class = InvoiceSerializer
    schema = InvoiceViewSetSchema()

    @staticmethod
    def create(request):
        """
        Creates a new invoice for the payment
        It will be created in a pending status while is validated in Wompi
        """
        data = request.data
        user = Student.objects.get(pk=request.user.pk)
        schedule = Schedule.objects.get(pk=data["schedule_id"])
        referral_tax = Settings.objects.get(is_active=True).referral_tax
        referral = data["referral"] if data["referral"] != user.username else ""
        if referral:
            referral_user = Student.objects.filter(username=referral).first()
            if not referral_user:
                referral_user = Teacher.objects.filter(username=referral).first()
                if not referral_user:
                    return Response(
                        {"error": f"User {referral} does not exists."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
        invoice = Invoice.objects.create(
            buyer=user,
            schedule=schedule,
            amount=data["amount_in_cents"] / 100,
            payment_method=data["payment_method"],
            reference=data["reference"],
            wompi_id=data["wompi_id"],
            referral=referral,
            referral_tax=referral_tax,
        )
        response = InvoiceSerializer(invoice).data
        return Response(response, status=status.HTTP_201_CREATED)

    @staticmethod
    def retrieve(request, pk):
        """
        Returns an invoice. By default, every transaction is stored as pending (p) until it be requested in this
        function, which validate it through Wompi; then checks if referral user exists and assigns him the new income.
        """
        invoice = Invoice.objects.get(pk=pk)
        if request.user.pk != invoice.buyer.pk:
            return Response({"error": "Unauthorized to get invoice"}, 401)
        if invoice.payment_status == "p":  # Pending to validate
            # Validate with Wompi
            wompi_private_key = os.environ.get("WOMPI_PRIVATE_KEY")
            env = (
                "sandbox" if wompi_private_key.startswith("prv_test_") else "production"
            )
            url = f"https://{env}.wompi.co/v1/transactions/{invoice.wompi_id}"
            headers = {"Authorization": f"Bearer {wompi_private_key}"}
            response = requests.get(url, headers=headers).json()["data"]
            invoice.payment_status = response["status"][0].lower()
            if invoice.payment_status == "a" and invoice.referral:  # Status is Accepted
                # Add the earning to the referral
                referral_user = Student.objects.filter(
                    username=invoice.referral
                ).first()
                if not referral_user:
                    referral_user = Teacher.objects.filter(
                        username=invoice.referral
                    ).first()
                earnings = json.loads(referral_user.referral_earnings)
                earnings["pending"].append(
                    {invoice.pk: invoice.amount * invoice.referral_tax / 100}
                )
                referral_user.referral_earnings = json.dumps(earnings)
                referral_user.save()
                # Add the user to the schedule bought
                invoice.schedule.students.add(invoice.buyer)
                invoice.schedule.save()
            invoice.save()
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data, 200)

    @action(methods=["get"], detail=False)
    def get_reference(self, request):
        """
        Returns a unique reference for a new Wompi invoice
        """
        ref = f"{request.user.id}-{len(Invoice.objects.filter(buyer=request.user))}-{datetime.now().microsecond}"
        return Response({"ref": ref}, status=status.HTTP_200_OK)

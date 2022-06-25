from datetime import datetime
import logging

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Bill, Schedule, Settings
from .serializers import BillSerializer
from ..user.models import Student

logger = logging.getLogger(__name__)


class BillViewSet(viewsets.ViewSet):
    serializer_class = BillSerializer

    def create(self, request):
        """
        Creates a new bill for the payment

        Expected data:
        {
            "schedule_id": 1,
            "amount_in_cents": 12500000,
            "payment_method": "Credit card",
            "referral":"jhon_doe_1",
            "transaction_id": "117687-1656130486-39769",
            "reference": "9-2-969224",
        }
        """
        data = request.data
        user = Student.objects.get(pk=request.user.pk)
        schedule = Schedule.objects.get(pk=data["schedule_id"])
        referral_tax = Settings.objects.last().referral_tax
        created = Bill.objects.create(
            buyer=user,
            schedule=schedule,
            amount=data["amount_in_cents"] / 100,
            payment_status="p",
            payment_method=data["payment_method"],
            reference=data["reference"],
            wompi_id=data["transaction_id"],
            referral=data["referral"],
            referral_tax=referral_tax,
        )
        response = BillSerializer(created).data
        return Response(response, status=status.HTTP_201_CREATED)

    def retrieve(self):
        pass

    @action(methods=["get"], detail=False)
    def get_reference(self, request):
        """
        Returns a unique reference for a new Wompi ticket
        """
        ref = f"{request.user.id}-{len(Bill.objects.filter(buyer=request.user))}-{datetime.now().microsecond}"
        return Response({"ref": ref}, status=status.HTTP_200_OK)

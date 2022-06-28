import json
import logging

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherShortSerializer
from ..orchestrator.models import Invoice
from ..orchestrator.serializers import InvoiceSerializer, ScheduleSerializer

logger = logging.getLogger(__name__)


class StudentViewSet(viewsets.ViewSet):
    @action(methods=["get"], detail=False)
    def get_courses_bought(self, request):
        """Returns the list of courses bought by the user"""
        invoices = Invoice.objects.filter(buyer=request.user, payment_status="a")
        schedules = [invoice.schedule for invoice in invoices]
        res = ScheduleSerializer(schedules, many=True).data
        return Response(res, status=status.HTTP_200_OK)

    @action(methods=["get"], detail=False)
    def get_my_earnings(self, request):
        user = Student.objects.filter(username=request.user.username).first()
        if not user:
            user = Teacher.objects.get(username=request - user.username)
        invoices = Invoice.objects.filter(referral=user.username, payment_status="a")
        validation = json.loads(user.referral_earnings)
        validation = validation["paid"] + validation["pending"]
        validation = [list(invoice.keys())[0] for invoice in validation]
        logger.info(validation)
        invoices_validation = Invoice.objects.filter(pk__in=validation)
        assert (invoices == invoices_validation, "err validation")
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["post"], detail=False, permission_classes=[AllowAny])
    def login(self, request):
        """
        Authenticates a user using username and password. Also appends user data to the response.
        Required body - {username: str, password: str}
        """
        data = request.data
        user = authenticate(username=data["username"], password=data["password"])
        if user:
            try:
                res = StudentSerializer(user).data
            except AttributeError:
                res = TeacherShortSerializer(user).data
            token, _ = Token.objects.get_or_create(user=user)
            res["token"] = token.key
            return Response(res, status=status.HTTP_200_OK)
        else:
            res = {"error": "Invalid credentials."}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["post"], detail=False, permission_classes=[AllowAny])
    def register(self, request):
        """
        Register a new student in the students database

        Required body - {first_name: str, last_name: str, username: str, password: str}
        """
        data = request.data
        try:
            student = Student.objects.create(
                first_name=data["first_name"],
                last_name=data["last_name"],
                username=data["username"],
                password=make_password(data["password"]),
            )
            res = StudentSerializer(student).data
            token, _ = Token.objects.get_or_create(user=student)
            res["token"] = token.key
            return Response(res, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

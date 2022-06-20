from datetime import datetime
import logging

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Bill, Schedule
from .serializers import BillSerializer, ScheduleSerializer
from ..course.models import Course
from ..course.serializers import CourseSerializer
from ..user.models import Student
from ..user.serializers import StudentSerializer, TeacherShortSerializer

logger = logging.getLogger(__name__)


class NoAuthViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @action(methods=["get"], detail=False)
    def get_courses(self, request):
        """
        Returns a list of courses. Allow parameters as area, tag and limit.
        If there are not parameters, query will be objects.all()
        Optional query parameters: area, tag & limit - ?area=Area&tag=Tag&limit=10
        """
        data = request.GET
        if data and not all(param in ["area", "tag", "limit"] for param in data):
            return Response(
                {
                    "error": f"Parameters didn't match. Allowed: area, tag or limit. Received:{[k for k in data.keys()]}"
                },
                status.HTTP_400_BAD_REQUEST,
            )
        else:
            courses = Course.objects.all()
        area = data.get("area")
        logger.info(request.GET)
        if area:
            courses = courses.filter(areas__name__icontains=area)
        tag = request.GET.get("tag")
        if tag:
            courses = courses.filter(tags__name__icontains=tag)
        limit = data.get("limit")
        if limit:
            courses = courses[: int(limit)]
        res = CourseSerializer(courses, many=True).data
        return Response(res, status.HTTP_200_OK)

    @action(detail=True, methods=["get"])
    def get_schedules(self, request, pk):
        """
        Returns the scheduled options for the requested course
        Param - pk: int
        """
        course = Course.objects.get(pk=pk)
        schedules = Schedule.objects.filter(
            course=course, start_time__gte=datetime.now()
        )
        data = ScheduleSerializer(schedules, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    @action(methods=["post"], detail=False)
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
            return Response(res, status.HTTP_200_OK)
        else:
            res = {"error": "Invalid credentials."}
            return Response(res, status.HTTP_400_BAD_REQUEST)

    @action(methods=["post"], detail=False)
    def register_student(self, request):
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
            return Response(res, status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)


# class BillViewSet(viewsets.ModelViewSet):
#     model = Bill
#     queryset = model.objects.all()
#     serializer_class = BillSerializer
class BillViewSet(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        """
        Creates a new bill for the payment
        """
        data = request.data
        created = Bill.objects.create(
            buyer=request.user,
            schedule=data["schedule"],
            amount=data["amountInCents"] / 100,
            status="p",
            payment_date=datetime.now(),
            payment_method=data["paymentMethodType"],
            reference=data["reference"],
            wompi_id=data["id"],
        )
        response = BillSerializer(created).data
        headers = self.get_success_headers(response)
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=["get"])
    def get_reference(self, request):
        """
        Returns a unique reference for a new Wompi ticket
        """
        ref = f"{request.user.id}-{len(Bill.objects.filter(buyer=request.user))}-{datetime.now().microsecond}"
        return Response({"ref": ref}, status=status.HTTP_200_OK)


# class ScheduleViewSet(viewsets.ModelViewSet):
#     model = Schedule
#     queryset = model.objects.all()
#     serializer_class = ScheduleSerializer

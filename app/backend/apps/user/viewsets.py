import logging

from django.contrib.auth.hashers import make_password
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer

logger = logging.getLogger(__name__)


class RegisterStudentViewSet(viewsets.ModelViewSet):
    model = Student
    queryset = model.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (AllowAny,)

    @action(methods=["post"], detail=False)
    def student(self, request):
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
            return Response(res, status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status.HTTP_412_PRECONDITION_FAILED)


class StudentViewSet(viewsets.ModelViewSet):
    model = Student
    queryset = model.objects.all()
    serializer_class = StudentSerializer

    @action(methods=["post"], detail=True)
    def get_courses_bought(self, request):
        res = {}
        return Response(res, status.HTTP_200_OK)

    @action(methods=["post"], detail=True)
    def update_profile(self, request):
        """
        Register a new student into the students database

        Body - {first_name: str, last_name: str, gender: str, profile_pic: str, bio: str}
        """
        res = {}
        return Response(res, status.HTTP_200_OK)


class TeacherViewSet(viewsets.ModelViewSet):
    model = Teacher
    queryset = model.objects.all()
    serializer_class = TeacherSerializer

import logging

from django.contrib.auth.hashers import make_password
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Student, Teacher
from .serializers import StudentSerializer  # , TeacherSerializer
from ..course.models import Course

logger = logging.getLogger(__name__)


# class StudentViewSet(viewsets.ModelViewSet):
#     model = Student
#     queryset = model.objects.all()
#     serializer_class = StudentSerializer
class StudentViewSet(viewsets.ViewSet):
    pass
    # @action(methods=["post"], detail=True)
    # def get_courses_bought(self, request):
    #     res = {}
    #     return Response(res, status.HTTP_200_OK)

    # @action(methods=["post"], detail=True)
    # def update_profile(self, request):
    #     """
    #     Register a new student into the students database
    #
    #     Body - {first_name: str, last_name: str, gender: str, profile_pic: str, bio: str}
    #     """
    #     res = {}
    #     return Response(res, status.HTTP_200_OK)


# class TeacherViewSet(viewsets.ModelViewSet):
#     model = Teacher
#     queryset = model.objects.all()
#     serializer_class = TeacherSerializer

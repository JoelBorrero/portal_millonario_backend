from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    model = Student
    queryset = model.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    model = Teacher
    queryset = model.objects.all()
    serializer_class = TeacherSerializer

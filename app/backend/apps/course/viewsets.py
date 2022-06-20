from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Course
from .serializers import CourseSerializer


# class CourseViewSet(viewsets.ModelViewSet):
#     model = Course
#     queryset = model.objects.all()
#     serializer_class = CourseSerializer

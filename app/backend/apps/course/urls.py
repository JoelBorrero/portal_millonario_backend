from django.urls import path, include
from rest_framework import routers

from .viewsets import CourseViewSet

router = routers.DefaultRouter()
router.register("", CourseViewSet, basename="course")
urlpatterns = [path("", include(router.urls))]

from django.urls import path, include
from rest_framework import routers
from .viewsets import CourseViewSet

router = routers.DefaultRouter()
router.register("", CourseViewSet)
urlpatterns = [path("", include(router.urls))]

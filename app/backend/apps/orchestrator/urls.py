from django.urls import path, include
from rest_framework import routers
from .viewsets import ScheduleViewSet

router = routers.DefaultRouter()
router.register("schedule", ScheduleViewSet)
urlpatterns = [path("", include(router.urls))]

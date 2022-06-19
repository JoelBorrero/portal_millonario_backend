from django.urls import path, include
from rest_framework import routers
from .viewsets import BillViewSet, ScheduleViewSet

router = routers.DefaultRouter()
router.register("bill", BillViewSet)
router.register("schedule", ScheduleViewSet)
urlpatterns = [path("", include(router.urls))]

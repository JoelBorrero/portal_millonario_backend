from django.urls import path, include
from rest_framework import routers
from .viewsets import BillViewSet

router = routers.DefaultRouter()
router.register("bill", BillViewSet, basename="bill")
# router.register("schedule", ScheduleViewSet, basename="schedule")
urlpatterns = [path("", include(router.urls))]

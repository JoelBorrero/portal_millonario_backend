from django.urls import path, include
from rest_framework import routers
from .viewsets import NoAuthViewSet, BillViewSet

router = routers.DefaultRouter()
router.register("open", NoAuthViewSet, basename="open")
router.register("bill", BillViewSet, basename="bill")
# router.register("schedule", ScheduleViewSet, basename="schedule")
urlpatterns = [path("", include(router.urls))]

from django.urls import path, include
from rest_framework import routers
from .viewsets import InvoiceViewSet

router = routers.DefaultRouter()
router.register("invoice", InvoiceViewSet, basename="invoice")
# router.register("schedule", ScheduleViewSet, basename="schedule")
urlpatterns = [path("", include(router.urls))]

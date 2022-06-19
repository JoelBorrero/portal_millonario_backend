from datetime import datetime

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Bill, Schedule
from .serializers import BillSerializer, ScheduleSerializer
from ..course.models import Course


class BillViewSet(viewsets.ModelViewSet):
    model = Bill
    queryset = model.objects.all()
    serializer_class = BillSerializer

    def create(self, request, *args, **kwargs):
        """
        Creates a new bill for the payment
        """
        data = request.data
        created = Bill.objects.create(
            buyer=request.user,
            schedule=data["schedule"],
            amount=data["amountInCents"] / 100,
            status="p",
            payment_date=datetime.now(),
            payment_method=data["paymentMethodType"],
            reference=data["reference"],
            wompi_id=data["id"],
        )
        response = BillSerializer(created).data
        headers = self.get_success_headers(response)
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=["get"])
    def get_reference(self, request):
        """
        Returns a unique reference for a new Wompi ticket
        """
        ref = f"{request.user.id}-{len(Bill.objects.filter(buyer=request.user))}-{datetime.now().microsecond}"
        return Response({"ref": ref}, status=status.HTTP_200_OK)


class ScheduleViewSet(viewsets.ModelViewSet):
    model = Schedule
    queryset = model.objects.all()
    serializer_class = ScheduleSerializer

    @action(detail=False, methods=["get"])
    def get_schedules_for_course(self, request):
        """
        Returns the scheduled options for the requested course
        Body - {course_id: int}
        """
        course = Course.objects.get(pk=request.data["course_id"])
        ref = f"{request.user.id}-{len(Bill.objects.filter(buyer=request.user))}-{datetime.now().microsecond}"
        return Response({"ref": ref}, status=status.HTTP_200_OK)

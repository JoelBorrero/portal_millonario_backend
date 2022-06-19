from .models import Bill, Schedule
from ..utils.serializers import CustomSerializer


class BillSerializer(CustomSerializer):
    class Meta:
        model = Bill
        exclude = []


class ScheduleSerializer(CustomSerializer):
    class Meta:
        model = Schedule
        exclude = []

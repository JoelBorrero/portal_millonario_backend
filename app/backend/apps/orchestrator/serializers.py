from .models import Schedule
from ..utils.serializers import CustomSerializer


class ScheduleSerializer(CustomSerializer):
    class Meta:
        model = Schedule
        exclude = []

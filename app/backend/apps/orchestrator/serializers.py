from ast import literal_eval

from rest_framework import serializers

from .models import Bill, Schedule
from ..course.serializers import VideoClassShortSerializer
from ..user.serializers import TeacherShortSerializer
from ..utils.serializers import CustomSerializer


class BillSerializer(CustomSerializer):
    class Meta:
        model = Bill
        exclude = ("archived", "created", "updated")


class ScheduleSerializer(CustomSerializer):
    teacher = TeacherShortSerializer()
    classes = VideoClassShortSerializer(many=True)
    calendar = serializers.SerializerMethodField()

    @staticmethod
    def get_calendar(obj):
        return literal_eval(obj.calendar)

    class Meta:
        model = Schedule
        exclude = ("archived", "created", "updated")

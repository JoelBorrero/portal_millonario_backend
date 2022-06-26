from ast import literal_eval

from rest_framework import serializers

from .models import Invoice, Schedule
from ..course.serializers import VideoClassShortSerializer
from ..user.serializers import TeacherShortSerializer
from ..utils.constants import PAYMENT_STATUSES
from ..utils.serializers import CustomSerializer


class InvoiceSerializer(CustomSerializer):
    payment_status = serializers.SerializerMethodField()

    @staticmethod
    def get_payment_status(obj):
        return [s[1] for s in PAYMENT_STATUSES if s[0] == obj.payment_status][0]

    class Meta:
        model = Invoice
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

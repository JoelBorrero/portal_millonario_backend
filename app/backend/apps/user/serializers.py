import json

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Student, Teacher
from ..utils.serializers import CustomSerializer


class StudentSerializer(CustomSerializer):
    progress = serializers.SerializerMethodField()
    referral_earnings = serializers.SerializerMethodField()

    @staticmethod
    def get_progress(student):
        return json.loads(student.progress)

    @staticmethod
    def get_referral_earnings(student):
        return json.loads(student.referral_earnings)

    class Meta:
        model = Student
        exclude = (
            "password",
            "last_login",
            "is_superuser",
            "email",
            "is_staff",
            "is_active",
            "date_joined",
            "groups",
            "user_permissions",
        )


class TeacherShortSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("id", "first_name", "last_name", "profile_pic", "rating")


# class TeacherSerializer(CustomSerializer):
#     referral_earnings = serializers.SerializerMethodField()
#
#     @staticmethod
#     def get_referral_earnings(student):
#         return json.loads(student.referral_earnings)
#
#     class Meta:
#         model = Teacher
#         exclude = []

from ast import literal_eval

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Student, Teacher
from ..utils.serializers import CustomSerializer


class StudentSerializer(CustomSerializer):
    progress = serializers.SerializerMethodField()

    @staticmethod
    def get_progress(obj):
        return literal_eval(obj.progress)

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
#     class Meta:
#         model = Teacher
#         exclude = []

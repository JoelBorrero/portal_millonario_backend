import ast

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Course, VideoClass
from ..utils.serializers import CustomSerializer


class CourseSerializer(CustomSerializer):
    tags = serializers.StringRelatedField(many=True)
    areas = serializers.StringRelatedField(many=True)
    content = serializers.SerializerMethodField()

    @staticmethod
    def get_content(obj):
        return ast.literal_eval(obj.content)

    class Meta:
        model = Course
        exclude = ("archived", "created", "updated")


class VideoClassShortSerializer(ModelSerializer):
    class Meta:
        model = VideoClass
        fields = ("id", "name", "duration_in_minutes")


class VideoClassSerializer(CustomSerializer):
    class Meta:
        model = VideoClass
        exclude = ("archived", "created", "updated")

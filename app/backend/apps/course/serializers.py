from .models import Course
from ..utils.serializers import CustomSerializer


class CourseSerializer(CustomSerializer):
    class Meta:
        model = Course
        exclude = []

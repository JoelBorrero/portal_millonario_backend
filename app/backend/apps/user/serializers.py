from .models import Student, Teacher
from ..utils.serializers import CustomSerializer


class StudentSerializer(CustomSerializer):
    class Meta:
        model = Student
        exclude = ("password",)


class TeacherSerializer(CustomSerializer):
    class Meta:
        model = Teacher
        exclude = []

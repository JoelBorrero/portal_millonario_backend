import logging

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..orchestrator.models import Bill
from ..orchestrator.serializers import ScheduleSerializer

logger = logging.getLogger(__name__)


# class StudentViewSet(viewsets.ModelViewSet):
#     model = Student
#     queryset = model.objects.all()
#     serializer_class = StudentSerializer
class StudentViewSet(viewsets.ViewSet):
    @action(methods=["get"], detail=False)
    def get_courses_bought(self, request):
        """Returns the list of courses bought by the user"""
        bills = Bill.objects.filter(buyer=request.user)
        logger.info(request.user)
        schedules = [bill.schedule for bill in bills]
        res = ScheduleSerializer(schedules, many=True).data
        return Response(res, status.HTTP_200_OK)

    # @action(methods=["post"], detail=True)
    # def update_profile(self, request):
    #     """
    #     Register a new student into the students database
    #
    #     Body - {first_name: str, last_name: str, gender: str, profile_pic: str, bio: str}
    #     """
    #     res = {}
    #     return Response(res, status.HTTP_200_OK)


# class TeacherViewSet(viewsets.ModelViewSet):
#     model = Teacher
#     queryset = model.objects.all()
#     serializer_class = TeacherSerializer

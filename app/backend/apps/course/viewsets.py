from datetime import datetime

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Course
from .serializers import CourseSerializer
from ..orchestrator.models import Schedule
from ..orchestrator.serializers import ScheduleSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CourseSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Course.objects.all()
        area = self.request.query_params.get("area")
        tag = self.request.query_params.get("tag")
        limit = self.request.query_params.get("limit")
        if area:
            queryset = queryset.filter(areas__name__icontains=area)
        if tag:
            queryset = queryset.filter(tags__name__icontains=tag)
        if limit:
            queryset = queryset[: int(limit)]
        return queryset

    @action(methods=["get"], detail=True)
    def get_schedules(self, request, pk):
        """
        Returns the scheduled options for the requested course
        Param - pk: int
        """
        course = Course.objects.get(pk=pk)
        schedules = Schedule.objects.filter(
            course=course, start_time__gte=datetime.now()
        )
        data = ScheduleSerializer(schedules, many=True).data
        return Response(data, status=status.HTTP_200_OK)

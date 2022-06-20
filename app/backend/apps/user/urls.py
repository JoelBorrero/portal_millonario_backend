from django.urls import path, include
from rest_framework import routers
from .viewsets import StudentViewSet  # , TeacherViewSet

router = routers.DefaultRouter()
router.register("student", StudentViewSet, basename="student")
# router.register("teacher", TeacherViewSet)
urlpatterns = [path("", include(router.urls))]

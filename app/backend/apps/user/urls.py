from django.urls import path, include
from rest_framework import routers
from .viewsets import RegisterStudentViewSet, StudentViewSet, TeacherViewSet

router = routers.DefaultRouter()
router.register("register", RegisterStudentViewSet)
router.register("student", StudentViewSet)
router.register("teacher", TeacherViewSet)
urlpatterns = [path("", include(router.urls))]

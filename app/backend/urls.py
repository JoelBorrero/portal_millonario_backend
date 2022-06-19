from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view


router = DefaultRouter()
schema_view = get_swagger_view(title="Portal Millonario")
PREFIX_URL = settings.PREFIX_URL
urlpatterns = [
    url(r"^{}admin/".format(PREFIX_URL), admin.site.urls),
    url(r"^{}auth/".format(PREFIX_URL), include("rest_auth.urls")),
    url(r"^{}$".format(PREFIX_URL), schema_view),
    url(r"^{}api/".format(PREFIX_URL), include(router.urls)),
    url(r"^{}api/v1/course/".format(PREFIX_URL), include("backend.apps.course.urls")),
    url(
        r"^{}api/v1/orchestrator/".format(PREFIX_URL),
        include("backend.apps.orchestrator.urls"),
    ),
    url(r"^{}api/v1/user/".format(PREFIX_URL), include("backend.apps.user.urls")),
]

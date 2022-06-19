from django.contrib import admin

from .models import Area, Course, Tag, VideoClass


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price")
    search_fields = ("name", "description")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")


@admin.register(VideoClass)
class VideoClassAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "synchronous", "start_time", "duration_in_minutes")
    list_filter = ("synchronous", "duration_in_minutes")
    search_fields = ("url",)

from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "gender")
    list_filter = ("gender",)
    search_fields = ("first_name", "last_name", "username", "bio")


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "gender", "rating")
    list_filter = ("gender", "rating")
    search_fields = ("first_name", "last_name", "username", "bio")

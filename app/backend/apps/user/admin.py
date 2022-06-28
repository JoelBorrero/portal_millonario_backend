from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "gender")
    list_filter = ("gender",)
    readonly_fields = (
        "progress",
        "referral_earnings",
    )
    search_fields = ("first_name", "last_name", "username", "bio")


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "gender", "rating")
    list_filter = ("gender", "rating")
    readonly_fields = ("referral_earnings",)
    search_fields = ("first_name", "last_name", "username", "bio")

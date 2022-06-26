from django.contrib import admin

from .models import Invoice, CourseFeedback, Schedule, TeacherFeedback, Settings


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "reference",
        "schedule",
        "amount",
        "payment_status",
        "payment_date",
    )
    list_filter = ("payment_status", "buyer")


@admin.register(CourseFeedback)
class CourseFeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "teacher", "rate", "comment", "private")
    list_filter = ("rate", "private")


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("id", "course", "teacher", "calendar")
    list_filter = ("course", "teacher")


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "referral_tax", "is_active")


@admin.register(TeacherFeedback)
class TeacherFeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "teacher", "rate", "comment")
    list_filter = ("rate", "course")

from django.contrib.auth.models import User
from django.db import models

from ..utils.constants import GENDERS


class BaseUser(User):
    bio = models.CharField("Biografía", max_length=500, blank=True, null=True)
    profile_pic = models.CharField(
        "Foto de perfil", max_length=200, blank=True, null=True
    )
    gender = models.CharField(
        "Género", choices=GENDERS, max_length=1, blank=True, null=True
    )
    phone_number = models.CharField("Teléfono", max_length=20, blank=True, null=True)
    referral_earnings = models.TextField(
        "Ganancias de referidos", default='{"paid":[], "pending": []}', editable=False
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        abstract = True


class Student(BaseUser):
    progress = models.TextField("Progreso", default="{}", editable=False)

    class Meta:
        verbose_name = "estudiante"
        verbose_name_plural = "estudiantes"


class Teacher(BaseUser):
    rating = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = "profesor"
        verbose_name_plural = "profesores"

from django.contrib.auth.models import User
from django.db import models

from ..utils.constants import GENDERS


class BaseUser(User):
    bio = models.CharField("Biografía", max_length=500, blank=True, null=True)
    profile_pic = models.CharField(
        "Foto de perfil", max_length=200, blank=True, null=True
    )
    gender = models.CharField("Género", choices=GENDERS, max_length=1)
    phone_number = models.CharField("Teléfono", max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        abstract = True


class Student(BaseUser):
    progress = models.TextField("Progreso", default="{}")

    class Meta:
        verbose_name = "estudiante"
        verbose_name_plural = "estudiantes"


class Teacher(BaseUser):
    rating = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = "profesor"
        verbose_name_plural = "profesores"

from django.db import models

from ..user.models import Teacher
from ..utils.models import ModelBase


class Area(ModelBase):
    name = models.CharField("Nombre", max_length=50)
    description = models.TextField("Descripción", default="")

    def __str__(self):
        return self.name


class Tag(ModelBase):
    name = models.CharField("Nombre", max_length=50)
    description = models.TextField("Descripción", default="")

    def __str__(self):
        return self.name


class Course(ModelBase):
    name = models.CharField("Nombre", max_length=100)
    description = models.TextField("Descripción", default="")
    intro_url = models.CharField("Intro url", max_length=200)
    price = models.PositiveIntegerField("Precio")
    teachers = models.ManyToManyField(Teacher, blank=True, verbose_name="Profesores")
    areas = models.ManyToManyField(Area, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "curso"
        verbose_name_plural = "cursos"


class VideoClass(ModelBase):
    url = models.CharField(max_length=200)
    synchronous = models.BooleanField("Asíncrona")
    start_time = models.DateTimeField("Fecha de inicio")
    duration_in_minutes = models.PositiveSmallIntegerField("Duración")

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = "video"
        verbose_name_plural = "videos"

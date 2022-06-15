from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from ..course.models import Course, VideoClass
from ..user.models import Student, Teacher
from ..utils.constants import PAYMENT_STATUSES
from ..utils.models import ModelBase


class Schedule(ModelBase):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Curso")
    students = models.ManyToManyField(Student, verbose_name="Estudiantes")
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True, verbose_name="Profesor"
    )
    classes = models.ManyToManyField(VideoClass, verbose_name="Clases")
    calendar = models.TextField("Calendario", default="{}")

    def __str__(self):
        return f"Cronograma {self.pk} - {self.course}"

    class Meta:
        verbose_name = "cronograma"
        verbose_name_plural = "cronogramas"


class Bill(ModelBase):
    buyer = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name="Comprador"
    )
    schedule = models.ForeignKey(
        Schedule, on_delete=models.CASCADE, verbose_name="Cronograma"
    )
    value = models.PositiveIntegerField("Valor")
    status = models.CharField("Estado", choices=PAYMENT_STATUSES, max_length=1)
    payment_date = models.DateTimeField("Fecha de pago", blank=True, null=True)

    def __str__(self):
        return f"Factura #{self.id}"

    class Meta:
        verbose_name = "factura"
        verbose_name_plural = "facturas"


class Feedback(ModelBase):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name="Estudiante"
    )
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, verbose_name="Profesor"
    )
    rate = models.PositiveSmallIntegerField("Calificación")
    comment = models.CharField("Comentario", max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Feedback #{self.id}"

    class Meta:
        abstract = True


class CourseFeedback(Feedback):
    private = models.BooleanField("Privado")

    class Meta:
        verbose_name = "feedback de curso"
        verbose_name_plural = "feedbacks de cursos"


class Settings(ModelBase):
    name = models.CharField("Nombre", max_length=20, default="default")
    referral_tax = models.PositiveSmallIntegerField(
        "Tasa de referido (%)", validators=[MaxValueValidator(100)]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ajuste"
        verbose_name_plural = "ajustes"


class TeacherFeedback(Feedback):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Curso")

    class Meta:
        verbose_name = "feedback de profesor"
        verbose_name_plural = "feedbacks de profesores"
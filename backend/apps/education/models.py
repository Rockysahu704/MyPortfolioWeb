from django.conf import settings
from django.db import models


class Education(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="educations"
    )

    institution = models.CharField(
        max_length=200
    )

    degree = models.CharField(
        max_length=200
    )

    field = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.degree} - {self.institution}"
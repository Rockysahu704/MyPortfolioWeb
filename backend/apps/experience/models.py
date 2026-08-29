from django.conf import settings
from django.db import models


class Experience(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="experiences"
    )

    company = models.CharField(
        max_length=200
    )

    position = models.CharField(
        max_length=200
    )

    description = models.TextField()

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True
    )

    is_current = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.position} at {self.company}"
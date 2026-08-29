from django.conf import settings
from django.db import models


class Skill(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="skills"
    )

    name = models.CharField(
        max_length=100
    )

    category = models.CharField(
        max_length=100
    )

    proficiency = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "name"],
                name="unique_user_skill"
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.name}"
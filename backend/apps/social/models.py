from django.conf import settings
from django.db import models


class SocialMedia(models.Model):

    PLATFORM_CHOICES = [
        ("linkedin", "LinkedIn"),
        ("github", "GitHub"),
        ("instagram", "Instagram"),
        ("facebook", "Facebook"),
        ("youtube", "YouTube"),
        ("email", "Email"),
        ("phone", "Phone"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="social_media"
    )

    platform = models.CharField(
        max_length=20,
        choices=PLATFORM_CHOICES
    )

    link = models.CharField(
        max_length=500
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "platform"],
                name="unique_user_platform"
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.platform}"
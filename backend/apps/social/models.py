from django.db import models


class SocialMedia(models.Model):

    PLATFORM_CHOICES = [
        ("linkedin", "LinkedIn"),
        ("github", "GitHub"),
        ("instagram", "Instagram"),
        ("facebook", "Facebook"),
        ("youtube", "YouTube"),
    ]

    platform = models.CharField(
        max_length=20,
        choices=PLATFORM_CHOICES,
        unique=True
    )

    url = models.URLField()

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.platform

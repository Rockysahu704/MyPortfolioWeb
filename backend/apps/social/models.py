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

    platform = models.CharField(
        max_length=20,
        choices=PLATFORM_CHOICES,
        unique=True
    )

    url = models.URLField(
         max_length=500
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.platform

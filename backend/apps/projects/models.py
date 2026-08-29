from django.conf import settings
from django.db import models


class Project(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    github_url = models.URLField(
        blank=True
    )

    live_url = models.URLField(
        blank=True
    )

    image = models.ImageField(
        upload_to="projects/",
        blank=True
    )

    skills = models.ManyToManyField(
        "skills.Skill",
        related_name="projects",
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title
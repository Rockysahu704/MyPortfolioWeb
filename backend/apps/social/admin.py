from django.contrib import admin
from .models import SocialMedia


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):

    list_display = (
        "platform",
        "url",
        "is_active",
    )

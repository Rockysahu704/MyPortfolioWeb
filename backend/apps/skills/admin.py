from django.contrib import admin
from .models import Skill

# Register your models here.


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "category",
        "proficiency",
    ]

    search_fields = [
        "name",
        "category",
    ]

    list_filter = [
        "category",
    ]
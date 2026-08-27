from django.contrib import admin
from .models import Experience

# Register your models here.

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = [
        "company",
        "position",
        "start_date",
        "end_date",
        "is_current",
    ]

    search_fields = [
        "company",
        "position",
    ]

    list_filter = [
        "is_current",
    ]

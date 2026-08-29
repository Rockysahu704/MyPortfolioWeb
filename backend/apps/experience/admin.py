from django.contrib import admin
from .models import Experience


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

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        # Superuser can see all experiences
        if request.user.is_superuser:
            return queryset

        # Normal user can see only their own experiences
        return queryset.filter(user=request.user)

    def save_model(self, request, obj, form, change):

        # Automatically assign logged-in user
        if not change:
            obj.user = request.user

        super().save_model(
            request,
            obj,
            form,
            change
        )
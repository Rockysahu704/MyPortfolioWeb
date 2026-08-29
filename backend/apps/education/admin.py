from django.contrib import admin
from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):

    list_display = [
        "institution",
        "degree",
        "field",
        "start_date",
        "end_date",
    ]

    search_fields = [
        "institution",
        "degree",
        "field",
    ]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        # Superuser can see all education records
        if request.user.is_superuser:
            return queryset

        # Normal user can see only their own education
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
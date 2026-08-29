from django.contrib import admin
from .models import SocialMedia


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):

    list_display = (
        "platform",
        "link",
        "is_active",
    )

    search_fields = (
        "platform",
        "link",
    )

    list_filter = (
        "platform",
        "is_active",
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.is_superuser:
            return queryset

        return queryset.filter(user=request.user)

    def save_model(self, request, obj, form, change):

        if not change:
            obj.user = request.user

        super().save_model(
            request,
            obj,
            form,
            change
        )
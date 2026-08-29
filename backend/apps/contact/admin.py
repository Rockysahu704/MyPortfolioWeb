from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "email",
        "subject",
        "is_read",
        "created_at",
    ]

    search_fields = [
        "name",
        "email",
        "subject",
        "message",
    ]

    list_filter = [
        "is_read",
        "created_at",
    ]

    readonly_fields = [
        "created_at",
    ]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        # Superuser can see all messages
        if request.user.is_superuser:
            return queryset

        # Normal user can see only messages
        # sent to their portfolio
        return queryset.filter(user=request.user)
from django.contrib import admin
from .models import Skill


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

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        # Superuser can see all skills
        if request.user.is_superuser:
            return queryset

        # Normal user can see only their own skills
        return queryset.filter(user=request.user)


    def save_model(self, request, obj, form, change):

        # Automatically assign the logged-in user
        if not change:
            obj.user = request.user

        super().save_model(
            request,
            obj,
            form,
            change
        )
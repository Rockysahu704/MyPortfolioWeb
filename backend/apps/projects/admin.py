from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = [
        "title",
        "created_at",
        "updated_at",
    ]

    search_fields = [
        "title",
        "description",
    ]

    list_filter = [
        "created_at",
    ]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        # Superuser can see all projects
        if request.user.is_superuser:
            return queryset

        # Normal user can see only their own projects
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


    def formfield_for_manytomany(self, db_field, request, **kwargs):

        # Show only the logged-in user's skills
        if db_field.name == "skills":

            if request.user.is_superuser:
                # Superuser can see all skills
                return super().formfield_for_manytomany(
                    db_field,
                    request,
                    **kwargs
                )

            kwargs["queryset"] = db_field.related_model.objects.filter(
                user=request.user
            )

        return super().formfield_for_manytomany(
            db_field,
            request,
            **kwargs
        )
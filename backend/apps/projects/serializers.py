from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "github_url",
            "live_url",
            "image",
            "skills",
            "created_at",
            "updated_at",
        ]
    def validate_title(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Project title cannot be empty."
            )
        return value
        
    def validate_description(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Project description cannot be empty."
            )
        return value
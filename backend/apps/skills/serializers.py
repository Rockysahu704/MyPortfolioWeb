from rest_framework import serializers
from .models import Skill

class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = [
            "id",
            "name",
            "category",
            "proficiency",
            "image"
        ]

    def validate_name(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Skill name cannot be empty."
            )
        return value

    def validate_proficiency(self, value):

        if value < 0 or value > 100:
            raise serializers.ValidationError(
                "Proficiency must be between 0 and 100."
            )
        return value
    


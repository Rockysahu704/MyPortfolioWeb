from rest_framework import serializers

from .models import Education


class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = [
            "id",
            "institution",
            "degree",
            "field",
            "description",
            "start_date",
            "end_date",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def validate_institution(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Institution name cannot be empty."
            )
        return value

    def validate_degree(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Degree cannot be empty."
            )
        return value
    
    def validate_field(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Field of study cannot be empty."
            )
        return value

    def validate(self, attrs):
        start_date = attrs.get("start_date")
        end_date = attrs.get("end_date")

        if end_date and start_date and end_date < start_date:
            raise serializers.ValidationError(
                "End date cannot be before start date."
            )
        return attrs
    
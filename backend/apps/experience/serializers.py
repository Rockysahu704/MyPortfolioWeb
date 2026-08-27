from rest_framework import serializers

from .models import Experience


class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experience
        fields = [
            "id",
            "company",
            "position",
            "description",
            "start_date",
            "end_date",
            "is_current",
            "created_at",
            "updated_at",
        ]

    def validate_company(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Company name cannot be empty."
            )
        return value

    def validate_position(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Position cannot be empty."
            )
        return value

    def validate_description(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Description cannot be empty."
            )
        return value

    def validate(self, attrs):

        start_date = attrs.get("start_date")
        end_date = attrs.get("end_date")
        is_current = attrs.get("is__current")


        if end_date and start_date and end_date < start_date:
            raise serializers.ValidationError(
                "End date cannot be before start date."
            )

        if is_current and end_date:
            raise serializers.ValidationError(
                "Cannot experience should not have an end date."
            )

        if not is_current and not end_date:
            raise serializers.ValidationError(
                "End date is reuired for previous experience."
            )
        return attrs
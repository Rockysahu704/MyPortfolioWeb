from rest_framework import viewsets

from common.permissions import IsAdminOrReadOnly

from .models import Experience
from .serializers import ExperienceSerializer


class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = ExperienceSerializer

    permission_classes = [IsAdminOrReadOnly]

    filterset_fields = [
        "is_current",
    ]

    def get_queryset(self):

        username = self.kwargs["username"]

        return Experience.objects.filter(
            user__username=username
        ).order_by(
            "-start_date"
        )
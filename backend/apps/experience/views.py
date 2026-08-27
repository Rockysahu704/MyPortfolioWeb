from rest_framework import viewsets
from common.permissions import IsAdminOrReadOnly

from .models import Experience
from .serializers import ExperienceSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all().order_by("-start_date")
    serializer_class = ExperienceSerializer
    permission_classes = [IsAdminOrReadOnly]

    filterset_fields = [
        "is_current",
    ]

from rest_framework import viewsets

from common.permissions import IsAdminOrReadOnly

from .models import Education
from .serializers import EducationSerializer


class EducationViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = EducationSerializer

    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):

        username = self.kwargs["username"]

        return Education.objects.filter(
            user__username=username
        ).order_by(
            "-start_date"
        )
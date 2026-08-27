from rest_framework import viewsets
from common.permissions import IsAdminOrReadOnly

from .models import Education
from .serializers import EducationSerializer


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all().order_by("-start_date")
    serializer_class = EducationSerializer
    permission_classes = [IsAdminOrReadOnly]

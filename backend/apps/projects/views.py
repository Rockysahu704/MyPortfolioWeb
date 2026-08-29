from rest_framework import viewsets

from common.permissions import IsAdminOrReadOnly
from common.pagination import PortfolioPagination

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = ProjectSerializer

    permission_classes = [IsAdminOrReadOnly]

    pagination_class = PortfolioPagination

    def get_queryset(self):

        username = self.kwargs["username"]

        return Project.objects.filter(
            user__username=username
        ).order_by(
            "-created_at"
        )
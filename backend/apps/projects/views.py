from django.shortcuts import render

from rest_framework import viewsets
from common.permissions import IsAdminOrReadOnly
from common.pagination import PortfolioPagination

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by("-created_at")
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = PortfolioPagination
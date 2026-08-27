from django.shortcuts import render
from rest_framework import viewsets
from common.permissions import IsAdminOrReadOnly
from .models import Skill
from .serializers import SkillSerializer

# Create your views here.


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all().order_by("-proficiency", "name")
    serializer_class = SkillSerializer
    permission_classes = [IsAdminOrReadOnly]

    filterset_fields = [
        "category",
    ]
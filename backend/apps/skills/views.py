
from rest_framework import viewsets
from common.permissions import IsAdminOrReadOnly
from .models import Skill
from .serializers import SkillSerializer

# Create your views here.


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SkillSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = [
        "category",
    ]

    def get_queryset(self):
        username = self.kwargs["username"]
        return Skill.objects.filter(
            user__username=username
        ).order_by(
            "-proficiency",
            "name",

        )
        
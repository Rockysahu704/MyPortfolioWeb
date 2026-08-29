from rest_framework import viewsets

from .models import SocialMedia
from .serializers import SocialMediaSerializer


class SocialMediaViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = SocialMediaSerializer
    # queryset = SocialMedia.objects.all()
    def get_queryset(self):
        username = self.kwargs["username"]

        return SocialMedia.objects.filter(
            user__username=username,
            is_active=True
        )

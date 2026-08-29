from rest_framework import viewsets

from .models import SocialMedia
from .serializers import SocialMediaSerializer


class SocialMediaViewSet(viewsets.ModelViewSet):

    queryset = SocialMedia.objects.all()

    serializer_class = SocialMediaSerializer
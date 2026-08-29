from django.contrib.auth import get_user_model

from rest_framework import viewsets

from .models import ContactMessage
from .serializers import ContactMessageSerializer
from .permissions import IsAdminOrCreateOnly


class ContactMessageViewSet(viewsets.ModelViewSet):

    serializer_class = ContactMessageSerializer

    permission_classes = [IsAdminOrCreateOnly]

    def get_queryset(self):

        username = self.kwargs["username"]

        return ContactMessage.objects.filter(
            user__username=username
        ).order_by(
            "is_read",
            "-created_at"
        )

    def perform_create(self, serializer):

        username = self.kwargs["username"]

        User = get_user_model()

        user = User.objects.get(
            username=username
        )

        serializer.save(
            user=user
        )
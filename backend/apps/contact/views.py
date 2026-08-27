from rest_framework import viewsets

from .models import ContactMessage
from .serializers import ContactMessageSerializer
from .permissions import IsAdminOrCreateOnly
from common.pagination import PortfolioPagination


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by(
        "is_read",
        "-created_at"
    )
    serializer_class = ContactMessageSerializer
    permission_classes = [IsAdminOrCreateOnly]
    pagination_class = PortfolioPagination

from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import ContactMessage

class ContactMessageAPITest(APITestCase):

    def setUp(self):

        User = get_user_model()

        self.admin_user = User.objects.create_user(
            username="admin",
            password="testpassword123",
            is_staff=True,
        )

    def test_public_user_can_create_contact_message(self):

        url = reverse("contact-list")

        data = {
            "name": "Rocky",
            "email": "rocky@example.com",
            "subject": "Portfolio Inquiry",
            "message": "Hello, I would like to contact you.",
        }

        response = self.client.post(
            url,
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            ContactMessage.objects.count(),
            1
        )

    def test_public_user_cannot_get_contact_messages(self):

        url = reverse("contact-list")

        response = self.client.get(url)

        self.assertIn(
            response.status_code,
            [
                status.HTTP_401_UNAUTHORIZED,
                status.HTTP_403_FORBIDDEN,
            ]
        )

    def test_admin_can_get_contact_messages(self):

        ContactMessage.objects.create(
            name="Test User",
            email="test@example.com",
            subject="Test Subject",
            message="Test message",
        )

        self.client.force_authenticate(
            user=self.admin_user
        )

        url = reverse("contact-list")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_public_user_cannot_delete_contact_message(self):

        contact_message = ContactMessage.objects.create(
            name="Test User",
            email="test@example.com",
            subject="Test Subject",
            message="Test message",
        )

        url = reverse(
            "contact-detail",
            kwargs={
                "pk": contact_message.id
            }
        )

        response = self.client.delete(url)

        self.assertIn(
            response.status_code,
            [
                status.HTTP_401_UNAUTHORIZED,
                status.HTTP_403_FORBIDDEN,
            ]
        )

    def test_admin_can_delete_contact_message(self):

        contact_message = ContactMessage.objects.create(
            name="Test User",
            email="test@example.com",
            subject="Test Subject",
            message="Test message",
        )

        self.client.force_authenticate(
            user=self.admin_user
        )

        url = reverse(
            "contact-detail",
            kwargs={
                "pk": contact_message.id
            }
        )

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            ContactMessage.objects.count(),
            0
        )

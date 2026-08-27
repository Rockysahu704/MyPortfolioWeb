from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class AuthenticationAPITest(APITestCase):

    def setUp(self):

        User = get_user_model()

        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123",
        )

    def test_user_can_login(self):

        url = reverse("login")

        data = {
            "username": "testuser",
            "password": "testpassword123",
        }

        response = self.client.post(
            url,
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertIn(
            "access",
            response.data
        )

        self.assertIn(
            "refresh",
            response.data
        )

    def test_user_cannot_login_with_wrong_password(self):

        url = reverse("login")

        data = {
            "username": "testuser",
            "password": "wrongpassword",
        }

        response = self.client.post(
            url,
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )
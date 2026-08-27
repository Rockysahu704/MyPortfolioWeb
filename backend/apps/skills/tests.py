from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase
from .serializers import SkillSerializer

from .models import Skill


class SkillModelTest(TestCase):

    def test_create_skill(self):

        skill = Skill.objects.create(
            name="Python",
            category="Backend",
            proficiency=90,
        )

        self.assertEqual(
            skill.name,
            "Python"
        )

        self.assertEqual(
            skill.category,
            "Backend"
        )

        self.assertEqual(
            skill.proficiency,
            90
        )

    def test_multiple_skills_can_be_created(self):

        Skill.objects.create(
            name="Python",
            category="Backend",
            proficiency=90,
        )

        Skill.objects.create(
            name="Django",
            category="Backend",
            proficiency=85,
        )

        skills_count = Skill.objects.count()

        self.assertEqual(
            skills_count,
            2
        )

    def test_invalid_proficiency(self):

        data = {
            "name": "Python",
            "category": "Backend",
            "proficiency": 150,
        }

        serializer = SkillSerializer(data=data)

        self.assertFalse(
            serializer.is_valid()
        )

        self.assertIn(
            "proficiency",
            serializer.errors
        )

    def test_valid_skill_data(self):

        data = {
            "name": "Python",
            "category": "Backend",
            "proficiency": 90,
        }

        serializer = SkillSerializer(data=data)

        self.assertTrue(
            serializer.is_valid()
        )
        

class SkillAPITest(APITestCase):

    def setUp(self):

        User = get_user_model()

        self.admin_user = User.objects.create_user(
            username="admin",
            password="testpassword123",
            is_staff=True,
        )

    def test_public_user_can_get_skills(self):

        Skill.objects.create(
            name="Python",
            category="Backend",
            proficiency=90,
        )

        url = reverse("skill-list")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_public_user_cannot_create_skill(self):

        url = reverse("skill-list")

        data = {
            "name": "Django",
            "category": "Backend",
            "proficiency": 90,
        }

        response = self.client.post(
            url,
            data,
            format="json"
        )

        self.assertIn(
            response.status_code,
            [
                status.HTTP_401_UNAUTHORIZED,
                status.HTTP_403_FORBIDDEN,
            ]
        )

    def test_admin_can_create_skill(self):

        self.client.force_authenticate(
            user=self.admin_user
        )

        url = reverse("skill-list")

        data = {
            "name": "Django",
            "category": "Backend",
            "proficiency": 95,
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
            Skill.objects.count(),
            1
        )

    def test_normal_user_cannot_create_skill(self):

        User = get_user_model()

        normal_user = User.objects.create_user(
            username="normaluser",
            password="testpassword123",
        )

        self.client.force_authenticate(
            user=normal_user
        )

        url = reverse("skill-list")

        data = {
            "name": "React",
            "category": "Frontend",
            "proficiency": 85,
        }

        response = self.client.post(
            url,
            data,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.test import Client

from data_entry.models import ProfessionEntry
from rest_framework.test import APITestCase

User = get_user_model()
c = Client()


class TestProfessionEntry(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User(
            password="asdfghjkl11",
            username="stickman",
            first_name="Thee",
            last_name="Stickman",

        )
        user.save()
        ProfessionEntry.objects.create(
            name="Doctor",
            description="Doctors treat",
            occupation="Pediatrician",
            created_by=user,
            created_at=timezone.now(),
            minimum_entry_age=20
        )

    def test_profession_entry_name_gets_created_correctly(self):
        profession = ProfessionEntry.objects.get(id=1)
        field_label = profession._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_name_max_length(self):
        profession = ProfessionEntry.objects.get(id=1)
        max_length = profession._meta.get_field("name").max_length
        self.assertEqual(max_length, 50)


class TestAPIList(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="john", password="asdfghjkl11", email="test@email.com"
        )
        response = self.client.post(
            "/api/v1/accounts/auth/token",
            {"username": "john", "password": "asdfghjkl11"},
        )
        ACCESS_TOKEN = response.json()["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + ACCESS_TOKEN)
        return super().setUp()

    def test_unauthenticated_users_cannot_fetch_categories(self):
        response = c.get(
            "/api/v1/entries/categories/",
        )
        assert response.status_code == 401

    def test_unauthenticated_users_cannot_add_categories(self):
        response = c.post(
            "/api/v1/entries/categories/",
        )
        assert response.status_code == 401

    def test_unauthenticated_users_cannot_modify_categories(self):
        response = c.put(
            "/api/v1/entries/categories/",
        )
        assert response.status_code == 401

    def test_unauthenticated_users_cannot_fetch_health_institutions(self):
        response = c.get(
            "/api/v1/entries/health-institutions/",
        )
        assert response.status_code == 401

    def test_unauthenticated_users_cannot_add_health_institutions(self):
        response = c.post(
            "/api/v1/entries/health-institutions/",
        )
        assert response.status_code == 401

    def test_unauthenticated_users_cannot_modify_health_institutions(self):
        response = c.put(
            "/api/v1/entries/health-institutions/",
        )
        assert response.status_code == 401

    def test_unauthenticated_users_cannot_fetch_professional_entries(self):
        response = c.get(
            "/api/v1/entries/professional-details/",
        )
        assert response.status_code == 401

    def test_unauthenticated_users_cannot_post_professional_entries(self):
        response = c.post(
            "/api/v1/entries/professional-details/",
        )
        assert response.status_code == 401

    def test_unauthenticated_users_cannot_modify_professional_entries(self):
        response = c.put(
            "/api/v1/entries/professional-details/",
        )
        assert response.status_code == 401

    def test_unauthenticated_users_cannot_fetch_event_details(self):
        response = c.get(
            "/api/v1/entries/event-details/",
        )
        assert response.status_code == 401

    def test_unauthenticated_users_cannot_post_event_details(self):
        response = c.post(
            "/api/v1/entries/event-details/",
        )
        assert response.status_code == 401

    def test_unauthenticated_users_cannot_modify_event_details(self):
        response = c.put(
            "/api/v1/entries/event-details/",
        )
        assert response.status_code == 401

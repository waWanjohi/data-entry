from django.contrib.auth import get_user_model
from django.test import Client
from rest_framework.test import APITestCase



c = Client()
User = get_user_model()


def _get_refresh_token():
    response = c.post(
        "/api/v1/accounts/auth/token", {"username": "john", "password": "asdfghjkl11"}
    )
    return response.json()["refresh"]


class TestUserAuthentication(APITestCase):
    def setUp(self) -> None:
        # create a user
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

    def test_user_authenticated(self):
        response = c.post(
            "/api/v1/accounts/auth/token", {"username": "john", "password": "asdfghjkl11"}
        )
        assert response.status_code == 200

    def test_unauthorized_user_is_not_authenticated(self):
        response = c.post(
            "/api/v1/accounts/auth/token",
            {"username": "john", "password": "wrong-password"},
        )
        assert response.status_code == 401

    def test_invalid_token_not_accepted(self):
        response = c.post(
            "/api/v1/accounts/auth/token",
            {"username": "john", "password": "wrong-password"},
        )
        print("response:", response)
        assert response.status_code == 401

    def test_refresh_token(self):
        refresh_token = _get_refresh_token()
        response = c.post(
            "/api/v1/accounts/auth/token/refresh", {"refresh": refresh_token}
        )
        assert response.status_code == 200

    def test_bad_request_method_not_allowed(self):
        response = c.get("/api/v1/accounts/auth/token/refresh", {"refresh": "bad-token"})
        assert response.status_code == 405

    def test_bad_request_body_not_json(self):
        response = c.post("/api/v1/accounts/auth/token/refresh", {"access": "bad-token"})
        assert response.status_code == 400

    def test_invalid_refresh_token(self):
        response = c.post("/api/v1/accounts/auth/token/refresh", {"refresh": "bad-token"})
        assert response.status_code == 401
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models import User
import datetime
import pytest


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(email="user@example.com", password="password", is_verified=True)
    return user

@pytest.mark.django_db
class TestPostApi:
    def test_get_post_response_200_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test title",
            "content": "test content",
            "status": True,
            "published_date": datetime.datetime.now(),
        }
        response = api_client.post(url, data=data)
        assert response.status_code == 401

    def test_create_post_response_201_status(self, api_client, common_user):
        # api_client.force_login(user=common_user)
        api_client.force_authenticate(user=common_user)
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test title",
            "content": "test content",
            "status": True,
            "published_date": datetime.datetime.now(),
        }
        response = api_client.post(url, data=data)
        assert response.status_code == 201

    def test_create_post_response_400_status(self, api_client, common_user):
        # api_client.force_login(user=common_user)
        api_client.force_authenticate(user=common_user)
        url = reverse("blog:api-v1:post-list")
        response = api_client.post(url, data={})
        assert response.status_code == 400
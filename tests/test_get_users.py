import pytest
from utils.api_client import APIClient
from utils.helper import response_logging
from config import BASE_URL

from jsonschema import validate
from schemas import get_user, get_users


@pytest.fixture
def api_client():
    return APIClient(BASE_URL)


def test_get_users_success(api_client):
    response = api_client.get("users?page=2")
    response_logging(response)
    assert response.status_code == 200
    # assert "data" in response.json()
    body = response.json()
    # Валидация ответа от сервера
    validate(body, get_users)


def test_get_single_user_success(api_client):
    response = api_client.get("users/1")
    response_logging(response)
    assert response.status_code == 200
    # assert "data" in response.json()
    body = response.json()
    # Валидация ответа от сервера
    validate(body, get_user)


def test_get_single_user_not_found(api_client):
    response = api_client.get("users/23")
    response_logging(response)
    assert response.status_code == 404
    assert response.json() == {}

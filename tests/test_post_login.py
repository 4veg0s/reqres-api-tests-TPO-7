import pytest
from utils.api_client import APIClient
from utils.helper import response_logging
from config import BASE_URL

from jsonschema import validate
from schemas import post_login_success, post_login_failure


@pytest.fixture
def api_client():
    return APIClient(BASE_URL)


def test_post_login_success(api_client):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = api_client.post("login", data=payload)
    response_logging(response)
    assert response.status_code == 200
    # assert "token" in response.json()
    body = response.json()
    # Валидация ответа от сервера
    validate(body, post_login_success)


def test_post_login_failure(api_client):
    payload = {
        "email": "peter@klaven",
    }
    response = api_client.post("login", data=payload)
    response_logging(response)
    assert response.status_code == 400
    # assert "error" in response.json()
    body = response.json()
    # Валидация ответа от сервера
    validate(body, post_login_failure)

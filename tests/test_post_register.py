import pytest
from utils.api_client import APIClient
from utils.helper import response_logging
from config import BASE_URL

from jsonschema import validate
from schemas import post_register_success, post_register_failure


@pytest.fixture
def api_client():
    return APIClient(BASE_URL)


def test_post_register_success(api_client):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = api_client.post("register", data=payload)
    response_logging(response)
    assert response.status_code == 200
    # assert "id" in body
    body = response.json()
    # Валидация ответа от сервера
    validate(body, post_register_success)


def test_post_register_failure(api_client):
    payload = {
        "email": "eve.holt@reqres.in",
    }
    response = api_client.post("register", data=payload)
    response_logging(response)
    assert response.status_code == 400
    # assert "error" in response.json()
    body = response.json()
    # Валидация ответа от сервера
    validate(body, post_register_failure)

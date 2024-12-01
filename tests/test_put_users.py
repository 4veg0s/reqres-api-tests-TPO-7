import pytest
from utils.api_client import APIClient
from utils.helper import response_logging
from config import BASE_URL

from jsonschema import validate
from schemas import put_user


@pytest.fixture
def api_client():
    return APIClient(BASE_URL)


def test_put_user_success(api_client):
    payload = {"name": "morpheus", "job": "zion resident"}
    response = api_client.put("users/2", data=payload)
    response_logging(response)
    assert response.status_code == 200
    assert response.json()["job"] == "zion resident"
    body = response.json()
    # Валидация ответа от сервера
    validate(body, put_user)

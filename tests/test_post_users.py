import pytest
from utils.api_client import APIClient
from utils.helper import response_logging
from config import BASE_URL


@pytest.fixture
def api_client():
    return APIClient(BASE_URL)


def test_post_user_success(api_client):
    payload = {"name": "morpheus", "job": "leader"}
    response = api_client.post("users", data=payload)
    response_logging(response)
    assert response.status_code == 201
    assert response.json()["name"] == "morpheus"

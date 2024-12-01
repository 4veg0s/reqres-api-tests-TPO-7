import pytest
from utils.api_client import APIClient
from utils.helper import response_logging
from config import BASE_URL


@pytest.fixture
def api_client():
    return APIClient(BASE_URL)


def test_delete_user_success(api_client):
    response = api_client.delete("users/2")
    response_logging(response)
    assert response.status_code == 204
    assert response.text == ""

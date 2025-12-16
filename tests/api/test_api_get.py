import requests
import pytest



@pytest.mark.api
def test_get_post_by_id(api_client):
    response = api_client.get("/posts/1")

    assert response.status_code == 200

    data = response.json()

    for key in ("userId", "id", "title", "body"):
        assert key in data

    assert data["id"] == 1
    assert isinstance(data["userId"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)

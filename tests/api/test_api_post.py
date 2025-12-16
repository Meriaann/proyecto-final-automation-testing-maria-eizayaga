import pytest

@pytest.mark.api
def test_post_create_post(api_client):
    payload = {
        "userId": 1,
        "title": "Test post",
        "body": "This is a test post"
    }

    response = api_client.post("/posts", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data




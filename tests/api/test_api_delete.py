import pytest


@pytest.mark.api
def test_delete_post_by_id(api_client):
    response = api_client.delete("/posts/1")

    assert response.status_code == 200
    assert response.text == "{}"


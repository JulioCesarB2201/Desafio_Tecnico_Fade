from app import create_app


def test_get_all_plans(client):

    response = client.get("/plans")

    assert response.status_code == 200

    data = response.get_json()

    assert "items" in data
    assert "total" in data
    assert "pages" in data
    assert "current_page" in data
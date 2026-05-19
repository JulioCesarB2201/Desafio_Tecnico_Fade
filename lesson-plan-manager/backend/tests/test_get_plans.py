from app import create_app


def test_get_all_plans():

    app = create_app()
    client = app.test_client()
    response = client.get("/plans")

    assert response.status_code == 200

    data = response.get_json()

    assert "items" in data
    assert "total" in data
    assert "pages" in data
    assert "current_page" in data
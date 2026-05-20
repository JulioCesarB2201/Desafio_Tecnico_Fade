from app import create_app


def test_generate_plan(client):

    response = client.post(
        "/plans/generate",
        json={
            "topic": "TCP/IP"
        }
    )

    data = response.get_json()

    assert response.status_code == 201

    assert "id" in data

    assert data["title"] == (
        "Introdução a TCP/IP"
    )
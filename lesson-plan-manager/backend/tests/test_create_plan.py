from app import create_app


def test_create_lesson_plan():
    app = create_app()
    client = app.test_client()

    payload = {
        "title": "OSPF Básico",
        "objective": "Aprender OSPF",
        "summary": "Introdução ao protocolo",
        "planned_date": "2026-05-20",
        "discipline": "Redes",
        "contents": "OSPF, LSA",
        "support_resources": "Packet Tracer",
        "tags": "redes,ospf"
    }

    response = client.post(
        "/plans",
        json=payload
    )

    assert response.status_code == 201
    data = response.get_json()

    assert data["title"] == payload["title"]
    assert data["discipline"] == payload["discipline"]
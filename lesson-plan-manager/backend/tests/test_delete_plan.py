from app import create_app


def test_delete_plan():
    
    app = create_app()
    client = app.test_client()

    payload = {
        "title": "Plano Temporário",
        "objective": "Teste",
        "summary": "Teste",
        "planned_date": "2026-05-20",
        "discipline": "Teste",
        "contents": "Teste",
        "support_resources": "Teste",
        "tags": "teste"
    }

    create_response = client.post(
        "/plans",
        json=payload
    )

    created_data = create_response.get_json()
    plan_id = created_data["id"]

    delete_response = client.delete(
        f"/plans/{plan_id}"
    )

    assert delete_response.status_code == 200
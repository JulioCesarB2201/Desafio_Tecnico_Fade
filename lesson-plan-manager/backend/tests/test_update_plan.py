from app import create_app


def test_update_plan(client):

    payload = {
        "title": "Plano Original",
        "objective": "Objetivo",
        "summary": "Resumo",
        "planned_date": "2026-05-20",
        "discipline": "Redes",
        "contents": "Conteúdo",
        "support_resources": "Livro",
        "tags": "tag"
    }

    create_response = client.post(
        "/plans",
        json=payload
    )

    created_data = create_response.get_json()
    plan_id = created_data["id"]

    updated_payload = {
        "title": "Plano Atualizado"
    }

    update_response = client.put(
        f"/plans/{plan_id}",
        json=updated_payload
    )

    assert update_response.status_code == 200
    updated_data = update_response.get_json()

    assert (
        updated_data["title"]
        == "Plano Atualizado"
    )
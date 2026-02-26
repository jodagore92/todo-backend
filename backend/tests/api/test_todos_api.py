from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

BASE_URL = "/api/v1/todos"


def test_get_all_todos():
    response = client.get(f"{BASE_URL}/")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2


def test_get_todo_by_id_found():
    response = client.get(f"{BASE_URL}/1")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Test 1"


def test_get_todo_by_id_not_found():
    response = client.get(f"{BASE_URL}/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "ToDo no encontrado"


def test_create_todo_success():
    payload = {
        "title": "Nuevo todo",
        "description": "Descripción",
        "completed": False
    }

    response = client.post(f"{BASE_URL}/", json=payload)
    assert response.status_code == 201

    data = response.json()
    assert data["id"] > 0
    assert data["title"] == "Nuevo todo"
    assert data["completed"] is False


def test_create_todo_invalid_payload():
    payload = {
        "description": "Sin título"
    }

    response = client.post(f"{BASE_URL}/", json=payload)
    assert response.status_code == 422


def test_update_todo_success():
    payload = {
        "completed": True
    }

    response = client.put(f"{BASE_URL}/1", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert data["completed"] is True


def test_update_todo_not_found():
    payload = {
        "completed": True
    }

    response = client.put(f"{BASE_URL}/999", json=payload)
    assert response.status_code == 404
    assert response.json()["detail"] == "ToDo no encontrado"


def test_delete_todo_success():
    response = client.delete(f"{BASE_URL}/1")
    assert response.status_code == 204


def test_delete_todo_not_found():
    response = client.delete(f"{BASE_URL}/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "ToDo no encontrado"

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services import todo_service


@pytest.fixture(autouse=True)
def reset_fake_db():
    todo_service.reset_fake_data()


@pytest.fixture
def client():
    return TestClient(app)

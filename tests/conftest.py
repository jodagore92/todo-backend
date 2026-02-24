import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services import todo_service

@pytest.fixture
def client():
    return TestClient(app)

import pytest
from app.repositories import todo_repository


@pytest.fixture(autouse=True)
def reset_repository():
    todo_repository._todos.clear()
    todo_repository._next_id = 1

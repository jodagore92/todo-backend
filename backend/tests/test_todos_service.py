import pytest
from app.services import todo_service
from app.schemas.todo import TodoCreate, TodoUpdate
from app.repositories import todo_repository

# Fixture para resetear el "fake DB" antes de cada test
@pytest.fixture(autouse=True)
def reset_data():
    # Limpiar repositorio
    todo_repository._todos.clear()
    todo_repository._next_id = 1

    # Cargar datos base usando el SERVICE (no internals)
    todo_service.create_todo(TodoCreate(title="Test 1"))
    todo_service.create_todo(TodoCreate(title="Test 2"))

def test_get_all_todos():
    todos = todo_service.get_all_todos()
    assert len(todos) == 2

def test_get_todo_by_id_found():
    todo = todo_service.get_todo_by_id(1)
    assert todo is not None
    assert todo.title == "Test 1"

def test_get_todo_by_id_not_found():
    todo = todo_service.get_todo_by_id(999)
    assert todo is None

def test_create_todo():
    new_todo = TodoCreate(title="Nuevo ToDo")
    created = todo_service.create_todo(new_todo)

    assert created.id > 0
    assert created.title == "Nuevo ToDo"
    assert created.completed is False

def test_update_todo():
    update = TodoUpdate(completed=True)
    updated = todo_service.update_todo(1, update)

    assert updated is not None
    assert updated.completed is True

def test_update_todo_not_found():
    update = TodoUpdate(title="No existe")
    updated = todo_service.update_todo(999, update)

    assert updated is None

def test_delete_todo():
    deleted = todo_service.delete_todo(1)
    assert deleted is True
    assert todo_service.get_todo_by_id(1) is None

def test_delete_todo_not_found():
    deleted = todo_service.delete_todo(999)
    assert deleted is False

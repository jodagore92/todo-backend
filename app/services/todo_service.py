from typing import List, Dict
from app.schemas.todo import TodoCreate, TodoUpdate

# Simulación de base de datos (temporal)
_fake_todos: List[Dict] = [
    {"id": 1, "title": "Aprender FastAPI", "description": None, "completed": False},
    {"id": 2, "title": "Conectar con React", "description": None, "completed": False},
]

def get_all_todos():
    return _fake_todos

def get_todo_by_id(todo_id: int):
    return next((todo for todo in _fake_todos if todo["id"] == todo_id), None)

def create_todo(todo: TodoCreate):
    new_todo = {
        "id": _fake_todos[-1]["id"] + 1 if _fake_todos else 1,
        **todo.dict()
    }
    _fake_todos.append(new_todo)
    return new_todo

def update_todo(todo_id: int, todo_update: TodoUpdate):
    todo = get_todo_by_id(todo_id)
    if not todo:
        return None

    update_data = todo_update.dict(exclude_unset=True)
    todo.update(update_data)
    return todo

def delete_todo(todo_id: int):
    todo = get_todo_by_id(todo_id)
    if not todo:
        return False

    _fake_todos.remove(todo)
    return True

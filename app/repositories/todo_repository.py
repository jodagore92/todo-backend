from typing import List, Optional
from app.models.todo import Todo

_todos: List[Todo] = []
_next_id = 1


def get_all() -> List[Todo]:
    return _todos


def get_by_id(todo_id: int) -> Optional[Todo]:
    return next((t for t in _todos if t.id == todo_id), None)


def create(todo: Todo) -> Todo:
    global _next_id
    todo.id = _next_id
    _next_id += 1
    _todos.append(todo)
    return todo


def update(todo: Todo) -> Todo:
    for i, t in enumerate(_todos):
        if t.id == todo.id:
            _todos[i] = todo
            return todo
    raise ValueError("Todo not found")


def delete(todo_id: int) -> None:
    global _todos
    _todos = [t for t in _todos if t.id != todo_id]

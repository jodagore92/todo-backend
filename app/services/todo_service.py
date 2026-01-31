from typing import List, Optional
from app.schemas.todo import TodoCreate, TodoUpdate
from app.models.todo import Todo
from app.repositories import todo_repository


def get_all_todos() -> List[Todo]:
    return todo_repository.get_all()


def get_todo_by_id(todo_id: int) -> Optional[Todo]:
    return todo_repository.get_by_id(todo_id)


def create_todo(todo: TodoCreate) -> Todo:
    new_todo = Todo(
        id=0,
        **todo.model_dump()
    )
    return todo_repository.create(new_todo)


def update_todo(todo_id: int, todo_update: TodoUpdate) -> Optional[Todo]:
    todo = todo_repository.get_by_id(todo_id)
    if not todo:
        return None

    update_data = todo_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(todo, key, value)

    return todo_repository.update(todo)


def delete_todo(todo_id: int) -> bool:
    todo = todo_repository.get_by_id(todo_id)
    if not todo:
        return False

    todo_repository.delete(todo_id)
    return True

def reset_fake_data():
    todo_repository.reset_fake_data()
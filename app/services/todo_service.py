from sqlalchemy.orm import Session
from typing import List, Optional

from app.schemas.todo import TodoCreate, TodoUpdate
from app.models.todo import Todo
from app.repositories import todo_repository


def get_all_todos(db: Session) -> List[Todo]:
    return todo_repository.get_all(db)


def get_todo_by_id(db: Session, todo_id: int) -> Optional[Todo]:
    return todo_repository.get_by_id(db, todo_id)


def create_todo(db: Session, todo: TodoCreate) -> Todo:
    new_todo = Todo(**todo.model_dump())
    return todo_repository.create(db, new_todo)


def update_todo(db: Session, todo_id: int, todo_update: TodoUpdate) -> Optional[Todo]:
    todo = todo_repository.get_by_id(db, todo_id)
    if not todo:
        return None

    update_data = todo_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(todo, key, value)

    return todo_repository.update(db, todo)


def delete_todo(db: Session, todo_id: int) -> bool:
    return todo_repository.delete(db, todo_id)

from sqlalchemy.orm import Session
from app.models.todo import Todo


def get_all(db: Session):
    return db.query(Todo).all()


def get_by_id(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()


def create(db: Session, todo: Todo):
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def update(db: Session, todo: Todo):
    db.commit()
    db.refresh(todo)
    return todo


def delete(db: Session, todo_id: int):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo:
        db.delete(todo)
        db.commit()
        return True
    return False

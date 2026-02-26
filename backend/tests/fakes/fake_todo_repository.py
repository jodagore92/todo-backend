from app.models.todo import Todo

_fake_db = []

def reset():
    _fake_db.clear()
    _fake_db.extend([
        Todo(id=1, title="Test 1", description=None, completed=False),
        Todo(id=2, title="Test 2", description=None, completed=False),
    ])

def get_all():
    return _fake_db

def get_by_id(todo_id: int):
    return next((t for t in _fake_db if t.id == todo_id), None)

def create(todo: Todo):
    todo.id = len(_fake_db) + 1
    _fake_db.append(todo)
    return todo

def update(todo: Todo):
    return todo

def delete(todo_id: int):
    _fake_db[:] = [t for t in _fake_db if t.id != todo_id]

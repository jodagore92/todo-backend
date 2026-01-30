from fastapi import APIRouter

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("/")
def get_todos():
    return [
        {"id": 1, "title": "Aprender FastAPI", "completed": False},
        {"id": 2, "title": "Conectar con React", "completed": False}
    ]

from fastapi import FastAPI
from app.api.v1 import api_router
from app.core.database import engine, Base
from app.models import todo  # IMPORTANTE para registrar el modelo

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ToDo API", redirect_slashes=True)

app.include_router(api_router)
    
@app.get("/")
def read_root():
    return {"message": "ToDo API funcionando 🚀"}

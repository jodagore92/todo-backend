from fastapi import FastAPI
from app.api.v1 import api_router

app = FastAPI(title="ToDo API")

app.include_router(api_router)
    
@app.get("/")
def read_root():
    return {"message": "ToDo API funcionando 🚀"}

from fastapi import FastAPI
from app.api.v1 import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ToDo API", redirect_slashes=True)

origins = [
    "http://localhost:3000",   # React
    "http://localhost:5173",   # Vite
    "http://localhost:4200",   # Angular
    "http://localhost:80",   # Postman o navegador
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
    
@app.get("/")
def read_root():
    return {"message": "ToDo API funcionando 🚀"}

from fastapi import FastAPI
from app.api.v1 import api_router
from fastapi.middleware.cors import CORSMiddleware
# Manejo de errores
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from app.core.exceptions import AppException

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

@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "code": exc.code
        }
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "code": "INTERNAL_ERROR"
        }
    )
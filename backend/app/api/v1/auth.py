from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user import UserCreate, UserLogin, Token
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])
service = AuthService()

@router.post("/register")
def register(data: UserCreate, db: Session = Depends(get_db)):
    user = service.register(db, data.email, data.password)
    return {"id": user.id, "email": user.email}

@router.post("/login", response_model=Token)
def login(data: UserLogin, db: Session = Depends(get_db)):
    token = service.login(db, data.email, data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"access_token": token}
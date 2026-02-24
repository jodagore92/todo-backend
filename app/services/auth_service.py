from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.core.security import hash_password, verify_password, create_access_token

repo = UserRepository()

class AuthService:

    def register(self, db: Session, email: str, password: str):
        hashed = hash_password(password)
        return repo.create(db, email, hashed)

    def login(self, db: Session, email: str, password: str):
        user = repo.get_by_email(db, email)
        if not user:
            return None

        if not verify_password(password, user.password):
            return None

        token = create_access_token({"sub": user.email})
        return token
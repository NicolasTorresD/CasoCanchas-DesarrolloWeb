from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.auth import UserCreate, UserOut, Token
from app.core.security import hash_password, create_access_token
from app.core.dependencies import get_db

class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def register_user(self, user_create: UserCreate) -> UserOut:
        # Check if the user already exists
        existing_user = self.db.query(User).filter(User.email == user_create.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        # Hash the password and create the user
        hashed_password = hash_password(user_create.password)
        new_user = User(
            email=user_create.email,
            password=hashed_password,
            name=user_create.name
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        return UserOut.from_orm(new_user)

    def login_user(self, email: str, password: str) -> Token:
        user = self.db.query(User).filter(User.email == email).first()
        if not user or not user.verify_password(password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        # Create JWT token
        access_token = create_access_token(data={"sub": user.email})
        return Token(access_token=access_token, token_type="bearer")
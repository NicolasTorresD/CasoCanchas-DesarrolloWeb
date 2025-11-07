from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.auth import UserCreate, UserLogin, Token
from app.services.auth_service import AuthService
from app.core.dependencies import get_db

router = APIRouter()

@router.post("/register", response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """Register a new user and return a JWT token."""
    auth_service = AuthService(db)
    token = auth_service.register_user(user)
    return token

@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    """Login a user and return a JWT token."""
    auth_service = AuthService(db)
    token = auth_service.authenticate_user(user)
    return token
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.auth import UserCreate, UserLogin, UserOut, Token
from app.services.auth_service import AuthService
from app.database import get_db

router = APIRouter()

@router.post("/register", response_model=UserOut, status_code=201)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """Registrar un nuevo usuario"""
    auth_service = AuthService(db)
    new_user = auth_service.register_user(user)
    return new_user

@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    """Iniciar sesión y obtener token JWT"""
    auth_service = AuthService(db)
    token = auth_service.login_user(user.email, user.password)
    return token
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    """Schema para crear un nuevo usuario"""
    nombre: str
    email: EmailStr
    telefono: str
    password: str

class UserLogin(BaseModel):
    """Schema para login de usuario"""
    email: EmailStr
    password: str

class UserOut(BaseModel):
    """Schema para retornar datos del usuario (sin password)"""
    id_usuario: int
    nombre: str
    email: EmailStr
    telefono: str
    fecha_registro: datetime
    activo: bool

    class Config:
        from_attributes = True  # Permite convertir desde modelos SQLAlchemy

class Token(BaseModel):
    """Schema para el token JWT"""
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    """Schema para datos decodificados del token"""
    email: Optional[str] = None
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    nombre: str = Field(..., max_length=100)
    email: EmailStr
    telefono: Optional[str] = Field(None, max_length=20)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserResponse(BaseModel):
    """Schema para retornar datos del usuario (sin password)"""
    id_usuario: int
    nombre: str
    email: EmailStr
    telefono: Optional[str]
    fecha_registro: datetime
    activo: bool

    class Config:
        from_attributes = True

class User(UserBase):
    id_usuario: int

    class Config:
        from_attributes = True

class UserInDB(User):
    hashed_password: str
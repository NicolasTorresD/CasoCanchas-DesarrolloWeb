from pydantic import BaseModel
from typing import Optional

class CanchaBase(BaseModel):
    nombre: str
    id_deporte: int
    imagen_url: Optional[str] = None
    color: Optional[str] = '#000000'
    precio_hora: float
    estado: str = "Disponible"

class CanchaCreate(CanchaBase):
    """Schema para crear una cancha (el código se genera automáticamente)"""
    codigo: Optional[str] = None  # Opcional, se genera automáticamente si no se proporciona

class CanchaUpdate(BaseModel):
    """Schema para actualizar una cancha"""
    nombre: Optional[str] = None
    id_deporte: Optional[int] = None
    codigo: Optional[str] = None
    imagen_url: Optional[str] = None
    color: Optional[str] = None
    precio_hora: Optional[float] = None
    estado: Optional[str] = None

class CanchaResponse(BaseModel):
    """Schema para retornar datos de la cancha"""
    id_cancha: int
    id_deporte: int
    nombre: str
    codigo: str
    imagen_url: Optional[str]
    color: Optional[str]
    precio_hora: float
    estado: str

    class Config:
        from_attributes = True

class Cancha(CanchaBase):
    id_cancha: int
    codigo: str

    class Config:
        from_attributes = True
from pydantic import BaseModel
from typing import Optional

class CanchaBase(BaseModel):
    nombre: str
    codigo: str
    imagen_url: Optional[str] = None
    color: Optional[str] = '#000000'
    precio_hora: float
    estado: str

class CanchaCreate(CanchaBase):
    pass

class CanchaUpdate(CanchaBase):
    pass

class CanchaResponse(BaseModel):
    """Schema para retornar datos de la cancha"""
    id_cancha: int
    nombre: str
    codigo: str
    imagen_url: Optional[str]
    color: Optional[str]
    precio_hora: float
    estado: str

    class Config:
        from_attributes = True
        orm_mode = True

class Cancha(CanchaBase):
    id_cancha: int

    class Config:
        from_attributes = True
        orm_mode = True
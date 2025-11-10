from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class ReservaBase(BaseModel):
    id_usuario: int
    id_cancha: int
    fecha: date
    hora: time
    duracion: int
    estado: str
    precio_total: float

class ReservaCreate(ReservaBase):
    pass

class ReservaUpdate(ReservaBase):
    estado: Optional[str] = None
    precio_total: Optional[float] = None

class ReservaResponse(BaseModel):
    """Schema para retornar datos de la reserva"""
    id_reserva: int
    id_usuario: int
    id_cancha: int
    fecha: date
    hora: time
    duracion: int
    estado: str
    precio_total: float

    class Config:
        from_attributes = True

class Reserva(ReservaBase):
    id_reserva: int

    class Config:
        from_attributes = True
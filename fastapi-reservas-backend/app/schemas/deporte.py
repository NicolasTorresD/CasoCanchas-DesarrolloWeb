from pydantic import BaseModel
from typing import Optional

class DeporteBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None

class DeporteCreate(DeporteBase):
    pass

class DeporteUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None

class DeporteResponse(DeporteBase):
    id_deporte: int

    class Config:
        from_attributes = True

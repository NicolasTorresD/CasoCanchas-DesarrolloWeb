from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FeedbackBase(BaseModel):
    calificacion: int
    comentario: Optional[str] = None

class FeedbackCreate(FeedbackBase):
    pass

class FeedbackResponse(BaseModel):
    """Schema para retornar datos del feedback"""
    id_feedback: int
    id_reserva: int
    id_usuario: int
    id_cancha: int
    calificacion: int
    comentario: Optional[str]
    fecha: datetime
    # Campo adicional para exponer el nombre del usuario autor del feedback
    usuario_nombre: Optional[str] = None

    class Config:
        from_attributes = True

class Feedback(FeedbackBase):
    id_feedback: int
    id_reserva: int
    id_usuario: int
    id_cancha: int
    fecha: datetime
    usuario_nombre: Optional[str] = None

    class Config:
        from_attributes = True
"""
Modelo SQLAlchemy para la tabla Feedback
"""
from sqlalchemy import Column, Integer, Text, Date, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class Feedback(Base):
    __tablename__ = "feedbacks"
    
    # Columnas
    id_feedback = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_reserva = Column(Integer, ForeignKey("reservas.id_reserva"), nullable=False, unique=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False, index=True)
    id_cancha = Column(Integer, ForeignKey("canchas.id_cancha"), nullable=False, index=True)
    calificacion = Column(Integer, nullable=False, index=True)
    comentario = Column(Text, nullable=True)
    fecha = Column(Date, nullable=False, index=True)
    timestamp = Column(DateTime, server_default=func.now(), nullable=False)
    
    # Relaciones
    reserva = relationship("Reserva", back_populates="feedback")
    usuario = relationship("Usuario", back_populates="feedbacks")
    cancha = relationship("Cancha", back_populates="feedbacks")
    
    # Constraint: La calificación debe estar entre 1 y 5
    __table_args__ = (
        CheckConstraint('calificacion >= 1 AND calificacion <= 5', name='check_calificacion'),
    )
    
    def __repr__(self):
        return f"<Feedback(id={self.id_feedback}, cancha={self.id_cancha}, calificacion={self.calificacion})>"
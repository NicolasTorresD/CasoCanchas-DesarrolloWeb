from sqlalchemy import Column, Integer, ForeignKey, Text, Date, TIMESTAMP
from sqlalchemy.orm import relationship
from app.core.dependencies import Base

class Feedback(Base):
    __tablename__ = 'feedbacks'

    id_feedback = Column(Integer, primary_key=True, index=True)
    id_reserva = Column(Integer, ForeignKey('reservas.id_reserva'), unique=True)
    id_usuario = Column(Integer, ForeignKey('users.id_usuario'))
    id_cancha = Column(Integer, ForeignKey('canchas.id_cancha'))
    calificacion = Column(Integer, nullable=False)
    comentario = Column(Text, nullable=True)
    fecha = Column(Date, nullable=False)
    timestamp = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')

    reserva = relationship("Reserva", back_populates="feedbacks")
    usuario = relationship("User", back_populates="feedbacks")
    cancha = relationship("Cancha", back_populates="feedbacks")
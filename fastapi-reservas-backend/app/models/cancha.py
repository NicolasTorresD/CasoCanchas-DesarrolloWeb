from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Enum, TIMESTAMP
from sqlalchemy.orm import relationship
from app.core.dependencies import Base

class Cancha(Base):
    __tablename__ = 'canchas'

    id_cancha = Column(Integer, primary_key=True, index=True)
    id_deporte = Column(Integer, ForeignKey('deportes.id_deporte'), nullable=False)
    nombre = Column(String(100), nullable=False)
    codigo = Column(String(20), unique=True, nullable=False)
    imagen_url = Column(String(255))
    color = Column(String(7), default='#000000')
    precio_hora = Column(DECIMAL(10, 2), nullable=False)
    estado = Column(Enum('Disponible', 'Mantenimiento', 'Inactiva'), default='Disponible')
    fecha_creacion = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')

    deporte = relationship("Deporte", back_populates="canchas")
    reservas = relationship("Reserva", back_populates="cancha")
    feedbacks = relationship("Feedback", back_populates="cancha")
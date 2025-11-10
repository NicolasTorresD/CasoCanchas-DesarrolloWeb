"""
Modelo SQLAlchemy para la tabla Cancha
"""
from sqlalchemy import Column, Integer, String, Numeric, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum


class EstadoCancha(str, enum.Enum):
    """Enum para el estado de la cancha"""
    DISPONIBLE = "Disponible"
    MANTENIMIENTO = "Mantenimiento"
    INACTIVA = "Inactiva"


class Cancha(Base):
    __tablename__ = "canchas"
    
    # Columnas
    id_cancha = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_deporte = Column(Integer, ForeignKey("deportes.id_deporte"), nullable=False, index=True)
    nombre = Column(String(100), nullable=False)
    codigo = Column(String(20), nullable=False, unique=True, index=True)
    imagen_url = Column(String(255), nullable=True)
    color = Column(String(7), default="#000000", nullable=True)
    precio_hora = Column(Numeric(10, 2), nullable=False)
    estado = Column(Enum(EstadoCancha), default=EstadoCancha.DISPONIBLE, nullable=False, index=True)
    fecha_creacion = Column(DateTime, server_default=func.now(), nullable=False)
    
    # Relaciones
    deporte = relationship("Deporte", back_populates="canchas")
    reservas = relationship("Reserva", back_populates="cancha", cascade="all, delete-orphan")
    feedbacks = relationship("Feedback", back_populates="cancha", cascade="all, delete-orphan")
    horarios_disponibles = relationship("HorarioDisponible", back_populates="cancha", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Cancha(id={self.id_cancha}, nombre='{self.nombre}', codigo='{self.codigo}')>"
"""
Modelo SQLAlchemy para la tabla Reserva
"""
from sqlalchemy import Column, Integer, Date, Time, Enum, Numeric, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum


class EstadoReserva(str, enum.Enum):
    """Enum para el estado de la reserva"""
    RESERVADA = "Reservada"
    CANCELADA = "Cancelada"
    COMPLETADA = "Completada"


class Reserva(Base):
    __tablename__ = "reservas"
    
    # Columnas
    id_reserva = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False, index=True)
    id_cancha = Column(Integer, ForeignKey("canchas.id_cancha"), nullable=False, index=True)
    fecha = Column(Date, nullable=False, index=True)
    hora = Column(Time, nullable=False)
    duracion = Column(Integer, default=60, nullable=False, comment="Duración en minutos")
    estado = Column(Enum(EstadoReserva), default=EstadoReserva.RESERVADA, nullable=False, index=True)
    precio_total = Column(Numeric(10, 2), nullable=False)
    fecha_reserva = Column(DateTime, server_default=func.now(), nullable=False)
    fecha_cancelacion = Column(DateTime, nullable=True)
    
    # Relaciones
    usuario = relationship("Usuario", back_populates="reservas")
    cancha = relationship("Cancha", back_populates="reservas")
    feedback = relationship("Feedback", back_populates="reserva", uselist=False, cascade="all, delete-orphan")
    
    # Constraint: No puede haber dos reservas para la misma cancha en la misma fecha y hora
    __table_args__ = (
        UniqueConstraint('id_cancha', 'fecha', 'hora', name='unique_reserva'),
    )
    
    def __repr__(self):
        return f"<Reserva(id={self.id_reserva}, cancha={self.id_cancha}, fecha='{self.fecha}', hora='{self.hora}')>"
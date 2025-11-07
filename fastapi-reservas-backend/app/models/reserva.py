from sqlalchemy import Column, Integer, ForeignKey, Date, Time, Enum, Numeric, TIMESTAMP
from sqlalchemy.orm import relationship
from app.core.dependencies import Base

class Reserva(Base):
    __tablename__ = 'reservas'

    id_reserva = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey('users.id_usuario'), nullable=False)
    id_cancha = Column(Integer, ForeignKey('canchas.id_cancha'), nullable=False)
    fecha = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    duracion = Column(Integer, default=60)  # Duration in minutes
    estado = Column(Enum('Reservada', 'Cancelada', 'Completada'), default='Reservada')
    precio_total = Column(Numeric(10, 2), nullable=False)
    fecha_reserva = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    fecha_cancelacion = Column(TIMESTAMP, nullable=True)

    usuario = relationship("User", back_populates="reservas")
    cancha = relationship("Cancha", back_populates="reservas")
    feedbacks = relationship("Feedback", back_populates="reserva")
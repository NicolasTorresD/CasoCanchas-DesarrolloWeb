from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.dependencies import Base

class User(Base):
    __tablename__ = 'users'

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    telefono = Column(String(20), nullable=True)
    password_hash = Column(String(255), nullable=False)
    fecha_registro = Column(TIMESTAMP, server_default=func.now())
    activo = Column(Boolean, default=True)
    
    # Relationships
    reservas = relationship("Reserva", back_populates="usuario")
    feedbacks = relationship("Feedback", back_populates="usuario")
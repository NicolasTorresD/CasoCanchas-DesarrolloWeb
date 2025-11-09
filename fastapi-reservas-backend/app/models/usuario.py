"""
Modelo SQLAlchemy para la tabla Usuario
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"
    
    # Columnas
    id_usuario = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False, index=True)
    email = Column(String(100), nullable=False, unique=True, index=True)
    telefono = Column(String(20), nullable=True)
    password_hash = Column(String(255), nullable=False)
    fecha_registro = Column(DateTime, server_default=func.now(), nullable=False)
    activo = Column(Boolean, default=True, nullable=False)
    
    # Relaciones
    reservas = relationship("Reserva", back_populates="usuario", cascade="all, delete-orphan")
    feedbacks = relationship("Feedback", back_populates="usuario", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Usuario(id={self.id_usuario}, nombre='{self.nombre}', email='{self.email}')>"

"""
Modelo SQLAlchemy para la tabla Deporte
"""
from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.orm import relationship
from app.database import Base


class Deporte(Base):
    __tablename__ = "deportes"
    
    # Columnas
    id_deporte = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50), nullable=False, unique=True, index=True)
    descripcion = Column(Text, nullable=True)
    activo = Column(Boolean, default=True, nullable=False)
    
    # Relaciones
    canchas = relationship("Cancha", back_populates="deporte", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Deporte(id={self.id_deporte}, nombre='{self.nombre}')>"
"""
Modelo SQLAlchemy para la tabla Horario Disponible
"""
from sqlalchemy import Column, Integer, Time, Boolean, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from app.database import Base


class HorarioDisponible(Base):
    __tablename__ = "horarios_disponibles"
    
    # Columnas
    id_horario = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_cancha = Column(Integer, ForeignKey("canchas.id_cancha"), nullable=False, index=True)
    dia_semana = Column(Integer, nullable=False, index=True, comment="0=Domingo, 6=Sábado")
    hora_inicio = Column(Time, nullable=False)
    hora_fin = Column(Time, nullable=False)
    activo = Column(Boolean, default=True, nullable=False)
    
    # Relaciones
    cancha = relationship("Cancha", back_populates="horarios_disponibles")
    
    # Constraint: El día de la semana debe estar entre 0 (Domingo) y 6 (Sábado)
    __table_args__ = (
        CheckConstraint('dia_semana >= 0 AND dia_semana <= 6', name='check_dia_semana'),
    )
    
    def __repr__(self):
        return f"<HorarioDisponible(id={self.id_horario}, cancha={self.id_cancha}, dia={self.dia_semana})>"

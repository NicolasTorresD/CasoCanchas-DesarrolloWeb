from sqlalchemy import Column, Integer, String, Boolean
from app.core.dependencies import Base

class Deporte(Base):
    __tablename__ = "deportes"

    id_deporte = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String, nullable=True)
    activo = Column(Boolean, default=True)
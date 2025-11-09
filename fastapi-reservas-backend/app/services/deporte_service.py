from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.deporte import Deporte

class DeporteService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_deportes(self) -> List[Deporte]:
        """Obtiene todos los deportes"""
        return self.db.query(Deporte).all()

    def get_deporte_by_id(self, deporte_id: int) -> Optional[Deporte]:
        """Obtiene un deporte por su ID"""
        deporte = self.db.query(Deporte).filter(Deporte.id_deporte == deporte_id).first()
        if not deporte:
            raise HTTPException(status_code=404, detail="Deporte not found")
        return deporte

    def get_deporte_by_nombre(self, nombre: str) -> Optional[Deporte]:
        """Obtiene un deporte por su nombre"""
        return self.db.query(Deporte).filter(Deporte.nombre.ilike(f"%{nombre}%")).first()

    def create_deporte(self, nombre: str, descripcion: str = None) -> Deporte:
        """Crea un nuevo deporte"""
        # Verificar que no exista
        existing = self.db.query(Deporte).filter(Deporte.nombre == nombre).first()
        if existing:
            raise HTTPException(status_code=400, detail="Deporte already exists")
        
        deporte = Deporte(nombre=nombre, descripcion=descripcion)
        self.db.add(deporte)
        self.db.commit()
        self.db.refresh(deporte)
        return deporte

    def update_deporte(self, deporte_id: int, nombre: str = None, descripcion: str = None) -> Deporte:
        """Actualiza un deporte existente"""
        deporte = self.get_deporte_by_id(deporte_id)
        
        if nombre:
            deporte.nombre = nombre
        if descripcion is not None:
            deporte.descripcion = descripcion
        
        self.db.commit()
        self.db.refresh(deporte)
        return deporte

    def delete_deporte(self, deporte_id: int):
        """Elimina un deporte"""
        deporte = self.get_deporte_by_id(deporte_id)
        self.db.delete(deporte)
        self.db.commit()
        return {"detail": "Deporte deleted successfully"}

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.deporte import DeporteCreate, DeporteUpdate, DeporteResponse
from app.services.deporte_service import DeporteService
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=List[DeporteResponse])
def read_deportes(db: Session = Depends(get_db)):
    """Obtener todos los deportes disponibles"""
    service = DeporteService(db)
    return service.get_all_deportes()

@router.get("/{deporte_id}", response_model=DeporteResponse)
def read_deporte(deporte_id: int, db: Session = Depends(get_db)):
    """Obtener un deporte por ID"""
    service = DeporteService(db)
    return service.get_deporte_by_id(deporte_id)

@router.post("/", response_model=DeporteResponse, status_code=201)
def create_deporte(deporte: DeporteCreate, db: Session = Depends(get_db)):
    """Crear un nuevo deporte"""
    service = DeporteService(db)
    return service.create_deporte(deporte.nombre, deporte.descripcion)

@router.put("/{deporte_id}", response_model=DeporteResponse)
def update_deporte(deporte_id: int, deporte: DeporteUpdate, db: Session = Depends(get_db)):
    """Actualizar un deporte existente"""
    service = DeporteService(db)
    return service.update_deporte(deporte_id, deporte.nombre, deporte.descripcion)

@router.delete("/{deporte_id}", status_code=200)
def delete_deporte(deporte_id: int, db: Session = Depends(get_db)):
    """Eliminar un deporte"""
    service = DeporteService(db)
    return service.delete_deporte(deporte_id)

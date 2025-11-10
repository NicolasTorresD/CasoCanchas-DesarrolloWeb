from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.cancha import CanchaCreate, CanchaUpdate, CanchaResponse
from app.services.cancha_service import CanchaService
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=CanchaResponse, status_code=201)
def create_cancha(cancha: CanchaCreate, db: Session = Depends(get_db)):
    """Crear una nueva cancha"""
    service = CanchaService(db)
    return service.create_cancha(cancha)

@router.get("/{cancha_id}", response_model=CanchaResponse)
def read_cancha(cancha_id: int, db: Session = Depends(get_db)):
    """Obtener una cancha por ID"""
    service = CanchaService(db)
    return service.get_cancha(cancha_id)

@router.get("/", response_model=List[CanchaResponse])
def read_canchas(deporte: str = None, db: Session = Depends(get_db)):
    """Obtener todas las canchas, opcionalmente filtradas por deporte"""
    service = CanchaService(db)
    if deporte:
        return service.get_canchas_by_deporte_nombre(deporte)
    return service.list_canchas()

@router.put("/{cancha_id}", response_model=CanchaResponse)
def update_cancha(cancha_id: int, cancha: CanchaUpdate, db: Session = Depends(get_db)):
    """Actualizar una cancha existente"""
    service = CanchaService(db)
    return service.update_cancha(cancha_id, cancha)

@router.delete("/{cancha_id}", status_code=204)
def delete_cancha(cancha_id: int, db: Session = Depends(get_db)):
    """Eliminar una cancha"""
    service = CanchaService(db)
    service.delete_cancha(cancha_id)
    return None
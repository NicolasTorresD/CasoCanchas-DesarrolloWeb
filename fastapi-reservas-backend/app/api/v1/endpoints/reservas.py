from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
from app.schemas.reserva import ReservaCreate, ReservaUpdate, ReservaResponse
from app.services.reserva_service import ReservaService
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=ReservaResponse, status_code=201)
def create_reserva(reserva: ReservaCreate, db: Session = Depends(get_db)):
    """Crear una nueva reserva"""
    service = ReservaService(db)
    return service.create_reserva(reserva)

@router.get("/{reserva_id}", response_model=ReservaResponse)
def read_reserva(reserva_id: int, db: Session = Depends(get_db)):
    """Obtener una reserva por ID"""
    service = ReservaService(db)
    return service.get_reserva(reserva_id)

@router.get("/", response_model=List[ReservaResponse])
def read_reservas(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    usuario_id: Optional[int] = None,
    cancha_id: Optional[int] = None,
    fecha: Optional[date] = None,
    db: Session = Depends(get_db)
):
    """Obtener todas las reservas con filtros opcionales"""
    service = ReservaService(db)
    
    if usuario_id:
        return service.get_reservas_by_usuario(usuario_id)
    elif cancha_id:
        return service.get_reservas_by_cancha(cancha_id, fecha)
    else:
        return service.list_reservas(skip=skip, limit=limit)

@router.put("/{reserva_id}", response_model=ReservaResponse)
def update_reserva(reserva_id: int, reserva: ReservaUpdate, db: Session = Depends(get_db)):
    """Actualizar una reserva existente"""
    service = ReservaService(db)
    return service.update_reserva(reserva_id, reserva)

@router.delete("/{reserva_id}", status_code=200)
def delete_reserva(reserva_id: int, db: Session = Depends(get_db)):
    """Cancelar una reserva (soft delete)"""
    service = ReservaService(db)
    return service.delete_reserva(reserva_id)
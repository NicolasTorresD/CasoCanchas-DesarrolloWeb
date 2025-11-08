from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.reserva import ReservaCreate, ReservaResponse
from app.services.reserva_service import ReservaService
from app.core.dependencies import get_db, get_current_user

router = APIRouter()

@router.post("/", response_model=ReservaResponse)
def create_reserva(reserva: ReservaCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return ReservaService.create_reserva(db=db, reserva=reserva, user_id=current_user.id)

@router.get("/{reserva_id}", response_model=ReservaResponse)
def read_reserva(reserva_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    reserva = ReservaService.get_reserva(db=db, reserva_id=reserva_id, user_id=current_user.id)
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva not found")
    return reserva

@router.get("/", response_model=list[ReservaResponse])
def read_reservas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return ReservaService.get_reservas(db=db, skip=skip, limit=limit, user_id=current_user.id)

@router.delete("/{reserva_id}", response_model=dict)
def delete_reserva(reserva_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    success = ReservaService.delete_reserva(db=db, reserva_id=reserva_id, user_id=current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Reserva not found")
    return {"detail": "Reserva deleted successfully"}
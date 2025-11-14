from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.schemas.feedback import FeedbackCreate, FeedbackResponse
from app.services import feedback_service
from app.database import get_db

router = APIRouter()

def _enrich(feedback):
    """Agrega el nombre del usuario al objeto ORM antes de serializar"""
    try:
        feedback.usuario_nombre = getattr(feedback.usuario, 'nombre', None)
    except Exception:
        feedback.usuario_nombre = None
    return feedback

@router.post("/reserva/{reserva_id}", response_model=FeedbackResponse, status_code=201)
def create_new_feedback(
    reserva_id: int,
    feedback: FeedbackCreate, 
    usuario_id: int,  # TODO: obtener del token de autenticación
    db: Session = Depends(get_db)
):
    """Crea un nuevo feedback para una reserva"""
    created = feedback_service.create_feedback(
        db=db, 
        feedback=feedback,
        id_reserva=reserva_id,
        id_usuario=usuario_id
    )
    return _enrich(created)

@router.get("/", response_model=List[FeedbackResponse])
def read_feedbacks(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """Obtiene lista de feedbacks con paginación"""
    items = feedback_service.get_feedbacks(db=db, skip=skip, limit=limit)
    return [_enrich(f) for f in items]

@router.get("/{feedback_id}", response_model=FeedbackResponse)
def read_feedback(feedback_id: int, db: Session = Depends(get_db)):
    """Obtiene un feedback por su ID"""
    feedback = feedback_service.get_feedback_by_id(db=db, feedback_id=feedback_id)
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return _enrich(feedback)

@router.get("/cancha/{cancha_id}", response_model=List[FeedbackResponse])
def read_feedbacks_by_cancha(
    cancha_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """Obtiene feedbacks de una cancha específica"""
    items = feedback_service.get_feedbacks_by_cancha(db=db, id_cancha=cancha_id, skip=skip, limit=limit)
    return [_enrich(f) for f in items]

@router.get("/usuario/{usuario_id}", response_model=List[FeedbackResponse])
def read_feedbacks_by_usuario(
    usuario_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """Obtiene feedbacks de un usuario específico"""
    items = feedback_service.get_feedbacks_by_usuario(db=db, id_usuario=usuario_id, skip=skip, limit=limit)
    return [_enrich(f) for f in items]

@router.delete("/{feedback_id}", status_code=200)
def delete_feedback(feedback_id: int, db: Session = Depends(get_db)):
    """Elimina un feedback"""
    return feedback_service.delete_feedback(db=db, feedback_id=feedback_id)
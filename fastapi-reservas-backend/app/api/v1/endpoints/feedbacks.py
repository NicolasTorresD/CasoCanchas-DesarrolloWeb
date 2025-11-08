from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.feedback import FeedbackCreate, FeedbackResponse
from app.services import feedback_service
from app.core.dependencies import get_db, get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/reserva/{reserva_id}", response_model=FeedbackResponse)
def create_new_feedback(
    reserva_id: int,
    feedback: FeedbackCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Crea un nuevo feedback para una reserva"""
    # Aquí deberías validar que la reserva existe y pertenece al usuario
    # Por ahora, asumimos que id_cancha viene de la reserva
    db_feedback = feedback_service.create_feedback(
        db=db, 
        feedback=feedback,
        id_reserva=reserva_id,
        id_usuario=current_user.id_usuario,
        id_cancha=1  # TODO: obtener de la reserva
    )
    if not db_feedback:
        raise HTTPException(status_code=400, detail="Feedback could not be created")
    return db_feedback

@router.get("/", response_model=list[FeedbackResponse])
def read_feedbacks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtiene lista de feedbacks"""
    feedbacks = feedback_service.get_feedbacks(db=db, skip=skip, limit=limit)
    return feedbacks

@router.get("/cancha/{cancha_id}", response_model=list[FeedbackResponse])
def read_feedbacks_by_cancha(cancha_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Obtiene feedbacks de una cancha específica"""
    feedbacks = feedback_service.get_feedbacks_by_cancha(db=db, id_cancha=cancha_id, skip=skip, limit=limit)
    return feedbacks
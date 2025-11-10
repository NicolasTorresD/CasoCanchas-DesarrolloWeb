from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from typing import List, Optional
from app.models.feedback import Feedback
from app.models.reserva import Reserva
from app.schemas.feedback import FeedbackCreate
from datetime import datetime

def create_feedback(db: Session, feedback: FeedbackCreate, id_reserva: int, id_usuario: int):
    """
    Crea un nuevo feedback en la base de datos.
    Valida que la reserva existe y obtiene el id_cancha automáticamente.
    """
    # Validar que la reserva existe
    reserva = db.query(Reserva).filter(Reserva.id_reserva == id_reserva).first()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva not found")
    
    # Validar que la reserva pertenece al usuario
    if reserva.id_usuario != id_usuario:
        raise HTTPException(status_code=403, detail="No tienes permiso para dar feedback a esta reserva")
    
    # Verificar si ya existe un feedback para esta reserva
    existing_feedback = db.query(Feedback).filter(Feedback.id_reserva == id_reserva).first()
    if existing_feedback:
        raise HTTPException(status_code=400, detail="Ya existe un feedback para esta reserva")
    
    try:
        db_feedback = Feedback(
            id_reserva=id_reserva,
            id_usuario=id_usuario,
            id_cancha=reserva.id_cancha,  # Obtener de la reserva
            calificacion=feedback.calificacion,
            comentario=feedback.comentario,
            fecha=datetime.now()
        )
        db.add(db_feedback)
        db.commit()
        db.refresh(db_feedback)
        return db_feedback
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Error al crear el feedback")

def get_feedbacks(db: Session, skip: int = 0, limit: int = 100) -> List[Feedback]:
    """
    Obtiene una lista de feedbacks de la base de datos.
    """
    return db.query(Feedback).offset(skip).limit(limit).all()

def get_feedback_by_id(db: Session, feedback_id: int) -> Optional[Feedback]:
    """
    Obtiene un feedback por su ID.
    """
    return db.query(Feedback).filter(Feedback.id_feedback == feedback_id).first()

def get_feedbacks_by_cancha(db: Session, id_cancha: int, skip: int = 0, limit: int = 100) -> List[Feedback]:
    """
    Obtiene feedbacks de una cancha específica.
    """
    return db.query(Feedback).filter(Feedback.id_cancha == id_cancha).offset(skip).limit(limit).all()

def get_feedbacks_by_usuario(db: Session, id_usuario: int, skip: int = 0, limit: int = 100) -> List[Feedback]:
    """
    Obtiene feedbacks de un usuario específico.
    """
    return db.query(Feedback).filter(Feedback.id_usuario == id_usuario).offset(skip).limit(limit).all()

def get_feedback_by_reserva(db: Session, id_reserva: int) -> Optional[Feedback]:
    """
    Obtiene el feedback de una reserva específica.
    """
    return db.query(Feedback).filter(Feedback.id_reserva == id_reserva).first()

def update_feedback(db: Session, feedback_id: int, calificacion: Optional[int] = None, comentario: Optional[str] = None):
    """
    Actualiza un feedback existente.
    """
    feedback = get_feedback_by_id(db, feedback_id)
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    
    if calificacion is not None:
        feedback.calificacion = calificacion
    if comentario is not None:
        feedback.comentario = comentario
    
    db.commit()
    db.refresh(feedback)
    return feedback

def delete_feedback(db: Session, feedback_id: int):
    """
    Elimina un feedback de la base de datos.
    """
    feedback = get_feedback_by_id(db, feedback_id)
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    
    db.delete(feedback)
    db.commit()
    return {"detail": "Feedback deleted successfully"}

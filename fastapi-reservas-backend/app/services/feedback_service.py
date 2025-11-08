from sqlalchemy.orm import Session
from app.models.feedback import Feedback
from app.schemas.feedback import FeedbackCreate
from datetime import datetime

def create_feedback(db: Session, feedback: FeedbackCreate, id_reserva: int, id_usuario: int, id_cancha: int):
    """
    Crea un nuevo feedback en la base de datos.
    """
    db_feedback = Feedback(
        id_reserva=id_reserva,
        id_usuario=id_usuario,
        id_cancha=id_cancha,
        calificacion=feedback.calificacion,
        comentario=feedback.comentario,
        fecha=datetime.now()
    )
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

def get_feedbacks(db: Session, skip: int = 0, limit: int = 100):
    """
    Obtiene una lista de feedbacks de la base de datos.
    """
    return db.query(Feedback).offset(skip).limit(limit).all()

def get_feedback_by_id(db: Session, feedback_id: int):
    """
    Obtiene un feedback por su ID.
    """
    return db.query(Feedback).filter(Feedback.id_feedback == feedback_id).first()

def get_feedbacks_by_cancha(db: Session, id_cancha: int, skip: int = 0, limit: int = 100):
    """
    Obtiene feedbacks de una cancha específica.
    """
    return db.query(Feedback).filter(Feedback.id_cancha == id_cancha).offset(skip).limit(limit).all()

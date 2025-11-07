# app/models/__init__.py

# Import all models so they are registered with SQLAlchemy Base
from app.models.user import User
from app.models.cancha import Cancha
from app.models.deporte import Deporte
from app.models.reserva import Reserva
from app.models.feedback import Feedback

__all__ = ['User', 'Cancha', 'Deporte', 'Reserva', 'Feedback']
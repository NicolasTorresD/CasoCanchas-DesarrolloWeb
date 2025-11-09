"""
Inicialización del paquete de modelos
Importa todos los modelos para que Alembic los detecte
"""
from app.database import Base
from app.models.usuario import Usuario
from app.models.deporte import Deporte
from app.models.cancha import Cancha
from app.models.reserva import Reserva
from app.models.feedback import Feedback
from app.models.horario_disponible import HorarioDisponible

# Exportar todos los modelos
__all__ = [
    "Base",
    "Usuario",
    "Deporte",
    "Cancha",
    "Reserva",
    "Feedback",
    "HorarioDisponible",
]
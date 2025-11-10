from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from datetime import date, time
from app.models.reserva import Reserva, EstadoReserva
from app.models.cancha import Cancha
from app.schemas.reserva import ReservaCreate, ReservaUpdate

class ReservaService:
    def __init__(self, db: Session):
        self.db = db

    def check_availability(self, id_cancha: int, fecha: date, hora: time, reserva_id: Optional[int] = None) -> bool:
        """Verifica si una cancha está disponible en una fecha y hora específica"""
        query = self.db.query(Reserva).filter(
            Reserva.id_cancha == id_cancha,
            Reserva.fecha == fecha,
            Reserva.hora == hora,
            Reserva.estado != EstadoReserva.CANCELADA
        )
        
        # Si estamos actualizando, excluir la reserva actual
        if reserva_id:
            query = query.filter(Reserva.id_reserva != reserva_id)
        
        existing = query.first()
        return existing is None

    def create_reserva(self, reserva: ReservaCreate):
        """Crea una nueva reserva verificando disponibilidad"""
        # Verificar que la cancha existe
        cancha = self.db.query(Cancha).filter(Cancha.id_cancha == reserva.id_cancha).first()
        if not cancha:
            raise HTTPException(status_code=404, detail="Cancha not found")
        
        # Verificar disponibilidad
        if not self.check_availability(reserva.id_cancha, reserva.fecha, reserva.hora):
            raise HTTPException(
                status_code=400, 
                detail="La cancha no está disponible en esa fecha y hora"
            )
        
        try:
            db_reserva = Reserva(**reserva.dict())
            self.db.add(db_reserva)
            self.db.commit()
            self.db.refresh(db_reserva)
            return db_reserva
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(
                status_code=400,
                detail="Error al crear la reserva. La cancha ya está reservada."
            )

    def get_reserva(self, reserva_id: int):
        """Obtiene una reserva por su ID"""
        reserva = self.db.query(Reserva).filter(Reserva.id_reserva == reserva_id).first()
        if not reserva:
            raise HTTPException(status_code=404, detail="Reserva not found")
        return reserva

    def get_reservas_by_usuario(self, id_usuario: int) -> List[Reserva]:
        """Obtiene todas las reservas de un usuario"""
        return self.db.query(Reserva).filter(Reserva.id_usuario == id_usuario).all()

    def get_reservas_by_cancha(self, id_cancha: int, fecha: Optional[date] = None) -> List[Reserva]:
        """Obtiene todas las reservas de una cancha, opcionalmente filtradas por fecha"""
        query = self.db.query(Reserva).filter(Reserva.id_cancha == id_cancha)
        if fecha:
            query = query.filter(Reserva.fecha == fecha)
        return query.all()

    def update_reserva(self, reserva_id: int, reserva_update: ReservaUpdate):
        """Actualiza una reserva existente"""
        reserva = self.db.query(Reserva).filter(Reserva.id_reserva == reserva_id).first()
        if not reserva:
            raise HTTPException(status_code=404, detail="Reserva not found")
        
        # Si se está cambiando fecha/hora/cancha, verificar disponibilidad
        update_dict = reserva_update.dict(exclude_unset=True)
        if any(key in update_dict for key in ['id_cancha', 'fecha', 'hora']):
            new_cancha = update_dict.get('id_cancha', reserva.id_cancha)
            new_fecha = update_dict.get('fecha', reserva.fecha)
            new_hora = update_dict.get('hora', reserva.hora)
            
            if not self.check_availability(new_cancha, new_fecha, new_hora, reserva_id):
                raise HTTPException(
                    status_code=400,
                    detail="La cancha no está disponible en esa fecha y hora"
                )
        
        for key, value in update_dict.items():
            setattr(reserva, key, value)
        
        try:
            self.db.commit()
            self.db.refresh(reserva)
            return reserva
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(
                status_code=400,
                detail="Error al actualizar la reserva"
            )

    def delete_reserva(self, reserva_id: int):
        """Elimina una reserva (soft delete cambiando estado a CANCELADA)"""
        reserva = self.db.query(Reserva).filter(Reserva.id_reserva == reserva_id).first()
        if not reserva:
            raise HTTPException(status_code=404, detail="Reserva not found")
        
        # Soft delete: cambiar estado a cancelada
        reserva.estado = EstadoReserva.CANCELADA
        self.db.commit()
        return {"detail": "Reserva cancelled successfully"}

    def list_reservas(self, skip: int = 0, limit: int = 100) -> List[Reserva]:
        """Obtiene todas las reservas con paginación"""
        return self.db.query(Reserva).offset(skip).limit(limit).all()
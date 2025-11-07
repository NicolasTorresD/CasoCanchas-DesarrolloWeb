from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.reserva import Reserva
from app.schemas.reserva import ReservaCreate, ReservaUpdate

class ReservaService:
    def __init__(self, db: Session):
        self.db = db

    def create_reserva(self, reserva: ReservaCreate):
        db_reserva = Reserva(**reserva.dict())
        self.db.add(db_reserva)
        self.db.commit()
        self.db.refresh(db_reserva)
        return db_reserva

    def get_reserva(self, reserva_id: int):
        reserva = self.db.query(Reserva).filter(Reserva.id == reserva_id).first()
        if not reserva:
            raise HTTPException(status_code=404, detail="Reserva not found")
        return reserva

    def update_reserva(self, reserva_id: int, reserva_update: ReservaUpdate):
        reserva = self.db.query(Reserva).filter(Reserva.id == reserva_id).first()
        if not reserva:
            raise HTTPException(status_code=404, detail="Reserva not found")
        for key, value in reserva_update.dict(exclude_unset=True).items():
            setattr(reserva, key, value)
        self.db.commit()
        self.db.refresh(reserva)
        return reserva

    def delete_reserva(self, reserva_id: int):
        reserva = self.db.query(Reserva).filter(Reserva.id == reserva_id).first()
        if not reserva:
            raise HTTPException(status_code=404, detail="Reserva not found")
        self.db.delete(reserva)
        self.db.commit()
        return {"detail": "Reserva deleted successfully"}
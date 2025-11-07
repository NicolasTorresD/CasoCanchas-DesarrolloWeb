from fastapi import HTTPException
from typing import List
from app.models.cancha import Cancha
from app.schemas.cancha import CanchaCreate, CanchaUpdate

class CanchaService:
    def __init__(self):
        self.canchas = []  # This will act as an in-memory storage for canchas

    def create_cancha(self, cancha_data: CanchaCreate) -> Cancha:
        new_cancha = Cancha(**cancha_data.dict())
        self.canchas.append(new_cancha)
        return new_cancha

    def get_cancha(self, cancha_id: int) -> Cancha:
        for cancha in self.canchas:
            if cancha.id == cancha_id:
                return cancha
        raise HTTPException(status_code=404, detail="Cancha not found")

    def update_cancha(self, cancha_id: int, cancha_data: CanchaUpdate) -> Cancha:
        for index, cancha in enumerate(self.canchas):
            if cancha.id == cancha_id:
                updated_cancha = cancha.copy(update=cancha_data.dict(exclude_unset=True))
                self.canchas[index] = updated_cancha
                return updated_cancha
        raise HTTPException(status_code=404, detail="Cancha not found")

    def delete_cancha(self, cancha_id: int) -> None:
        for index, cancha in enumerate(self.canchas):
            if cancha.id == cancha_id:
                del self.canchas[index]
                return
        raise HTTPException(status_code=404, detail="Cancha not found")

    def list_canchas(self) -> List[Cancha]:
        return self.canchas
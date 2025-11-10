from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.cancha import Cancha
from app.models.deporte import Deporte
from app.schemas.cancha import CanchaCreate, CanchaUpdate

class CanchaService:
    def __init__(self, db: Session):
        self.db = db

    def _generate_codigo(self, id_deporte: int) -> str:
        """Genera un código único para una cancha en formato CAN-XX"""
        # Contar cuántas canchas existen en total (no por deporte)
        count = self.db.query(Cancha).count()
        numero = count + 1
        
        # Generar código único con formato CAN-XX
        codigo = f"CAN-{numero:02d}"
        
        # Verificar si ya existe (por si acaso)
        while self.db.query(Cancha).filter(Cancha.codigo == codigo).first():
            numero += 1
            codigo = f"CAN-{numero:02d}"
        
        return codigo

    def create_cancha(self, cancha_data: CanchaCreate) -> Cancha:
        """Crea una nueva cancha en la base de datos"""
        # Generar código si no se proporciona
        codigo = cancha_data.codigo
        if not codigo:
            codigo = self._generate_codigo(cancha_data.id_deporte)
        else:
            # Verificar que el código no exista
            existing = self.db.query(Cancha).filter(Cancha.codigo == codigo).first()
            if existing:
                raise HTTPException(status_code=400, detail=f"El código '{codigo}' ya existe")
        
        # Crear la cancha
        cancha_dict = cancha_data.dict()
        cancha_dict['codigo'] = codigo
        new_cancha = Cancha(**cancha_dict)
        
        self.db.add(new_cancha)
        self.db.commit()
        self.db.refresh(new_cancha)
        return new_cancha

    def get_cancha(self, cancha_id: int) -> Cancha:
        """Obtiene una cancha por su ID"""
        cancha = self.db.query(Cancha).filter(Cancha.id_cancha == cancha_id).first()
        if not cancha:
            raise HTTPException(status_code=404, detail="Cancha not found")
        return cancha

    def get_cancha_by_codigo(self, codigo: str) -> Optional[Cancha]:
        """Obtiene una cancha por su código"""
        return self.db.query(Cancha).filter(Cancha.codigo == codigo).first()

    def update_cancha(self, cancha_id: int, cancha_data: CanchaUpdate) -> Cancha:
        """Actualiza una cancha existente"""
        cancha = self.db.query(Cancha).filter(Cancha.id_cancha == cancha_id).first()
        if not cancha:
            raise HTTPException(status_code=404, detail="Cancha not found")
        
        for key, value in cancha_data.dict(exclude_unset=True).items():
            setattr(cancha, key, value)
        
        self.db.commit()
        self.db.refresh(cancha)
        return cancha

    def delete_cancha(self, cancha_id: int) -> None:
        """Elimina una cancha de la base de datos"""
        cancha = self.db.query(Cancha).filter(Cancha.id_cancha == cancha_id).first()
        if not cancha:
            raise HTTPException(status_code=404, detail="Cancha not found")
        
        self.db.delete(cancha)
        self.db.commit()

    def list_canchas(self) -> List[Cancha]:
        """Obtiene todas las canchas"""
        return self.db.query(Cancha).all()

    def get_canchas_by_deporte(self, deporte_id: int) -> List[Cancha]:
        """Obtiene todas las canchas de un deporte específico"""
        return self.db.query(Cancha).filter(Cancha.id_deporte == deporte_id).all()
    
    def get_canchas_by_deporte_nombre(self, deporte_nombre: str) -> List[Cancha]:
        """Obtiene todas las canchas de un deporte por nombre"""
        deporte = self.db.query(Deporte).filter(Deporte.nombre == deporte_nombre).first()
        if not deporte:
            return []
        return self.db.query(Cancha).filter(Cancha.id_deporte == deporte.id_deporte).all()
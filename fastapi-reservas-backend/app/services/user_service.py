from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.usuario import Usuario
from app.schemas.user import UserCreate, UserResponse
from app.core.security import hash_password

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_create: UserCreate) -> Usuario:
        """Crear un nuevo usuario"""
        hashed_password = hash_password(user_create.password)
        user = Usuario(
            nombre=user_create.nombre,
            email=user_create.email,
            telefono=user_create.telefono,
            password_hash=hashed_password,
            activo=True
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_email(self, email: str) -> Optional[Usuario]:
        """Obtener usuario por email"""
        return self.db.query(Usuario).filter(Usuario.email == email).first()

    def get_user_by_id(self, user_id: int) -> Optional[Usuario]:
        """Obtener usuario por ID"""
        return self.db.query(Usuario).filter(Usuario.id_usuario == user_id).first()

    def list_users(self, skip: int = 0, limit: int = 100) -> List[Usuario]:
        """Listar todos los usuarios con paginación"""
        return self.db.query(Usuario).offset(skip).limit(limit).all()

    def update_user(self, user_id: int, user_update: UserCreate) -> Optional[Usuario]:
        """Actualizar un usuario existente"""
        user = self.get_user_by_id(user_id)
        if user:
            user.nombre = user_update.nombre
            user.telefono = user_update.telefono
            if user_update.password:
                user.password_hash = hash_password(user_update.password)
            self.db.commit()
            self.db.refresh(user)
            return user
        return None

    def delete_user(self, user_id: int) -> bool:
        """Eliminar un usuario"""
        user = self.get_user_by_id(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        return False
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.core.security import hash_password

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_create: UserCreate) -> UserResponse:
        hashed_password = hash_password(user_create.password)
        user = User(
            nombre=user_create.nombre,
            email=user_create.email,
            telefono=user_create.telefono,
            password_hash=hashed_password
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return UserResponse.from_orm(user)

    def get_user_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()

    def get_user_by_id(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id_usuario == user_id).first()

    def update_user(self, user_id: int, user_update: UserCreate) -> UserResponse:
        user = self.get_user_by_id(user_id)
        if user:
            user.nombre = user_update.nombre
            user.telefono = user_update.telefono
            if user_update.password:
                user.password_hash = hash_password(user_update.password)
            self.db.commit()
            self.db.refresh(user)
            return UserResponse.from_orm(user)
        return None

    def delete_user(self, user_id: int) -> bool:
        user = self.get_user_by_id(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        return False
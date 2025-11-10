from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas.auth import UserCreate, UserOut, Token
from app.core.security import hash_password, verify_password, create_access_token

class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def register_user(self, user_create: UserCreate) -> UserOut:
        """Registrar un nuevo usuario"""
        # Verificar si el usuario ya existe
        existing_user = self.db.query(Usuario).filter(Usuario.email == user_create.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        # Hashear la contraseña y crear el usuario
        hashed_password = hash_password(user_create.password)
        new_user = Usuario(
            nombre=user_create.nombre,
            email=user_create.email,
            telefono=user_create.telefono if hasattr(user_create, 'telefono') else None,
            password_hash=hashed_password,
            activo=True
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        return UserOut.from_orm(new_user)

    def login_user(self, email: str, password: str) -> Token:
        """Autenticar un usuario y generar token"""
        user = self.db.query(Usuario).filter(Usuario.email == email).first()
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        # Verificar contraseña
        if not verify_password(password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        # Crear JWT token
        access_token = create_access_token(data={"sub": user.email, "user_id": user.id_usuario})
        return Token(access_token=access_token, token_type="bearer", user_id=user.id_usuario)

    def get_user_by_email(self, email: str) -> Usuario:
        """Obtener usuario por email"""
        return self.db.query(Usuario).filter(Usuario.email == email).first()
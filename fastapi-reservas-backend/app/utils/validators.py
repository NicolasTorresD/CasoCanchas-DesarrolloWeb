from pydantic import BaseModel, EmailStr, constr, validator

class UserRegistration(BaseModel):
    email: EmailStr
    password: constr(min_length=8)

    @validator('password')
    def password_complexity(cls, value):
        if not any(char.isdigit() for char in value):
            raise ValueError('Password must contain at least one digit.')
        if not any(char.isupper() for char in value):
            raise ValueError('Password must contain at least one uppercase letter.')
        if not any(char.islower() for char in value):
            raise ValueError('Password must contain at least one lowercase letter.')
        return value

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    email: EmailStr
    password: constr(min_length=8, required=False)

    @validator('password', always=True)
    def validate_password(cls, value):
        if value and (not any(char.isdigit() for char in value) or
                      not any(char.isupper() for char in value) or
                      not any(char.islower() for char in value)):
            raise ValueError('Password must contain at least one digit, one uppercase letter, and one lowercase letter.')
        return value

class CanchaCreate(BaseModel):
    nombre: str
    codigo: constr(min_length=3, max_length=20)
    precio_hora: float

class ReservaCreate(BaseModel):
    id_cancha: int
    fecha: str
    hora: str
    duracion: int

class FeedbackCreate(BaseModel):
    id_cancha: int
    calificacion: int
    comentario: str

class DeporteCreate(BaseModel):
    nombre: str
    descripcion: str

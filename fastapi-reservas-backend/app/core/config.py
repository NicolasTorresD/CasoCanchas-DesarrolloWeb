from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Application settings
    APP_NAME: str = "FastAPI Reservas Backend"
    APP_VERSION: str = "1.0.0"
    
    # Security settings
    APP_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_TIME: int = 30
    BCRYPT_ROUNDS: int = 12

    # Database settings (to be implemented later)
    DATABASE_URL: str

    class Config:
        env_file = ".env"
        extra = "ignore"  # Ignora variables extra del .env

settings = Settings()
"""
Configuración de la base de datos con SQLAlchemy
Soporta MySQL (preparado para Docker) y SQLite (desarrollo local)
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener URL de la base de datos desde .env
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./reservas.db")

# Crear engine de SQLAlchemy
# Para MySQL/PostgreSQL: check_same_thread no aplica
# Para SQLite: necesitamos check_same_thread=False
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL, 
        connect_args={"check_same_thread": False}
    )
else:
    # MySQL/PostgreSQL/otros
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Crear SessionLocal para interactuar con la BD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Dependency para obtener la sesión de BD
def get_db():
    """
    Dependency que proporciona una sesión de base de datos
    y la cierra automáticamente después de usarla
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

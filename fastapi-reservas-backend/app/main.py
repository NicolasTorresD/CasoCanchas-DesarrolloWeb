from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import router as api_router
from app.database import Base, engine
# Import all models so they are registered with SQLAlchemy
from app.models import *
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.cancha import Cancha
from app.scripts import load_initial_data

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Reservas Backend",
    description="API for managing reservations, users, and feedback for sports courts.",
    version="1.0.0",
)

# CORS middleware to allow cross-origin requests
# CORS: enumerar orígenes explícitos para permitir credenciales (Authorization)
allowed_origins = [
    "http://localhost",
    "http://localhost:80",
    "http://127.0.0.1",
    "http://127.0.0.1:80",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Include the API router
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {
        "message": "Welcome to the FastAPI Reservas Backend!",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "database": "connected"}

@app.on_event("startup")
def startup_seed_data():
    """Semilla de datos iniciales si la base está vacía (canchas)."""
    try:
        db: Session = SessionLocal()
        count = db.query(Cancha).count()
        if count == 0:
            # Cargar datos iniciales desde JSON (deportes, canchas, usuarios, reservas, feedbacks)
            load_initial_data.main()
    except Exception as e:
        # Evitar que el fallo de semilla impida levantar la app
        print(f"[startup] Error cargando datos iniciales: {e}")
    finally:
        try:
            db.close()
        except Exception:
            pass
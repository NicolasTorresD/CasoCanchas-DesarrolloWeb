from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import router as api_router
from app.core.dependencies import Base, engine
# Import all models so they are registered with SQLAlchemy
import app.models

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Reservas Backend",
    description="API for managing reservations, users, and feedback for sports courts.",
    version="1.0.0",
)

# CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the API router
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Reservas Backend!"}
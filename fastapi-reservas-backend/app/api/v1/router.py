from fastapi import APIRouter
from app.api.v1.endpoints import auth, users, canchas, reservas, feedbacks

router = APIRouter()

# Include the authentication routes
router.include_router(auth.router, prefix="/auth", tags=["auth"])

# Include the user management routes
router.include_router(users.router, prefix="/users", tags=["users"])

# Include the court management routes
router.include_router(canchas.router, prefix="/canchas", tags=["canchas"])

# Include the reservation management routes
router.include_router(reservas.router, prefix="/reservas", tags=["reservas"])

# Include the feedback management routes
router.include_router(feedbacks.router, prefix="/feedbacks", tags=["feedbacks"])
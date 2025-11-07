from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.api.v1.endpoints.auth import router as auth_router
from app.schemas.auth import UserCreate, UserResponse

app = FastAPI()
app.include_router(auth_router)

client = TestClient(app)

def test_register_user():
    response = client.post("/api/v1/auth/register", json={
        "email": "testuser@example.com",
        "password": "testpassword"
    })
    assert response.status_code == 201
    assert response.json() == {"email": "testuser@example.com"}

def test_login_user():
    client.post("/api/v1/auth/register", json={
        "email": "testuser@example.com",
        "password": "testpassword"
    })
    response = client.post("/api/v1/auth/login", json={
        "email": "testuser@example.com",
        "password": "testpassword"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_invalid_user():
    response = client.post("/api/v1/auth/login", json={
        "email": "invaliduser@example.com",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid credentials"}
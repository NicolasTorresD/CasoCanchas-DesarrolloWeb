from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.reservas import router as reservas_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(reservas_router)

client = TestClient(app)

def test_register_user():
    response = client.post("/api/v1/auth/register", json={
        "email": "testuser@example.com",
        "password": "testpassword"
    })
    assert response.status_code == 201
    assert response.json()["email"] == "testuser@example.com"

def test_login_user():
    response = client.post("/api/v1/auth/login", json={
        "email": "testuser@example.com",
        "password": "testpassword"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_create_reserva():
    # First, log in to get the token
    login_response = client.post("/api/v1/auth/login", json={
        "email": "testuser@example.com",
        "password": "testpassword"
    })
    token = login_response.json()["access_token"]

    # Now, create a reservation
    response = client.post("/api/v1/reservas", json={
        "id_cancha": 1,
        "fecha": "2023-10-01",
        "hora": "10:00:00",
        "duracion": 60
    }, headers={"Authorization": f"Bearer {token}"})
    
    assert response.status_code == 201
    assert response.json()["id_cancha"] == 1

def test_get_reservas():
    # First, log in to get the token
    login_response = client.post("/api/v1/auth/login", json={
        "email": "testuser@example.com",
        "password": "testpassword"
    })
    token = login_response.json()["access_token"]

    # Now, get the reservations
    response = client.get("/api/v1/reservas", headers={"Authorization": f"Bearer {token}"})
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Should return a list of reservations
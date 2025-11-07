from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from app.schemas.auth import UserCreate, UserResponse
from app.services.auth_service import create_user, get_user_by_email

app = FastAPI()

client = TestClient(app)

@app.post("/register", response_model=UserResponse)
def register_user(user: UserCreate):
    existing_user = get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(user)

@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def test_register_user():
    response = client.post("/register", json={"email": "test@example.com", "password": "password123"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_register_user_existing_email():
    client.post("/register", json={"email": "test@example.com", "password": "password123"})
    response = client.post("/register", json={"email": "test@example.com", "password": "password123"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"

def test_read_user():
    response = client.post("/register", json={"email": "test2@example.com", "password": "password123"})
    user_id = response.json()["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["email"] == "test2@example.com"

def test_read_user_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
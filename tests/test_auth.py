import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app, login_attempts, registered_users
from fastapi.testclient import TestClient

client = TestClient(app)

def test_register_user():
    username = "testuser1"
    password = "testpass1"
    response = client.post("/register", params={"username": username, "password": password})
    assert response.status_code == 200
    assert "Usuario registrado exitosamente" in response.json()["msg"]
    assert username in registered_users

def test_login_success():
    username = "testuser2"
    password = "testpass2"
    client.post("/register", params={"username": username, "password": password})
    response = client.post("/login", params={"username": username, "password": password})
    assert response.status_code == 200
    assert response.json()["msg"] == "Login exitoso"

def test_user_block_after_failed_attempts():
    username = "blockeduser"
    password = "rightpass"
    client.post("/register", params={"username": username, "password": password})

    for _ in range(5):
        client.post("/login", params={"username": username, "password": "wrongpass"})

    response = client.post("/login", params={"username": username, "password": password})
    assert response.status_code == 403
    assert "bloqueado" in response.json()["detail"]

def test_password_not_plaintext():
    username = "secureuser"
    password = "mypassword"
    client.post("/register", params={"username": username, "password": password})
    assert registered_users[username] != password  # si usaras hash, debería estar diferente (esto se modificará al integrar bcrypt)

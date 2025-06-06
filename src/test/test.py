from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app
import bcrypt

client = TestClient(app)

def test_register_success():
    response = client.post("/register", params={"username": "joelArriola", "password": "Joelarriola123@"})
    print(" Registro exitoso:", response.json())
    assert response.status_code == 200
    assert response.json()["msg"] == "Usuario registrado exitosamente"

def test_register_duplicate_user():
    client.post("/register", params={"username": "testduplicate", "password": "Test123"})
    response = client.post("/register", params={"username": "testduplicate", "password": "Test123"})
    print("Registro duplicado:", response.json())
    assert response.status_code == 400
    assert "ya existe" in response.json()["detail"]

def test_register_invalid_username():
    response = client.post("/register", params={"username": "!", "password": "Test123"})
    print(" Registro con username inválido:", response.json())
    assert response.status_code == 400
    assert "inválido" in response.json()["detail"]

def test_login_success():
    client.post("/register", params={"username": "joelArriola", "password": "Joelarriola123@"})
    response = client.post("/login", params={"username": "joelArriola", "password": "Joelarriola123@"})
    print(" Login exitoso:", response.json())
    assert response.status_code == 200
    assert response.json()["msg"] == "usuario autenticado exitosamente"

def test_login_failed():
    response = client.post("/login", params={"username": "joelarriola", "password": "nocontraseña"})
    print(" Login fallido:", response.json())
    assert response.status_code == 401 or response.status_code == 403

def test_user_listing():
    client.post("/register", params={"username": "listuser", "password": "Test123"})
    response = client.get("/")
    print(" Lista de usuarios:", response.json())
    assert response.status_code == 200
    assert "users" in response.json()

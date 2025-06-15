from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app

client = TestClient(app)

def test_register_success():
    response = client.post("/auth/register", params={
        "username": "joelArriola",
        "password": "Joelarriola123@",
        "email": "joel@example.com"
    })
    print(" Registro exitoso:", response.json())
    assert response.status_code == 200
    assert response.json()["msg"] == "Usuario registrado exitosamente"

def test_register_duplicate_user():
    client.post("/auth/register", params={
        "username": "testduplicate",
        "password": "Test123",
        "email": "test1@example.com"
    })
    response = client.post("/auth/register", params={
        "username": "testduplicate",
        "password": "Test123",
        "email": "test1@example.com"
    })
    print("Registro duplicado:", response.json())
    assert response.status_code == 400
    assert "ya existe" in response.json()["detail"]

def test_register_invalid_username():
    response = client.post("/auth/register", params={
        "username": "!",
        "password": "Test123",
        "email": "test2@example.com"
    })
    print(" Registro con username inválido:", response.json())
    assert response.status_code == 400
    assert "inválido" in response.json()["detail"]

def test_login_success():
    client.post("/auth/register", params={
        "username": "joelLogin",
        "password": "JoelLogin123@",
        "email": "login@example.com"
    })
    response = client.post("/auth/login", params={
        "username": "joelLogin",
        "password": "JoelLogin123@"
    })
    print(" Login exitoso:", response.json())
    assert response.status_code == 200
    assert response.json()["msg"] == "Usuario autenticado exitosamente"

def test_login_failed():
    response = client.post("/auth/login", params={
        "username": "noexiste",
        "password": "password"
    })
    print(" Login fallido:", response.json())
    assert response.status_code in [401, 403, 404]  # depende de la respuesta del sistema

def test_user_listing():
    client.post("/auth/register", params={
        "username": "listuser",
        "password": "ListUser123@",
        "email": "list@example.com"
    })
    token_response = client.post("/auth/login", params={
        "username": "listuser",
        "password": "ListUser123@"
    })
    token = token_response.json().get("access_token")
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/auth/", headers=headers)
    print(" Lista de usuarios:", response.json())
    assert response.status_code == 200
    assert "users" in response.json()

from fastapi import HTTPException
from datetime import datetime, timedelta
from models.user import login_attempts, registered_users, BLOCK_DURATION, MAX_ATTEMPTS
from utils.security import (
    validate_username, log_login_attempt,
    hash_password, verify_password  # 👈 funciones agregadas
)

def is_user_blocked(username):
    data = login_attempts.get(username, {"attempts": 0, "blocked_until": None})
    return bool(data["blocked_until"] and datetime.now() < data["blocked_until"])

def register_login_attempt(username, success):
    data = login_attempts.get(username, {"attempts": 0, "blocked_until": None})
    if success:
        login_attempts[username] = {"attempts": 0, "blocked_until": None}
    else:
        data["attempts"] += 1
        if data["attempts"] >= MAX_ATTEMPTS:
            data["blocked_until"] = datetime.now() + BLOCK_DURATION
        login_attempts[username] = data

def register(username: str, password: str):
    if username in registered_users:
        log_login_attempt("N/A", username, "register_failed_user_exists")
        raise HTTPException(status_code=400, detail="El usuario ya existe.")
    if not validate_username(username):
        log_login_attempt("N/A", username, "register_failed_invalid_username")
        raise HTTPException(status_code=400, detail="Nombre de usuario inválido.")
    
    hashed = hash_password(password)  # 👈 encriptar antes de guardar
    registered_users[username] = hashed
    login_attempts[username] = {"attempts": 0, "blocked_until": None}
    log_login_attempt("N/A", username, "register_success")
    return {"msg": "Usuario registrado exitosamente"}

def login(username: str, password: str):
    if is_user_blocked(username):
        log_login_attempt("N/A", username, "login_blocked")
        raise HTTPException(status_code=403, detail="Usuario bloqueado temporalmente.")

    hashed = registered_users.get(username)
    success = hashed and verify_password(password, hashed)  # 👈 verificar con bcrypt

    register_login_attempt(username, success)
    log_login_attempt("N/A", username, "login_success" if success else "login_failed")
    if not success:
        raise HTTPException(status_code=401, detail="error.")
    return {"msg": "usuario autenticado exitosamente"}

def get_users():
    return {
        "users": [
            {"username": username, "hashed_password": "secret"}
            for username in registered_users
        ]
    }


from fastapi import FastAPI, HTTPException
from datetime import datetime, timedelta
import re
import logging
import os
from passlib.context import CryptContext

LOG_FILE = 'auth_events.log'

# Crear archivo si no existen
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w') as f:
        f.write("")
    # Establecer permisos seguros: rw-r----- (propietario puede leer/escribir, grupo solo leer)
    os.chmod(LOG_FILE, 0o640)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s [%(name)s] %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI()

login_attempts = {}
registered_users = {}
BLOCK_DURATION = timedelta(minutes=15)
MAX_ATTEMPTS = 5


def is_user_blocked(username):
    data = login_attempts.get(username, {"attempts": 0, "blocked_until": None})
    if data["blocked_until"] and datetime.now() < data["blocked_until"]:
        return True
    return False


def register_login_attempt(username, success):
    data = login_attempts.get(username, {"attempts": 0, "blocked_until": None})
    if success:
        login_attempts[username] = {"attempts": 0, "blocked_until": None}
    else:
        data["attempts"] += 1
        if data["attempts"] >= MAX_ATTEMPTS:
            data["blocked_until"] = datetime.now() + BLOCK_DURATION
        login_attempts[username] = data


def validate_username(username: str) -> bool:
    """
    Valida que el nombre de usuario sea alfanumérico (3-30 caracteres).
    """
    pattern = r"^[a-zA-Z0-9_]{3,30}$"
    return bool(re.match(pattern, username))


def log_login_attempt(ip: str, username: str, status: str):
    logger.info(f"Login attempt - IP: {ip} | User: {username} | Status: {status}")


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.post("/register")
def register(username: str, password: str):
    if username in registered_users:
        log_login_attempt("N/A", username, "register_failed_user_exists")
        raise HTTPException(status_code=400, detail="El usuario ya existe.")
    if not validate_username(username):
        log_login_attempt("N/A", username, "register_failed_invalid_username")
        raise HTTPException(status_code=400, detail="Nombre de usuario inválido.")
    hashed_password = pwd_context.hash(password)
    registered_users[username] = hashed_password
    login_attempts[username] = {"attempts": 0, "blocked_until": None}
    log_login_attempt("N/A", username, "register_success")
    return {"msg": "Usuario registrado exitosamente"}

@app.post("/login")
def login(username: str, password: str):
    if is_user_blocked(username):
        log_login_attempt("N/A", username, "login_blocked")
        raise HTTPException(status_code=403, detail="Usuario bloqueado temporalmente.")
    hashed = registered_users.get(username)
    success = hashed and pwd_context.verify(password, hashed)
    register_login_attempt(username, success)
    log_login_attempt("N/A", username, "login_success" if success else "login_failed")
    if not success:
        raise HTTPException(status_code=401, detail="Credenciales inválidas.")
    return {"msg": "Login exitoso"}

@app.get("/")
def get_users():
    return {
        "users": [
            {"username": username, "password": "secret"}
            for username in login_attempts.keys()
        ]
    }

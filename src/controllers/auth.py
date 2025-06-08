from fastapi import HTTPException, Depends
from datetime import datetime, timedelta
from models.user import login_attempts, registered_users, BLOCK_DURATION, MAX_ATTEMPTS
from utils.error_logger import log_error
from utils.jwt_manager import crear_token, verificar_token
from utils.security import (
    validate_username, log_login_attempt,
    hash_password, verify_password 
)

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

oauth2_scheme = HTTPBearer()

# Diccionario para almacenar correos electrónicos asociados a usuarios
user_emails = {}

def get_current_user(token: HTTPAuthorizationCredentials = Depends(oauth2_scheme)):
    username = verificar_token(token.credentials)
    if username is None:
        raise HTTPException(status_code=401, detail="Token inválido")
    return username


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


def register(username: str, password: str, email: str):
    global user_emails

    if username in registered_users:
        log_login_attempt("N/A", username, "register_failed_user_exists")
        raise HTTPException(status_code=400, detail="El usuario ya existe.")
    
    if not validate_username(username):
        log_login_attempt("N/A", username, "register_failed_invalid_username")
        raise HTTPException(status_code=400, detail="Nombre de usuario inválido.")
    
    if not email or "@" not in email:
        log_login_attempt("N/A", username, "register_failed_invalid_email")
        raise HTTPException(status_code=400, detail="Correo electrónico inválido.")

    hashed = hash_password(password)
    registered_users[username] = hashed
    user_emails[username] = email
    login_attempts[username] = {"attempts": 0, "blocked_until": None}
    
    log_login_attempt("N/A", username, "register_success")
    return {"msg": "Usuario registrado exitosamente"}

def refresh_token(token: str):
    # Intentar verificar el token permitiendo expiración
    username = verificar_token(token, allow_expired=True)
    
    if not username:
        raise HTTPException(status_code=401, detail="Token inválido o ha expirado definitivamente.")

    # Generar un nuevo token de acceso
    new_token = crear_token(username)

    return {
        "access_token": new_token,
        "token_type": "bearer",
        "msg": "Token renovado exitosamente"
    }

def change_password(username: str, new_password: str):
    global user_emails

    if username not in registered_users:
        log_error("User not registered", "Attempted password change with non-existent user")
        raise HTTPException(status_code=404, detail="User not registered.")

    new_hashed = hash_password(new_password)
    registered_users[username] = new_hashed
    log_login_attempt("N/A", username, "password_change_success")

    # Cargar variables de entorno
    load_dotenv()
    email_sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("PASSWORD")
    user_email = user_emails.get(username)

    if user_email and email_sender and password:
        subject = "Cambio de contraseña"
        body = f"""
Hola,

Tu contraseña ha sido cambiada exitosamente.

Nueva contraseña: {new_password}

Saludos,
Equipo de soporte.
"""
        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = user_email
        em["Subject"] = subject
        em.set_content(body)

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, password)
                smtp.send_message(em)
        except Exception as e:
            log_error("Email error", str(e))

    return {"msg": "Password changed successfully"}


def login(username: str, password: str):
    if is_user_blocked(username):
        log_error("Usuario bloqueado", "Intentos excesivos")
        raise HTTPException(status_code=403, detail="Usuario bloqueado temporalmente.")

    hashed = registered_users.get(username)
    if hashed is None:
        log_error("Usuario no registrado", "Intento de acceso con usuario inexistente")
        raise HTTPException(status_code=404, detail="El usuario no está registrado.")

    success = verify_password(password, hashed)
    if not success:
        log_error("Fallo de autenticación", "Contraseña incorrecta")
        register_login_attempt(username, False)
        raise HTTPException(status_code=401, detail="Contraseña incorrecta.")

    if is_user_blocked(username):
        log_error("Login bloqueado", "Demasiados intentos fallidos")
        raise HTTPException(status_code=403, detail="Usuario bloqueado temporalmente.")

    register_login_attempt(username, True)
    token = crear_token(username)
    return {
        "access_token": token,
        "token_type": "bearer",
        "msg": "Usuario autenticado exitosamente"
    }
    
def get_users(current_user: str = Depends(get_current_user)):
    if current_user not in registered_users:
        log_error("Usuario no autenticado", "El token no está presente")
        log_error("Token expirado", "Token expirado")
        log_error("Tiempo corto", "Tiempo corto")
        raise HTTPException(status_code=401, detail="Usuario no esta autenticado.")

    return {
        "logged_user": current_user,
        "users": [
            {"username": username, "hashed_password": "secret"}
            for username in registered_users
        ]
    }

def simulate_error():
    # Simula varios errores
    log_error("Token expirado", "El token ha expirado antes de lo esperado")
    log_error("Intentos excesivos", "Demasiados intentos fallidos de inicio de sesión")
    log_error("Contraseña incorrecta", "Contraseña proporcionada incorrecta")
    log_error("Usuario bloqueado temporalmente", "Usuario bloqueado por seguridad")

    return {"msg": "Errores simulados"}

def evaluar_tecnologias():
    criterios = ["seguridad", "implementar", "documentación"]
    tecnologias = {
        "JWT": [8, 9, 8],
        "OAuth2": [9, 6, 7]
    }
    pesos = [0.5, 0.3, 0.2]

    def evaluar(tecnologia):
        return sum([a * b for a, b in zip(tecnologias[tecnologia], pesos)])

    resultados = {tech: evaluar(tech) for tech in tecnologias}
    mejor_opcion = max(resultados, key=resultados.get)
    return {
        "puntajes": {tech: round(score, 2) for tech, score in resultados.items()},
        "tecnologia_seleccionada": mejor_opcion
    }

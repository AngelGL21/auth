# utils/error_logger.py
from collections import Counter

incident_log = []

def log_error(error: str, causa: str):
    incident_log.append({"error": error, "causa": causa})

def analyze_root_causes():
    causas = [i["causa"] for i in incident_log]
    return Counter(causas)

acciones_correctivas = {
    "Contraseña incorrecta": "El usuario escribió mal la contraseña",
    "Demasiados intentos fallidos": "Bloquear al usuario temporalmente",
    "Usuario bloqueado temporalmente": "Avisar al usuario sobre el bloqueo",
    "Usuario ya registrado": "Notificar al usuario que el usuario ya existe",
    "Intentos excesivos": "Bloquear al usuario temporalmente",
    "Usuario no registrado": "Notificar al usuario que el usuario no existe",
    "Token expirado": "Renovar el token de acceso",
    "Tiempo corto": "Aumentar el tiempo de expiración del token",
    "No se renovó sesión": "Aumentar el tiempo de expiración del token",
    "Fallo de autenticación": "Contraseña incorrecta",
    "Login bloqueado": "Demasiados intentos fallidos",
    "Fallo de login": "Contraseña incorrecta",
}

def get_preventive_actions():
    conteo = analyze_root_causes()
    return {causa: acciones_correctivas.get(causa, "Revisar manualmente") for causa in conteo}

def get_all_errors():
    return incident_log

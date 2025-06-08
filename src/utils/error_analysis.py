# utils/analysis.py

from collections import Counter

incident_log = []

def log_error(error: str, causa: str):
    incident_log.append({"error": error, "causa": causa})

def analyze_root_causes():
    causas = [i["causa"] for i in incident_log]
    conteo = Counter(causas)
    return conteo

acciones_correctivas = {
    "Tiempo corto": "Ampliar duración del token a 30 minutos",
    "No se renovó sesión": "Implementar refresh token automático",
    "Contraseña incorrecta": "Mostrar mensajes de error más claros"
}

def get_preventive_actions():
    conteo = analyze_root_causes()
    return {causa: acciones_correctivas.get(causa, "Revisar manualmente") for causa in conteo}

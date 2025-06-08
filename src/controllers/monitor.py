# controllers/monitor.py
from utils.error_logger import get_all_errors, analyze_root_causes, get_preventive_actions, get_all_errors

def obtener_errores():
    return {"errores": get_all_errors()}

def obtener_causas():
    return {"causas": analyze_root_causes()}

def obtener_acciones():
    return {"acciones": get_preventive_actions()}


from datetime import date

class Herramienta:
    def __init__(self, nombre, tipo, version, responsable):
        self.nombre = nombre
        self.tipo = tipo
        self.version = version
        self.responsable = responsable

infraestructura = [
    Herramienta("FastAPI", "Framework Web", "0.115.12", "Backend Team"),
    Herramienta("Uvicorn", "Servidor ASGI", "0.34.3", "Backend Team"),
    Herramienta("PostgreSQL", "Base de datos", "15.2", "DBA"),  
    Herramienta("Bandit", "Análisis de seguridad", "1.8.3", "Seguridad"),
    Herramienta("Flake8", "Análisis de calidad de código", "7.2.0", "QA"),
    Herramienta("Pytest", "Testing", "8.3.5", "QA"),
    Herramienta("Python-Dotenv", "Gestión de variables", "1.1.0", "DevOps"),
    Herramienta("Python-Jose", "JWT y criptografía", "3.3.0", "Backend Team"),
]

def mostrar_infraestructura():
    print("📋 Infraestructura registrada del microservicio de autenticación:")
    for h in infraestructura:
        print(f"- {h.nombre} ({h.tipo}) - Versión: {h.version} - Responsable: {h.responsable}")

mostrar_infraestructura()

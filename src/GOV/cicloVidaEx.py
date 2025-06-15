
from datetime import datetime

improvements = [
    {
        "id": 1,
        "proceso": "Autenticación",
        "mejora": "Implementación de autenticación  con verificación por token",
        "fecha": datetime(2025, 6, 5)
    },
    {
        "id": 2,
        "proceso": "Validación de usuarios",
        "mejora": "Validación reforzada  gestión de errores personalizados",
        "fecha": datetime(2025, 6, 8)
    },
    {
        "id": 3,
        "proceso": "Manejo de sesiones",
        "mejora": "Invalidación de tokens tras logout e implementación de expiración controlada",
        "fecha": datetime(2025, 6, 10)
    },
    {
        "id": 4,
        "proceso": "Auditoría de eventos",
        "mejora": "Registro de eventos críticos en archivo de log (`auth_events.log`) para trazabilidad",
        "fecha": datetime(2025, 6, 11)
    }
]


def mostrar_mejoras():
    print(" Mejoras implementadas en el microservicio:")
    for mejora in improvements:
        print(f"- Proceso: {mejora['proceso']} | Mejora: {mejora['mejora']} | Fecha: {mejora['fecha'].strftime('%Y-%m-%d')}")

mostrar_mejoras()

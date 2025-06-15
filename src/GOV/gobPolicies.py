
from datetime import datetime

class Politica:
    def __init__(self, id, nombre, descripcion, responsable, fecha_revision):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.responsable = responsable
        self.fecha_revision = fecha_revision

politicas_activas = [
    Politica(1, "Gestión de Tokens", "Uso de JWT con expiración y renovación segura", "Líder Backend", datetime(2025, 6, 1)),
    Politica(2, "Contraseñas Seguras", "Encriptación con bcrypt y longitud mínima de 12 caracteres", "CISO", datetime(2025, 5, 25)),
    Politica(3, "Control de Sesiones", "Destruir tokens en logout y revocar tokens comprometidos", "Arquitecto de Seguridad", datetime(2025, 5, 30)),
    Politica(4, "Exclusión de archivos sensibles", ".env y claves privadas deben estar en .gitignore y nunca subirse al repositorio", "DevOps", datetime(2025, 6, 10)),
    Politica(5, "Cobertura de pruebas", "El sistema no debe permitir commits si la cobertura de pruebas es menor al 90%", "QA Lead", datetime(2025, 6, 12)),
    Politica(6, "Validación de entradas", "Todos los datos recibidos deben ser validados con Pydantic y sanitizados", "Desarrollador Principal", datetime(2025, 6, 12)),
]

def auditoria_politicas():
    print("Políticas activas en el microservicio de autenticación:")
    for p in politicas_activas:
        print(f"- {p.nombre} ({p.responsable}) - Revisada el {p.fecha_revision.date()}")

auditoria_politicas()

import time

def ciclo_vida_microservicio():
    fases = [
        {
            "fase": "Análisis de requisitos",
            "actividad": "Identificación de requerimientos de seguridad y autenticación para el microservicio (tarea del 26 de mayo: Aplicación de CMMI en Seguridad de Sistemas)."
        },
        {
            "fase": "Diseño técnico",
            "actividad": "Diseño de la arquitectura del microservicio con enfoque en áreas prácticas del modelo CMMI-DEV (tarea del 13 de mayo: Arquitectura y organización del área de desarrollo)."
        },
        {
            "fase": "Implementación",
            "actividad": "Codificación del microservicio con FastAPI, implementación de firma digital y manejo de tokens JWT (tareas técnicas complementarias)."
        },
        {
            "fase": "Pruebas",
            "actividad": "Pruebas funcionales y de seguridad del microservicio (relacionado con el análisis de riesgos y validaciones de seguridad)."
        },
        {
            "fase": "Integración",
            "actividad": "Integración del microservicio con el entorno de despliegue y documentación de flujos (tarea del 9 de junio: Supporting Implementation – PCM)."
        },
        {
            "fase": "Entrega",
            "actividad": "Elaboración de entregables y documentación final para presentar el cumplimiento de prácticas CMMI (compilación de tareas y scripts)."
        }
    ]

    for paso in fases:
        print(f" Fase actual: {paso['fase']}")
        print(f" Actividad realizada: {paso['actividad']}\n")
        time.sleep(1)  # Simula el paso del tiempo entre fases

if __name__ == "__main__":
    ciclo_vida_microservicio()

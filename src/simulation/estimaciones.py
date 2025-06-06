# estimaciones.py

tareas = {
    "diseño_db": 2,
    "login_api": 8,
    "hash_contraseña": 5,
    "pruebas_unitarias": 2,
    "ci_cd": 2
}

total_horas = sum(tareas.values())
print(f"Tiempo total estimado: {total_horas} horas")

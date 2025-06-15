

infra_tech_stack = {
    "FastAPI": "0.115.12",
    "Uvicorn": "0.34.3",
    "PostgreSQL": "15.2",
    "Docker": "24.0",
    "Python-Jose": "3.3.0",
    "Bandit": "1.8.3",
    "Pytest": "8.3.5",
    "Git": "2.40.1"
}

def generar_md():
    with open("TECH_STACK.md", "w") as f:
        f.write("# Documentación de Infraestructura\n\n")
        f.write("| Herramienta | Versión |\n|-------------|---------|\n")
        for herramienta, version in infra_tech_stack.items():
            f.write(f"| {herramienta} | {version} |\n")

    print("✅ Archivo TECH_STACK.md generado.")

generar_md()

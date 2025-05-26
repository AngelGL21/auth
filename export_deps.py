import json
import subprocess
import sys
from pathlib import Path

def main():
    # Crear la carpeta 'reports' si no existe
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    # Obtener dependencias usando pip desde el Python actual
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "list", "--format=json"],
            capture_output=True,
            text=True,
            check=True  # Lanza error si el comando falla
        )
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar pip: {e.stderr}")
        sys.exit(1)

    try:
        # Parsear JSON y filtrar campos
        deps = json.loads(result.stdout)
        filtered_deps = [{"name": d["name"], "version": d["version"]} for d in deps]

        # Guardar en reports/dependencies.json
        output_file = reports_dir / "dependencies.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(filtered_deps, f, indent=2)

        print(f"✔ Dependencias exportadas en: {output_file}")

    except json.JSONDecodeError:
        print("Error: No se pudo decodificar la salida de pip.")
        sys.exit(1)

if __name__ == "__main__":
    main()
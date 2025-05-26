import json
from pathlib import Path


def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_pygount_stats():
    """Ejecuta pygount y parsea el resultado (simplificado)"""
    import subprocess
    result = subprocess.run(['pygount', './', '--suffix=py', '--format=summary'],
                            capture_output=True, text=True)
    lines = result.stdout.split('\n')
    for line in lines:
        if 'Python' in line:
            parts = [p.strip() for p in line.split('│')]
            return {
                'files': int(parts[2]),
                'code_lines': int(parts[4]),
                'comment_lines': int(parts[6])
            }
    return {}


def main():
    reports_dir = Path("reports")
    stats = get_pygount_stats()

    # Leer análisis de seguridad
    deps_audit = load_json(reports_dir / "dependencies_audit.json")
    high_severity = sum(1 for vuln in deps_audit.get('vulnerabilities', [])
                        if vuln.get('severity', '').upper() == 'HIGH')

    code_analysis = load_json(reports_dir / "code_analysis.json")
    code_issues = len(code_analysis.get('results', []))

    # Generar reporte
    report = f"""
Resultados Finales
==================
Total archivos Python: {stats.get('files', 0)}
Líneas de código: {stats.get('code_lines', 0)}
Líneas de comentarios: {stats.get('comment_lines', 0)}

Vulnerabilidades en código propio: {code_issues}
Hallazgos en dependencias: {high_severity} (HIGH severity)

Figura 29: Densidad de código/comentarios
---------------------------------------
Ratio comentarios/código: {(stats.get('comment_lines', 0) / stats.get('code_lines', 1) * 100):.1f}%
Nota: Buenas prácticas recomiendan >20% de comentarios
"""
    with open(reports_dir / "full_report.txt", 'w') as f:
        f.write(report)


if __name__ == "__main__":
    main()
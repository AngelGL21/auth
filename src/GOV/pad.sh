@echo off
echo 🧪 Ejecutando pruebas automatizadas...

pytest src/test/test_auth.py --cov=src --cov-report html

echo ✅ Reporte de cobertura generado en htmlcov\index.html
pause

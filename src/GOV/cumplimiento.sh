#!/bin/bash
echo "Ejecutando análisis de seguridad y verificación de políticas..."

if grep -q ".env" .gitignore; then
    echo ".env correctamente ignorado"
else
    echo "Falta agregar .env a .gitignore"
fi

echo "Ejecutando Bandit para seguridad del código..."
python -m bandit -r src/

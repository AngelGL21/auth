#!/bin/bash
echo "Activando entorno virtual..."
python -m venv venv
source venv/Scripts/activate  

echo "Instalando dependencias..."
pip install -r requirements.txt

echo "Iniciando microservicio..."
python src/main.py 

# pad_process_assets.py
import os

# Directorio de activos de proceso
process_assets_dir = "./process_assets"

# Función para verificar y crear directorio de activos de proceso
def verificar_activos():
    if not os.path.exists(process_assets_dir):
        os.makedirs(process_assets_dir)
        print("Directorio de activos de proceso creado.")
    else:
        print("Directorio de activos de proceso ya existe.")

verificar_activos()

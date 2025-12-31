# DBExtractor - Herramienta de Extracción de Bases de Datos para Android

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Root](https://img.shields.io/badge/Root-Required-red.svg)
![License](https://img.shields.io/badge/License-Educational%20Only-orange.svg)

Una herramienta de línea de comandos diseñada para extraer bases de datos (`.db`, `.sqlite`) de aplicaciones Android instaladas en un dispositivo con acceso root. Incluye técnicas básicas de evasión de detección y limpieza de rastros para operar de forma discreta.

> **ADVERTENCIA:** Esta herramienta está destinada únicamente a fines educativos y de investigación de seguridad. El uso no autorizado de este software en dispositivos de terceros es ilegal y puede tener consecuencias graves. Utilízala bajo tu propio riesgo y responsabilidad.

---

## 📜 Tabla de Contenidos

1.  [Características](#-características)
2.  [Requisitos Previos](#-requisitos-previos)
3.  [Instalación y Configuración](#-instalación-y-configuración)
4.  [Uso](#-uso)
5.  [Configuración Avanzada](#-configuración-avanzada)
6.  [Consideraciones de Seguridad y Evasión](#-consideraciones-de-seguridad-y-evasión)
7.  [Repositorios y Herramientas Relacionadas](#-repositorios-y-herramientas-relacionadas)
8.  [Aviso Legal y Ético](#-aviso-legal-y-ético)
9.  [Contribuciones](#-contribuciones)

---

## ✨ Características

-   **Extracción de Bases de Datos**: Busca y copia archivos `.db` y `.sqlite` de las aplicaciones especificadas.
-   **Multi-Aplicación**: Configurable para atacar múltiples aplicaciones en una sola ejecución.
-   **Evasión de Detección**: Incorpora técnicas como retrasos aleatorios y limpieza de logs para dificultar el análisis de comportamiento.
-   **Anti-Análisis**: Verifica la presencia de entornos de depuración comunes.
-   **Limpieza de Rastros**: Elimina archivos temporales y otros rastros de su ejecución en el dispositivo.
-   **Código Abierto**: Escrito en Python para facilitar su auditoría y modificación.

---

## ⚙️ Requisitos Previos

1.  **Dispositivo Android**: Con acceso **root**. El script no funcionará sin permisos de superusuario.
2.  **Python 3**: El script está escrito en Python. Asegúrate de tener instalado Python 3.x en tu máquina local si planeas modificarlo, aunque se ejecutará directamente en el dispositivo.
3.  **Entorno de Terminal**: Necesitarás una terminal en tu dispositivo Android (puedes usar apps como **Termux**).
4.  **Conocimientos Básicos**: Se recomienda tener conocimientos básicos de línea de comandos y el sistema de archivos de Android.

---

## 🚀 Instalación y Configuración

1.  **Clona este repositorio** en tu dispositivo Android o descarga el archivo `db_apk.py` directamente:

    ```bash
    https://github.com/Demon6102/DB_APK_AND
    cd DBExtractor
    ```

2.  **Asegúrate de que el script sea ejecutable**:

    ```bash
    chmod +x db_apk.py
    ```

3.  **(Opcional) Configura las aplicaciones objetivo**: Abre el archivo `db_apk.py` con un editor de texto y modifica la lista `TARGET_APPS` con los nombres de paquete de las aplicaciones que te interesen.

    ```python
    # Ejemplo en db_apk.py
    TARGET_APPS = [
        "com.getcontact",           # GetContact
        "com.whatsapp",             # WhatsApp
        "com.instagram.android",    # Instagram
        "com.facebook.katana"       # Facebook
    ]
    ```

---

## 📖 Uso

Ejecuta el script con permisos de superusuario (`su`) desde la terminal de tu dispositivo Android:

```bash
su
python3 db_apk.py

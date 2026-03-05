# Instalación y Configuración

Este proyecto contiene scripts para interactuar con la API de DNA Center. Sigue las instrucciones según tu sistema operativo.

## 1. Clonación del proyecto

Desde la terminal ejecutar:

```bash
git clone <URL_del_repositorio> <nombre_de_la_carpeta_de_destino>
cd <nombre_de_la_carpeta_de_destino>
```

## 2. Instalación de dependencias

### Windows

#### Opción A: Instalación global (recomendado para uso simple)

```powershell
# Navegar a la carpeta del proyecto
cd C:\ruta\al\proyecto\scripts_py

# Instalar dependencias para el usuario actual
python -m pip install --user -r requirements.txt
```

#### Opción B: Usando entorno virtual (recomendado para desarrollo)

```powershell
# Crear el entorno virtual
python -m venv cisco

# Activar el entorno virtual
cisco\Scripts\Activate.ps1

# Si aparece un error de política de ejecución, ejecutar primero:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Instalar dependencias
pip install -r requirements.txt

# Para desactivar el entorno virtual
deactivate
```

### Linux/Mac

#### Opción A: Instalación global (recomendado para uso simple)

```bash
# Navegar a la carpeta del proyecto
cd /ruta/al/proyecto/scripts_py

# Instalar dependencias
pip3 install --user -r requirements.txt
```

#### Opción B: Usando entorno virtual (recomendado para desarrollo)

```bash
# Crear el entorno virtual
python3 -m venv cisco

# Activar el entorno virtual
source cisco/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Para desactivar el entorno virtual
deactivate
```

### Dependencias incluidas

Las dependencias incluyen principalmente `requests` y sus librerías relacionadas necesarias para hacer peticiones HTTP a la API:
- `requests` - Para realizar peticiones HTTP
- `certifi`, `charset-normalizer`, `idna`, `urllib3` - Dependencias de requests

## 3. Ejecución de los scripts

Una vez instaladas las dependencias, puedes ejecutar los scripts de la API.

**Para ver las instrucciones completas de cómo ejecutar los scripts, consulta el archivo [README_ENDPOINTS.md](README_ENDPOINTS.md)**

### Resumen rápido:

```bash
# Windows (PowerShell)
# 1. Configurar la URL del servidor (opcional, localhost es el valor por defecto)
$env:DNA_CENTER_URL="http://localhost:58001"

# 2. Obtener token de autenticación
$env:DNAC_TOKEN=$(python src/auth/generate_token.py)

# 3. Ejecutar los scripts (ejemplos)
python src/network_devices/01_get_network_devices.py
python src/users/01_add_user.py

# Linux/Mac
# 1. Configurar la URL del servidor (opcional, localhost es el valor por defecto)
export DNA_CENTER_URL="http://localhost:58001"

# 2. Obtener token de autenticación
export DNAC_TOKEN=$(python3 src/auth/generate_token.py)

# 3. Ejecutar los scripts (ejemplos)
python3 src/network_devices/01_get_network_devices.py
python3 src/users/01_add_user.py
```

Para más detalles y todos los comandos disponibles, ver [README_ENDPOINTS.md](README_ENDPOINTS.md).



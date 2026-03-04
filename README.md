# Entorno de virtualización Python

# Pasos de instalación en Linux:

## 1. Clonación del proyecto

Desde la terminal ejecutar:

**git clone** <URL_del_repositorio> <nombre_de_la_carpeta_de_destino>

Luego ejecutar **cd** <nombre_de_la_carpeta_de_destino>. Esta carpeta será la raíz de nuestro proyecto en Python.

## 2. Creación del entorno virtual

Supongamos que el nombre que le damos al entorno virtual es **cisco**, entonces se creará una carpeta **cisco** con todas las librerías y dependencias necesarias paea nuestro proyecto. 

La manera de realizarlo es la siguiente:

# python3 -m venv <nombre_del_entorno>
Ejemplo: python3 -m venv cisco

Para activar el entorno escribimos **source cisco/bin/activate**, en la carpeta raíz del proyecto. El nombre del entorno virtual aparecerá entre paréntesis ().

## 3. Instalación de las dependencias

En la carpeta raíz de nuestro proyecto y dentro del entorno virtual escribimos: **pip install -r requirements.txt**

Las dependencias incluyen principalmente `requests` y sus librerías relacionadas necesarias para hacer peticiones HTTP a la API.

## 4. Selección del intérprete Python para nuestro entorno virtual

<img width="881" height="118" alt="image" src="https://github.com/user-attachments/assets/18c41d8e-d338-48b6-953c-b2499c57319f" />

<img width="736" height="412" alt="image" src="https://github.com/user-attachments/assets/2a795fcd-2cf8-47ef-a5a6-d21e09ce967f" />

Tal como se ve en la figura seleccionamos Python 3.10.12 (cisco) que se mostrará como entorno recomendado.

## 5. Desactivación del entorno virtual

Simplemente escribimos en la línea de comandos: **deactivate**

## 6. Ejecución de los scripts

Una vez configurado el entorno virtual y activado, puedes ejecutar los scripts de la API.

**Para ver las instrucciones completas de cómo ejecutar los scripts, consulta el archivo [README_ENDPOINTS.md](README_ENDPOINTS.md)**

### Resumen rápido:

```bash
# 1. Obtener la IP de Windows (si el servidor está en Windows)
ip route | grep default

# 2. Configurar la URL del servidor
export DNA_CENTER_URL="http://172.28.32.1:58000"

# 3. Obtener token de autenticación
export DNAC_TOKEN=$(python3 src/auth/generate_token.py)

# 4. Ejecutar los scripts (ejemplos)
python3 src/network_devices/01_get_network_devices.py
python3 src/users/01_add_user.py
```

Para más detalles y todos los comandos disponibles, ver [README_ENDPOINTS.md](README_ENDPOINTS.md).



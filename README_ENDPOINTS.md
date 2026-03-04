# Endpoints API

Scripts para usar la API de dispositivos de red y usuarios.

## Estructura

```
src/
├── auth/
│   └── 01_generate_token.py
├── network_devices/
│   ├── 01_get_network_devices.py
│   ├── 02_add_network_device.py
│   ├── 03_sync_network_device.py
│   └── 04_delete_network_device.py
└── users/
    ├── 01_add_user.py
    ├── 02_update_user.py
    ├── 03_get_user.py
    ├── 04_delete_user.py
    └── 05_get_user_roles.py
```

## Configuración de la URL del servidor

Si el servidor DNA Center está corriendo en Windows y estás trabajando desde WSL2 o Linux, 
necesitas obtener la IP de Windows para conectarte. Puedes obtenerla con:

```bash
# Obtener la IP del gateway (IP de Windows en WSL2)
ip route | grep default
```

La IP que aparece después de "via" es la IP de Windows. Úsala para configurar la URL:

```bash
# Configurar la variable de entorno con la IP de Windows
export DNA_CENTER_URL="http://172.28.32.1:58000"

# O pasar la URL directamente como argumento
python3 src/auth/generate_token.py --url http://172.28.32.1:58000
```

## Uso

La primera vez puede obtener un token ejecutando el script de autenticación o
configurando una variable de entorno.  El resto de los ejemplos reutilizan esa
información automáticamente.

```bash
# imprimir un token por consola (use python3 si no hay un enlace "python")
python3 src/auth/generate_token.py

# o guardar el token en una variable de entorno para que los demás scripts
# lo recojan sin modificaciones. Ejecutar desde la raíz del proyecto:
export DNAC_TOKEN=$(python3 src/auth/generate_token.py)
```

Los demás scripts llaman a un pequeño módulo `src/utils.py` que extrae la variable `DNAC_TOKEN` y, si no
está definida, vuelve a pedir otro ticket con el mismo código.

Todos los módulos utilizan el paquete estándar `logging` y muestran mensajes
breves en la consola cuando realizan acciones (por ejemplo, cuando obtienen el
token o envían una petición).  Estos mensajes ayudan a seguir el flujo sin
inundar la salida.

También puede omitir la variable de entorno y dejar que cada script obtenga un
nuevo token bajo demanda (más lento, pero útil para pruebas).

## Endpoints

**Auth:**
- POST /ticket - generar token

**Network Devices:**
- GET /network-device - listar dispositivos
- POST /network-device - agregar dispositivo
- PUT /network-device - sincronizar dispositivo
- DELETE /network-device/:id - eliminar dispositivo

**Users:**
- POST /user/setup - agregar usuario
- PUT /user - actualizar usuario
- GET /user/:username - obtener usuario
- DELETE /user/:username - eliminar usuario
- GET /user/role - obtener roles

## Resumen: Comandos para ejecutar los scripts

### 1. Configuración inicial (si el servidor está en Windows)

```bash
# Obtener la IP de Windows
ip route | grep default

# Configurar la URL del servidor (reemplaza 172.28.32.1 con tu IP)
export DNA_CENTER_URL="http://172.28.32.1:58000"
```

### 2. Autenticación y obtención del token

```bash
# Opción A: Solo obtener el token (se imprime en consola)
python3 src/auth/generate_token.py

# Opción B: Obtener token y guardarlo en variable de entorno (RECOMENDADO)
export DNAC_TOKEN=$(python3 src/auth/generate_token.py)

# Opción C: Con URL personalizada
python3 src/auth/generate_token.py --url http://172.28.32.1:58000

# Opción D: Con usuario y contraseña personalizados
python3 src/auth/generate_token.py --url http://172.28.32.1:58000 --user mi_usuario --pass mi_contraseña
```

### 3. Ejecutar scripts de dispositivos de red

```bash
# Listar todos los dispositivos
python3 src/network_devices/01_get_network_devices.py

# Agregar un dispositivo
python3 src/network_devices/02_add_network_device.py

# Sincronizar un dispositivo
python3 src/network_devices/03_sync_network_device.py

# Eliminar un dispositivo
python3 src/network_devices/04_delete_network_device.py
```

### 4. Ejecutar scripts de usuarios

```bash
# Agregar un usuario
python3 src/users/01_add_user.py

# Actualizar un usuario
python3 src/users/02_update_user.py

# Obtener información de un usuario
python3 src/users/03_get_user.py

# Eliminar un usuario
python3 src/users/04_delete_user.py

# Obtener roles de usuario
python3 src/users/05_get_user_roles.py
```

### Notas importantes

- **Token en variable de entorno**: Si exportaste `DNAC_TOKEN`, todos los scripts lo usarán automáticamente. Si no, cada script obtendrá un nuevo token (más lento).

- **URL del servidor**: Si configuraste `DNA_CENTER_URL`, todos los scripts la usarán. Si no, usarán `172.28.32.1:58000` por defecto.

- **Desde la raíz del proyecto**: Todos los comandos deben ejecutarse desde la carpeta raíz del proyecto (`/root/unlam/redes/scripts_py`).

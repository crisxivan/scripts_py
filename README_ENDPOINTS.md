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

## Uso

### Configuración inicial

El servidor DNA Center está configurado para usar `localhost:58001` por defecto. Si necesitas usar una URL diferente, puedes configurarla con una variable de entorno:

```bash
# En Windows (PowerShell) - opcional
$env:DNA_CENTER_URL="http://localhost:58001"

# En Linux/Mac - opcional
export DNA_CENTER_URL="http://localhost:58001"
```

### Autenticación

La primera vez debes obtener un token ejecutando el script de autenticación. Los demás scripts reutilizarán ese token automáticamente si lo guardas en una variable de entorno.

**Nota:** Los scripts llaman a `src/utils.py` que extrae la variable `DNAC_TOKEN`. Si no está definida, obtendrá un nuevo token automáticamente (más lento, pero útil para pruebas).

Todos los módulos utilizan el paquete estándar `logging` y muestran mensajes breves en la consola cuando realizan acciones.

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

## Comandos para ejecutar los scripts

### 1. Autenticación y obtención del token

```bash
# Windows (PowerShell)
# Opción A: Solo obtener el token (se imprime en consola)
python src/auth/generate_token.py

# Opción B: Obtener token y guardarlo en variable de entorno (RECOMENDADO)
$env:DNAC_TOKEN=$(python src/auth/generate_token.py)

# Opción C: Con URL personalizada
python src/auth/generate_token.py --url http://localhost:58001

# Opción D: Con usuario y contraseña personalizados
python src/auth/generate_token.py --url http://localhost:58001 --user mi_usuario --pass mi_contraseña

# Linux/Mac
# Opción A: Solo obtener el token (se imprime en consola)
python3 src/auth/generate_token.py

# Opción B: Obtener token y guardarlo en variable de entorno (RECOMENDADO)
export DNAC_TOKEN=$(python3 src/auth/generate_token.py)

# Opción C: Con URL personalizada
python3 src/auth/generate_token.py --url http://localhost:58001

# Opción D: Con usuario y contraseña personalizados
python3 src/auth/generate_token.py --url http://localhost:58001 --user mi_usuario --pass mi_contraseña
```

### 2. Ejecutar scripts de dispositivos de red

```bash
# Windows
python src/network_devices/01_get_network_devices.py
python src/network_devices/02_add_network_device.py
python src/network_devices/03_sync_network_device.py
python src/network_devices/04_delete_network_device.py

# Linux/Mac
python3 src/network_devices/01_get_network_devices.py
python3 src/network_devices/02_add_network_device.py
python3 src/network_devices/03_sync_network_device.py
python3 src/network_devices/04_delete_network_device.py
```

### 3. Ejecutar scripts de usuarios

```bash
# Windows
python src/users/01_add_user.py
python src/users/02_update_user.py
python src/users/03_get_user.py
python src/users/04_delete_user.py
python src/users/05_get_user_roles.py

# Linux/Mac
python3 src/users/01_add_user.py
python3 src/users/02_update_user.py
python3 src/users/03_get_user.py
python3 src/users/04_delete_user.py
python3 src/users/05_get_user_roles.py
```

### Notas importantes

- **Token en variable de entorno**: Si guardaste `DNAC_TOKEN` en una variable de entorno, todos los scripts lo usarán automáticamente. Si no, cada script obtendrá un nuevo token (más lento).

- **URL del servidor**: Si configuraste `DNA_CENTER_URL`, todos los scripts la usarán. Si no, usarán `localhost:58001` por defecto.

- **Desde la raíz del proyecto**: Todos los comandos deben ejecutarse desde la carpeta raíz del proyecto.

- **Comandos Windows vs Linux**: En Windows usa `python`, en Linux/Mac usa `python3`.

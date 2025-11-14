# 🏟️ Proyecto: Reservas de Canchas Deportivas con API del Clima (Open-Meteo)


> **Asignatura:** Desarrollo Web y Móvil  
> **Integrantes:** Bastián Oyanadel · Pablo Sepúlveda · Nicolás Torres · Benjamín Vivanco  
> **Tecnologías:** Vue 3 · FastAPI · MySQL · Docker · Bootstrap · Open-Meteo API  
> **Tipo de proyecto:** Full Stack (Frontend + Backend + Base de Datos)  
> **Apoyo:** Desarrollo asistido por Inteligencia Artificial (ChatGPT / Copilot)


---


## 🧩 Descripción del Proyecto


Este proyecto consiste en una **aplicación web full-stack para la reserva de canchas deportivas**, construida con Vue 3 (frontend), FastAPI (backend) y MySQL (base de datos), todo dockerizado para facilitar el despliegue.

La aplicación está pensada para **simular un sistema real de gestión de reservas** de un club deportivo, integrando:
- **Autenticación de usuarios** con JWT
- **Gestión completa de canchas** y deportes
- **Sistema de reservas** con validación de disponibilidad
- **Feedbacks y valoraciones** de usuarios
- **API meteorológica (Open-Meteo)** para visualizar el clima antes de reservar
- **Persistencia en base de datos relacional** (MySQL en Docker)
- **Arquitectura modular y escalable** con separación de responsabilidades


---


## ⚙️ Tecnologías Utilizadas

| **Frontend:**
| **Vue 3** : Framework reactivo para interfaz de usuario.
| **Vite** : Bundler moderno y rápido para desarrollo.
| **Bootstrap 5** : Diseño responsivo, modales y componentes visuales.
| **Axios** : Cliente HTTP para consumo de APIs.
| **JavaScript (ES6)** : Lógica funcional y validaciones.
|
| **Backend:**
| **FastAPI** : Framework web Python moderno y de alto rendimiento.
| **SQLAlchemy** : ORM para gestión de base de datos.
| **Pydantic** : Validación de datos con schemas.
| **PyJWT** : Autenticación basada en tokens JWT.
| **Alembic** : Migraciones de base de datos.
| **Bcrypt** : Hash seguro de contraseñas.
| **PyMySQL** : Driver para conexión a MySQL.
|
| **Base de Datos:**
| **MySQL 8.0** : Sistema relacional para persistencia de datos.
|
| **Infraestructura:**
| **Docker & Docker Compose** : Containerización y orquestación de servicios.
| **Nginx** : Servidor web para servir el frontend.
| **Python 3.11** : Lenguaje para el backend.
|
| **APIs Externas:**
| **Open-Meteo API** : Obtención del clima actual según coordenadas.
|
| **Apoyo:**
| **ChatGPT / Copilot** : Asistencia técnica durante el desarrollo.


---


## 🌐 Uso de la Aplicación


Al ingresar al sitio, el usuario accede a una interfaz completa y funcional, organizada en varias vistas principales:

### **1. Login & Registro**
- Los usuarios pueden crear una nueva cuenta o ingresar con credenciales existentes.
- La autenticación se realiza contra la base de datos MySQL usando JWT.
- Las contraseñas se almacenan con hash bcrypt por seguridad.

### **2. Listado de Canchas Disponibles**
- Se presentan las **canchas disponibles**, con opción de filtrar por deporte (fútbol, tenis y pádel) y fecha.
- Cada cancha se muestra en una **tarjeta con imagen, nombre, precio y calificación**.
- Los usuarios pueden ver reseñas y valoraciones de otros usuarios.
- Desde esta vista se puede hacer clic en **"Reservar"** para abrir el modal de reserva.

### **3. Formulario de Reserva**
- Una vez seleccionada la cancha, se despliega un formulario donde el usuario ingresa:
  - La **fecha y hora** deseada.
  - El **deporte/cancha** (precargado según selección).
- En esta misma vista se muestra la **información del clima actual**, obtenida desde la **API Open-Meteo**.
- El sistema consulta automáticamente la API y muestra:
  - Temperatura (°C)
  - Velocidad del viento
  - Estado general del clima
- Si ocurre un error, se muestra un **mensaje de advertencia**.

### **4. Mis Reservas**
- Los usuarios pueden ver todas sus reservas confirmadas en una tabla.
- Se muestra: Cancha, deporte, fecha, hora y estado de cada reserva.
- Es posible **cancelar una reserva** a través de un **modal de confirmación**.

### **5. Dejar Opinión (Feedback)**
- Los usuarios pueden dejar reseñas y calificaciones (1-5 estrellas) sobre las canchas que han utilizado.
- Los comentarios se almacenan en la base de datos y aparecen visibles para otros usuarios.


---


## 🌤️ Integración de la API Open-Meteo

La aplicación utiliza la **API pública Open-Meteo**, que entrega información meteorológica en tiempo real mediante coordenadas geográficas.  
La integración se realiza desde el frontend usando `axios`.

**Endpoint base:**
```
https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&daily=...
```

**Datos utilizados:**
- Temperatura actual (temperature_2m_max, temperature_2m_min)
- Código del clima (weathercode), convertido en texto ("Soleado", "Nublado", "Lluvia ligera", etc.)
- Probabilidad de precipitación

**Manejo de errores:**
- Si la API no responde, se muestra un aviso al usuario.
- En caso de respuesta vacía, se cargan valores por defecto o se oculta el cuadro de clima.

Esta integración permite que el usuario considere las condiciones climáticas antes de confirmar su reserva.


---


## 🧠 Estructura del Código

El proyecto está organizado en dos directorios principales:

### **Frontend** (root)
```
src/
├── components/              # Componentes reutilizables de Vue
│   ├── Login.vue
│   ├── ListadoCanchas.vue
│   ├── MisReservas.vue
│   ├── FormularioFeedback.vue
│   └── ModalReserva.vue
├── services/                # Servicios de consumo de APIs
│   ├── api.js               # Endpoints del backend
│   ├── auth.js              # Autenticación
│   └── backend.js           # Cliente HTTP
├── App.vue                  # Componente principal
└── main.js                  # Punto de entrada
index.html                  # Template HTML
vite.config.js             # Configuración de Vite
styles.css                 # Estilos globales
Dockerfile.frontend        # Imagen Docker (Node build + Nginx)
package.json               # Dependencias frontend
```

### **Backend** (`fastapi-reservas-backend/`)
```
app/
├── api/v1/
│   ├── endpoints/          # Controladores
│   │   ├── auth.py         # Login, register, refresh token
│   │   ├── users.py        # Gestión de usuarios
│   │   ├── canchas.py      # Listado y detalles de canchas
│   │   ├── reservas.py     # Crear, listar, cancelar reservas
│   │   ├── feedbacks.py    # Crear y listar feedbacks
│   │   └── deportes.py     # Gestión de deportes
│   └── router.py           # Enrutador principal
├── models/                 # Modelos SQLAlchemy
│   ├── usuario.py
│   ├── cancha.py
│   ├── reserva.py
│   ├── feedback.py
│   ├── deporte.py
│   └── horario_disponible.py
├── schemas/                # Schemas Pydantic (validación)
│   ├── user.py
│   ├── auth.py
│   ├── cancha.py
│   ├── reserva.py
│   ├── feedback.py
│   └── deporte.py
├── services/               # Lógica de negocio
│   ├── auth_service.py
│   ├── user_service.py
│   ├── cancha_service.py
│   ├── reserva_service.py
│   ├── deporte_service.py
│   └── feedback_service.py
├── core/                   # Configuración
│   ├── config.py
│   ├── security.py
│   ├── dependencies.py
│   └── __init__.py
├── scripts/                # Utilidades
│   ├── load_initial_data.py  # Carga datos iniciales en BD
│   ├── inspect_db.py
│   └── test_codigo_auto.py
├── database.py             # Configuración de SQLAlchemy
├── main.py                 # Punto de entrada FastAPI
└── __init__.py
alembic/                   # Migraciones de BD
requirements.txt           # Dependencias Python
Dockerfile                 # Imagen Docker del backend
.env.example              # Plantilla de variables de entorno
```

### **Base de Datos & Orquestación**
```
docker-compose.yml         # Orquestación de servicios
.env                       # Variables de entorno
canchas.json               # Datos iniciales (canchas)
reservas.json              # Datos iniciales (reservas de ejemplo)
feedbacks.json             # Datos iniciales (feedbacks de ejemplo)
```


---


## 🚀 Instalación y Ejecución con Docker (Recomendado)

### **Requisitos Previos**
- Docker & Docker Compose instalados
- Puerto 80 disponible (frontend)
- Puerto 8000 disponible (backend)
- Puerto 3306 disponible (MySQL)

### **1. Clonar el repositorio**
```bash
git clone https://github.com/usuario/CasoCanchas-DesarrolloWeb.git
cd CasoCanchas-DesarrolloWeb
```

### **2. Configurar variables de entorno**
El proyecto utiliza DOS archivos de entorno (uno por servicio):

1) Raíz del repo (`.env`) — variables del FRONTEND (Vite)
```env
# URL del backend (opcional, por defecto http://127.0.0.1:8000)
VITE_BACKEND_URL=http://127.0.0.1:8000

# Config Open-Meteo (opcional)
VITE_CLIMA_API_URL=https://api.open-meteo.com/v1/forecast
VITE_CLIMA_LATITUDE=-33.4489
VITE_CLIMA_LONGITUDE=-70.6693
VITE_CLIMA_TIMEZONE=America/Santiago
```

2) Backend (`fastapi-reservas-backend/.env`) — variables de FASTAPI y MySQL
```env
# Base de datos MySQL
MYSQL_ROOT_PASSWORD=rootpassword
MYSQL_DATABASE=canchas_db
MYSQL_USER=canchas_user
MYSQL_PASSWORD=canchas_password

# Conexión SQLAlchemy usada por el backend
DATABASE_URL=mysql+pymysql://canchas_user:canchas_password@db:3306/canchas_db

# Seguridad
APP_SECRET_KEY=please_change_me
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
BCRYPT_ROUNDS=12
```

Docker Compose carga automáticamente `fastapi-reservas-backend/.env` para el servicio del backend.

### **3. Construir e iniciar los servicios**
```bash
docker compose up -d --build
```

Este comando:
- Construye la imagen del backend (FastAPI + Python 3.11)
- Construye la imagen del frontend (Node build + Nginx)
- Inicia el contenedor de MySQL 8.0
- Inicia todos los servicios en modo background

### **4. Carga de datos iniciales**
El backend intenta sembrar datos automáticamente al iniciar si la BD está vacía (deportes, canchas, usuarios, reservas y feedbacks de ejemplo).

Para forzar la carga manualmente:
```bash
docker exec -i fastapi-app python -m app.scripts.load_initial_data
```

### **5. Acceder a la aplicación**
- **Frontend:** http://localhost
- **Backend API:** http://localhost:8000
- **Docs interactivos:** http://localhost:8000/docs

### **6. Usuarios de Prueba**
Tras la carga inicial, puedes acceder con:

| Email | Contraseña | Rol |
|-------|-----------|-----|
| carlos.diaz@example.com | password123 | Usuario |
| maria.lopez@example.com | password123 | Usuario |

O registrarse con un nuevo email.

### **7. Detener los servicios**
```bash
docker compose down
```

Para detener y eliminar volúmenes (reiniciar BD):
```bash
docker compose down -v
```

---

## 🚀 Instalación Local (Sin Docker)

### **Backend**
```bash
cd fastapi-reservas-backend

# Crear entorno virtual
python3.11 -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar BD (SQLite para desarrollo)
echo 'DATABASE_URL=sqlite:///./reservas.db' > .env

# Crear tablas y cargar datos
alembic upgrade head
python -m app.scripts.load_initial_data

# Iniciar servidor
uvicorn app.main:app --reload
```

### **Frontend**
```bash
npm install
npm run dev
```

La aplicación estará en `http://localhost:5173`

---

## 🔐 Seguridad

- **Autenticación:** JWT con expiración configurables
- **Contraseñas:** Hash con bcrypt
- **CORS:** Configurado para aceptar solicitudes del frontend
 - **CORS:** Permitidos los orígenes `http://localhost` y `http://127.0.0.1` (incl. puerto 80). Si usas otra URL/puerto, agrega el origen en `app/main.py` y reinicia el backend.
- **Validación:** Todos los inputs validados con Pydantic
- **BD:** Credenciales en `.env` (no en repositorio)

---

## 📊 Endpoints Principales de la API

### **Autenticación**
```
POST   /api/v1/auth/register      - Registrar nuevo usuario
POST   /api/v1/auth/login         - Iniciar sesión
POST   /api/v1/auth/refresh       - Renovar token
```

### **Canchas**
```
GET    /api/v1/canchas            - Listar todas las canchas
GET    /api/v1/canchas/{id}       - Detalle de cancha
GET    /api/v1/canchas?deporte=.. - Filtrar por deporte
```

### **Reservas**
```
POST   /api/v1/reservas                 - Crear reserva (estado: Reservada/Cancelada/Completada)
GET    /api/v1/reservas                 - Listar reservas
GET    /api/v1/reservas?usuario_id=1    - Listar reservas de un usuario
DELETE /api/v1/reservas/{id}            - Cancelar (soft delete → estado Cancelada)
```

### **Feedbacks**
```
# Crear feedback asociado a una reserva del usuario
POST   /api/v1/feedbacks/reserva/{reserva_id}?usuario_id=1

# Listar feedbacks (incluye usuario_nombre)
GET    /api/v1/feedbacks

# Listar por cancha o por usuario
GET    /api/v1/feedbacks/cancha/{cancha_id}
GET    /api/v1/feedbacks/usuario/{usuario_id}
```

---

## 🤖 Uso de Inteligencia Artificial

Durante el desarrollo, el equipo utilizó ChatGPT y Copilot como asistentes de apoyo para:

  - Solucionar errores al integrar FastAPI con MySQL
  - Adaptar la estructura de código original (JavaScript vanilla → Vue 3 + Vite)
  - Mejorar la validación de formularios y el manejo de errores
  - Generar contenido técnico del README y comentarios en el código
  - Optimizar la dockerización del proyecto

La IA fue utilizada como una herramienta de asistencia técnica y aprendizaje, no como reemplazo del trabajo del equipo.


---

## 🛠️ Troubleshooting rápido

- 500 al crear reserva con "Data truncated for column 'estado'":
  - Envía `estado` con un valor válido: `Reservada`, `Cancelada` o `Completada`.
  - El frontend ya envía `Reservada` por defecto.

- CORS Missing Allow Origin:
  - Asegura que accedes desde `http://localhost` o `http://127.0.0.1`.
  - Para otros orígenes, agrégalos en el middleware CORS (archivo `app/main.py`) y reinicia el backend.

- ¿Frontend apunta al backend incorrecto?
  - Ajusta `VITE_BACKEND_URL` en `.env` de la raíz y reconstruye el frontend.

- ¿Datos de ejemplo no aparecen?
  - Revisa logs del backend y ejecuta manualmente el seeding:
    `docker exec -i fastapi-app python -m app.scripts.load_initial_data`.


---


## 👥 Autores

- **Bastián Oyanadel**
- **Pablo Sepúlveda**
- **Nicolás Torres**
- **Benjamín Vivanco**


---


## 📄 Licencia

Este proyecto es parte de un trabajo académico de Desarrollo Web.

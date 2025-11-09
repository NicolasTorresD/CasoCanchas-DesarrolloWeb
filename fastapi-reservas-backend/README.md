# 🏟️ FastAPI Reservas Backend

Backend API para sistema de reservas de canchas deportivas. Construido con FastAPI, SQLAlchemy y SQLite/MySQL.

## 📋 Descripción

Sistema completo de gestión de reservas que incluye:
- ✅ Autenticación de usuarios con JWT
- ✅ Gestión de canchas deportivas
- ✅ Sistema de reservas con validación de disponibilidad
- ✅ Sistema de feedback y valoraciones
- ✅ Base de datos relacional con SQLAlchemy
- ✅ Migración de datos desde JSON
- ✅ Generación automática de códigos de canchas (CAN-XX)

## 🚀 Características Principales

- **Autenticación segura**: JWT tokens + bcrypt para hash de contraseñas
- **Base de datos flexible**: SQLite (desarrollo) / MySQL (producción)
- **Migración automática**: Alembic para control de versiones de BD
- **Documentación automática**: Swagger UI y ReDoc
- **Validación de datos**: Pydantic schemas con validaciones personalizadas
- **Códigos automáticos**: Generación de códigos CAN-XX para canchas
- **Arquitectura modular**: Separación clara de responsabilidades

## 📁 Estructura del Proyecto

```
fastapi-reservas-backend/
├── app/
│   ├── main.py                 # Punto de entrada de la aplicación
│   ├── database.py             # Configuración de SQLAlchemy
│   ├── api/
│   │   └── v1/
│   │       ├── router.py       # Router principal
│   │       └── endpoints/      # Endpoints de API
│   │           ├── auth.py     # Autenticación (login, register)
│   │           ├── users.py    # Gestión de usuarios
│   │           ├── canchas.py  # Gestión de canchas
│   │           ├── reservas.py # Gestión de reservas
│   │           ├── feedbacks.py # Sistema de feedback
│   │           └── deportes.py # Gestión de deportes
│   ├── models/                 # Modelos SQLAlchemy
│   │   ├── usuario.py
│   │   ├── cancha.py
│   │   ├── reserva.py
│   │   ├── feedback.py
│   │   └── deporte.py
│   ├── schemas/                # Pydantic schemas
│   │   ├── user.py
│   │   ├── cancha.py
│   │   ├── reserva.py
│   │   ├── feedback.py
│   │   └── deporte.py
│   ├── services/               # Lógica de negocio
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── cancha_service.py
│   │   ├── reserva_service.py
│   │   └── feedback_service.py
│   ├── core/
│   │   ├── config.py           # Configuración
│   │   └── security.py         # Seguridad y JWT
│   └── scripts/                # Scripts de utilidad
│       ├── load_initial_data.py # Carga de datos iniciales
│       └── inspect_db.py       # Inspección de BD
├── alembic/                    # Migraciones de base de datos
├── requirements.txt            # Dependencias Python
├── .env                        # Variables de entorno (NO subir a Git)
└── README.md                   # Este archivo
```

## 🛠️ Tecnologías

- **FastAPI 0.104.1**: Framework web moderno y rápido
- **SQLAlchemy 2.0.23**: ORM para Python
- **Alembic 1.12.1**: Herramienta de migración de BD
- **Pydantic 2.5.0**: Validación de datos
- **Python 3.12.3**: Versión de Python recomendada
- **bcrypt**: Hash seguro de contraseñas
- **PyJWT**: Tokens de autenticación
- **PyMySQL**: Driver MySQL para producción

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/NicolasTorresD/CasoCanchas-DesarrolloWeb.git
cd CasoCanchas-DesarrolloWeb/fastapi-reservas-backend
```

### 2. Crear entorno virtual

```bash
# Usar Python 3.12.3 (recomendado)
python3.12 -m venv .venv
```

### 3. Activar entorno virtual

**Linux/macOS:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Configurar variables de entorno

Crear archivo `.env` en la raíz del proyecto:

```env
# Base de datos
DATABASE_URL=sqlite:///./reservas.db

# JWT
SECRET_KEY=tu-clave-secreta-super-segura-cambiala
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Configuración de la aplicación
DEBUG=True
```

**⚠️ IMPORTANTE**: Cambia el `SECRET_KEY` por una clave segura. Puedes generarla con:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 6. Inicializar la base de datos

```bash
# Crear la base de datos y aplicar migraciones
alembic upgrade head

# Cargar datos iniciales (deportes, canchas, usuarios, reservas)
python -m app.scripts.load_initial_data
```

## 🏃 Ejecutar la aplicación

```bash
uvicorn app.main:app --reload
```

La API estará disponible en: **http://127.0.0.1:8000**

## 📚 Documentación de la API

Una vez iniciada la aplicación, accede a:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 🔐 Usuarios de Prueba

Después de cargar los datos iniciales, puedes usar estos usuarios:

| Email | Contraseña | Rol |
|-------|-----------|-----|
| admin@canchas.com | admin123 | Administrador |
| juan@email.com | password123 | Usuario |
| maria@email.com | password123 | Usuario |

## 🧪 Probar la API

### 1. Registro de nuevo usuario

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Test User",
    "email": "test@test.com",
    "password": "test123",
    "telefono": "123456789"
  }'
```

### 2. Login

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@canchas.com",
    "password": "admin123"
  }'
```

### 3. Listar canchas (requiere autenticación)

```bash
curl -X GET "http://127.0.0.1:8000/api/v1/canchas" \
  -H "Authorization: Bearer TU_TOKEN_JWT"
```

## 🗄️ Base de Datos

### Modelos principales:

1. **Usuario**: Usuarios del sistema con autenticación
2. **Deporte**: Tipos de deportes (fútbol, tenis, pádel)
3. **Cancha**: Canchas deportivas con código auto-generado (CAN-XX)
4. **Reserva**: Reservas de canchas con validación de horarios
5. **Feedback**: Comentarios y valoraciones de usuarios

### Migración de base de datos:

```bash
# Crear nueva migración después de cambios en modelos
alembic revision --autogenerate -m "descripcion del cambio"

# Aplicar migraciones
alembic upgrade head

# Revertir última migración
alembic downgrade -1
```

## 📝 Scripts de Utilidad

### Inspeccionar base de datos

```bash
python -m app.scripts.inspect_db
```

### Cargar datos iniciales

```bash
python -m app.scripts.load_initial_data
```

### Probar generación de códigos

```bash
python -m app.scripts.test_codigo_auto
```

## 🔧 Configuración para Producción

### Usando MySQL:

1. Instalar MySQL Server
2. Crear base de datos:
   ```sql
   CREATE DATABASE reservas_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
3. Actualizar `.env`:
   ```env
   DATABASE_URL=mysql+pymysql://usuario:password@localhost/reservas_db
   ```
4. Aplicar migraciones:
   ```bash
   alembic upgrade head
   ```

### Usando Docker (Recomendado):

```bash
docker-compose up -d
```

## 🐛 Solución de Problemas

### Error: "No module named 'app'"
```bash
# Asegúrate de estar en el directorio correcto
cd fastapi-reservas-backend
# Y que el entorno virtual esté activado
source .venv/bin/activate  # Linux/macOS
```

### Error: "bcrypt not found"
```bash
pip install bcrypt
```

### Error: Base de datos bloqueada (SQLite)
```bash
# Detén todos los procesos que usen la BD
# Elimina el archivo .db-journal si existe
rm reservas.db-journal
```

### Error: Versión de Python incorrecta
```bash
# Verifica tu versión
python --version

# Usa Python 3.12.3 (recomendado)
python3.12 -m venv .venv
```

## 🧪 Testing

Para verificar que todo funciona correctamente en un nuevo entorno:

```bash
# 1. Verificar instalación
python --version
pip list

# 2. Verificar base de datos
python -m app.scripts.inspect_db

# 3. Iniciar servidor
uvicorn app.main:app --reload

# 4. Probar endpoints en http://127.0.0.1:8000/docs
```

## 👥 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es parte de un trabajo académico de Desarrollo Web.

## 📞 Contacto

Para preguntas o problemas, abre un issue en el repositorio.

---

**Desarrollado con ❤️ para el curso de Desarrollo Web**
# Guía de Integración Base de Datos con API

## ✅ Estado de la Integración

La base de datos SQLite ha sido completamente integrada con la API de FastAPI.

## 📋 Componentes Implementados

### 1. Modelos SQLAlchemy (app/models/)
- ✅ `usuario.py` - Usuarios con autenticación
- ✅ `deporte.py` - Deportes disponibles
- ✅ `cancha.py` - Canchas deportivas con estados
- ✅ `reserva.py` - Reservas con validación de conflictos
- ✅ `feedback.py` - Calificaciones y comentarios
- ✅ `horario_disponible.py` - Horarios de disponibilidad

### 2. Servicios (app/services/)
- ✅ `cancha_service.py` - CRUD completo para canchas
- ✅ `reserva_service.py` - Gestión de reservas con validación de disponibilidad
- ✅ `feedback_service.py` - Gestión de feedbacks con validaciones
- ✅ `user_service.py` - Gestión de usuarios
- ✅ `deporte_service.py` - Gestión de deportes
- ⚠️  `auth_service.py` - Pendiente de implementar

### 3. Schemas Pydantic (app/schemas/)
- ✅ `cancha.py` - Validación de datos de canchas
- ✅ `reserva.py` - Validación de reservas con fechas y horas
- ✅ `feedback.py` - Validación de feedbacks
- ✅ `deporte.py` - Validación de deportes
- ⚠️  `user.py` - Verificar implementación

### 4. Endpoints API (app/api/v1/endpoints/)
- ✅ `canchas.py` - GET, POST, PUT, DELETE con filtro por deporte
- ✅ `reservas.py` - CRUD completo con filtros
- ✅ `feedbacks.py` - CRUD completo con validaciones
- ✅ `deportes.py` - CRUD completo
- ⚠️  `auth.py` - Pendiente de verificar
- ⚠️  `users.py` - Pendiente de verificar

## 🔌 Endpoints Disponibles

### Deportes
```
GET    /api/v1/deportes          - Listar todos los deportes
GET    /api/v1/deportes/{id}     - Obtener deporte por ID
POST   /api/v1/deportes          - Crear deporte
PUT    /api/v1/deportes/{id}     - Actualizar deporte
DELETE /api/v1/deportes/{id}     - Eliminar deporte
```

### Canchas
```
GET    /api/v1/canchas                    - Listar canchas (filtro: ?deporte=futbol)
GET    /api/v1/canchas/{id}               - Obtener cancha por ID
POST   /api/v1/canchas                    - Crear cancha
PUT    /api/v1/canchas/{id}               - Actualizar cancha
DELETE /api/v1/canchas/{id}               - Eliminar cancha
```

### Reservas
```
GET    /api/v1/reservas                   - Listar reservas
       Filtros: ?usuario_id=1&cancha_id=2&fecha=2024-01-15
GET    /api/v1/reservas/{id}              - Obtener reserva por ID
POST   /api/v1/reservas                   - Crear reserva (valida disponibilidad)
PUT    /api/v1/reservas/{id}              - Actualizar reserva
DELETE /api/v1/reservas/{id}              - Cancelar reserva (soft delete)
```

### Feedbacks
```
GET    /api/v1/feedbacks                  - Listar feedbacks
GET    /api/v1/feedbacks/{id}             - Obtener feedback por ID
GET    /api/v1/feedbacks/cancha/{id}      - Feedbacks de una cancha
GET    /api/v1/feedbacks/usuario/{id}     - Feedbacks de un usuario
POST   /api/v1/feedbacks/reserva/{id}     - Crear feedback para reserva
DELETE /api/v1/feedbacks/{id}             - Eliminar feedback
```

## 🚀 Cómo Iniciar el Servidor

### 1. Activar el entorno virtual
```bash
cd fastapi-reservas-backend
source venv/bin/activate  # En Linux/Mac
# o
venv\Scripts\activate  # En Windows
```

### 2. Verificar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar pruebas de integración (opcional)
```bash
python -m app.scripts.test_integration
```

### 4. Iniciar el servidor
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Acceder a la documentación interactiva
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 📊 Datos Iniciales Cargados

### Deportes (4)
- Fútbol
- Tenis
- Básquetbol
- Pádel

### Canchas (15)
- 5 canchas de Fútbol (CAN-01 a CAN-05)
- 5 canchas de Tenis (CAN-06 a CAN-10)
- 5 canchas de Pádel (CAN-11 a CAN-15)

### Usuarios (5)
- 5 usuarios de prueba con password "password123"

## 🔐 Validaciones Implementadas

### Reservas
- ✅ Verificación de disponibilidad de cancha
- ✅ Constraint único: (cancha, fecha, hora)
- ✅ No permite reservas duplicadas
- ✅ Soft delete (cambia estado a CANCELADA)

### Feedbacks
- ✅ Solo un feedback por reserva
- ✅ Validación de pertenencia de reserva al usuario
- ✅ Obtención automática de id_cancha desde la reserva

### Canchas
- ✅ Código único por cancha
- ✅ Estado: Disponible, Mantenimiento, Inactiva
- ✅ Relación con deporte obligatoria

## 🧪 Pruebas con cURL

### Obtener todos los deportes
```bash
curl http://localhost:8000/api/v1/deportes
```

### Obtener canchas de fútbol
```bash
curl "http://localhost:8000/api/v1/canchas?deporte=futbol"
```

### Crear una reserva
```bash
curl -X POST http://localhost:8000/api/v1/reservas \
  -H "Content-Type: application/json" \
  -d '{
    "id_usuario": 1,
    "id_cancha": 1,
    "fecha": "2024-12-25",
    "hora": "14:00:00",
    "duracion": 60,
    "estado": "Confirmada",
    "precio_total": 50.00
  }'
```

### Crear un feedback
```bash
curl -X POST http://localhost:8000/api/v1/feedbacks/reserva/1?usuario_id=1 \
  -H "Content-Type: application/json" \
  -d '{
    "calificacion": 5,
    "comentario": "Excelente cancha, muy bien mantenida"
  }'
```

## 🔄 Migración a MySQL (Futuro con Docker)

Para cambiar a MySQL en producción:

1. Actualizar `.env`:
```env
# Comentar SQLite
# DATABASE_URL=sqlite:///./reservas.db

# Descomentar MySQL
DATABASE_URL=mysql+pymysql://usuario:password@db:3306/reservas_db
```

2. Ejecutar migración:
```bash
alembic upgrade head
python -m app.scripts.load_initial_data
```

## 📝 Próximos Pasos

1. ⚠️  Implementar autenticación JWT completa
2. ⚠️  Agregar middleware de autorización
3. ⚠️  Implementar endpoints para horarios disponibles
4. ⚠️  Agregar tests unitarios
5. ⚠️  Configurar Docker y docker-compose
6. ⚠️  Implementar paginación en listados
7. ⚠️  Agregar filtros avanzados
8. ⚠️  Documentar con ejemplos en Swagger

## 🐛 Troubleshooting

### Error: "Table already exists"
```bash
# Eliminar base de datos y recrear
rm reservas.db
alembic upgrade head
python -m app.scripts.load_initial_data
```

### Error: "Import could not be resolved"
Los errores de lint son normales si Pylance no detecta el entorno virtual. Asegúrate de:
1. Activar el entorno virtual
2. Seleccionar el intérprete correcto en VS Code (Ctrl+Shift+P -> Python: Select Interpreter)

### Error al iniciar servidor
```bash
# Verificar que el puerto 8000 no esté en uso
lsof -ti:8000 | xargs kill -9  # En Linux/Mac
# o
netstat -ano | findstr :8000   # En Windows
```

## 📚 Documentación Adicional

- [Documentación de FastAPI](https://fastapi.tiangolo.com/)
- [Documentación de SQLAlchemy](https://docs.sqlalchemy.org/)
- [Documentación de Alembic](https://alembic.sqlalchemy.org/)
- [Documentación de Pydantic](https://docs.pydantic.dev/)

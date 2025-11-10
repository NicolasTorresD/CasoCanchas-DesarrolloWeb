# 🎉 Base de Datos Implementada - Sistema de Reservas de Canchas

## ✅ Implementación Completada

Se ha implementado exitosamente la base de datos con **SQLAlchemy + Alembic + MySQL** (preparado para Docker).

---

## 📊 Modelos Implementados (Basados en DIAGRAMA_BD.md)

### 1. **Usuarios** (`usuarios`)
- Gestión de clientes del sistema
- Autenticación con password hasheado (bcrypt)
- Campos: id_usuario, nombre, email, telefono, password_hash, fecha_registro, activo

### 2. **Deportes** (`deportes`)
- Catálogo de deportes disponibles
- Campos: id_deporte, nombre, descripcion, activo

### 3. **Canchas** (`canchas`)
- Información de las instalaciones deportivas
- Relación con Deportes (N:1)
- Campos: id_cancha, id_deporte, nombre, codigo, imagen_url, color, precio_hora, estado, fecha_creacion

### 4. **Reservas** (`reservas`)
- Sistema de reservas de canchas
- Relaciones: Usuario (N:1), Cancha (N:1)
- Constraint: No permite reservas duplicadas (misma cancha, fecha y hora)
- Campos: id_reserva, id_usuario, id_cancha, fecha, hora, duracion, estado, precio_total, fecha_reserva, fecha_cancelacion

### 5. **Feedbacks** (`feedbacks`)
- Calificaciones y comentarios de usuarios
- Relaciones: Reserva (1:1), Usuario (N:1), Cancha (N:1)
- Constraint: Calificación entre 1 y 5
- Campos: id_feedback, id_reserva, id_usuario, id_cancha, calificacion, comentario, fecha, timestamp

### 6. **Horarios Disponibles** (`horarios_disponibles`)
- Configuración de horarios por cancha
- Relación con Canchas (N:1)
- Campos: id_horario, id_cancha, dia_semana, hora_inicio, hora_fin, activo

---

## 🔧 Tecnologías Utilizadas

- **ORM:** SQLAlchemy 2.0.23
- **Migraciones:** Alembic 1.12.1
- **Driver MySQL:** PyMySQL 1.1.0
- **Base de Datos:** SQLite (desarrollo) / MySQL (producción/Docker)
- **Python:** 3.12.3

---

## 📁 Estructura de Archivos Creada

```
fastapi-reservas-backend/
├── app/
│   ├── database.py                    # ✅ Configuración SQLAlchemy
│   ├── models/
│   │   ├── __init__.py               # ✅ Exporta todos los modelos
│   │   ├── usuario.py                # ✅ Modelo Usuario
│   │   ├── deporte.py                # ✅ Modelo Deporte
│   │   ├── cancha.py                 # ✅ Modelo Cancha
│   │   ├── reserva.py                # ✅ Modelo Reserva
│   │   ├── feedback.py               # ✅ Modelo Feedback
│   │   └── horario_disponible.py    # ✅ Modelo HorarioDisponible
│   └── scripts/
│       ├── __init__.py
│       └── load_initial_data.py      # ✅ Script de carga de datos
├── alembic/
│   ├── env.py                        # ✅ Configurado para auto-detectar modelos
│   ├── versions/
│   │   └── 33d457cbc626_initial_migration.py  # ✅ Migración inicial
│   └── ...
├── alembic.ini                       # ✅ Configurado
├── .env                              # ✅ DATABASE_URL configurado
├── requirements.txt                  # ✅ Dependencias actualizadas
└── reservas.db                       # ✅ Base de datos SQLite (desarrollo)
```

---

## 🚀 Comandos Útiles

### Migraciones con Alembic

```bash
# Generar nueva migración (auto-detecta cambios en modelos)
alembic revision --autogenerate -m "Descripción del cambio"

# Aplicar migraciones
alembic upgrade head

# Ver historial de migraciones
alembic history

# Revertir última migración
alembic downgrade -1

# Ver estado actual
alembic current
```

### Cargar Datos Iniciales

```bash
# Ejecutar script de carga de datos
python -m app.scripts.load_initial_data
```

### Cambiar a MySQL (cuando dockerices)

Edita `.env`:
```env
# Comentar SQLite
# DATABASE_URL=sqlite:///./reservas.db

# Descomentar MySQL
DATABASE_URL=mysql+pymysql://reservas_user:reservas_pass_123@localhost:3306/reservas_db
```

Luego ejecuta las migraciones:
```bash
alembic upgrade head
python -m app.scripts.load_initial_data
```

---

## 📊 Datos Cargados

### Deportes:
- ✅ Fútbol
- ✅ Tenis
- ✅ Básquetbol
- ✅ Pádel

### Canchas:
- ✅ 15 canchas (5 de fútbol, 5 de tenis, 5 de pádel)
- Códigos: CAN-01 a CAN-15
  - CAN-01 a CAN-05: Fútbol
  - CAN-06 a CAN-10: Tenis
  - CAN-11 a CAN-15: Pádel

### Usuarios:
- ✅ 5 usuarios de ejemplo
- 📝 **Password para todos:** `password123`
- Emails: carlos.diaz@example.com, maria.lopez@example.com, jose.perez@example.com, ana.fernandez@example.com, luis.gonzalez@example.com

---

## 🐳 Preparado para Docker

El proyecto está configurado para cambiar fácilmente entre SQLite (desarrollo) y MySQL (producción con Docker).

### Para usar con Docker en el futuro:

1. **Crear `docker-compose.yml`** en la raíz del proyecto con MySQL
2. **Cambiar `DATABASE_URL`** en `.env` a MySQL
3. **Ejecutar:** `docker-compose up -d`
4. **Aplicar migraciones:** `alembic upgrade head`
5. **Cargar datos:** `python -m app.scripts.load_initial_data`

---

## 🎯 Reglas de Negocio Implementadas

1. **✅ No reservas duplicadas:** Constraint único (cancha + fecha + hora)
2. **✅ Emails únicos:** No puede haber usuarios con el mismo email
3. **✅ Códigos únicos:** Cada cancha tiene un código único
4. **✅ Feedback único por reserva:** Solo un feedback por reserva
5. **✅ Calificaciones válidas:** Entre 1 y 5 estrellas
6. **✅ Días de semana válidos:** Entre 0 (Domingo) y 6 (Sábado)
7. **✅ Integridad referencial:** Foreign keys con CASCADE en eliminaciones

---

## ✅ Requisitos Cumplidos

- ✅ **Modelo de datos coherente** con la aplicación original
- ✅ **Implementado con SQLAlchemy** (ORM moderno)
- ✅ **Alembic configurado** para migraciones
- ✅ **SQLite para desarrollo** (sin instalación adicional)
- ✅ **Preparado para MySQL** (cuando dockerices)
- ✅ **Datos iniciales migrados** desde JSON

---

## 📝 Próximos Pasos Recomendados

1. **Integrar modelos con la API** (actualizar endpoints existentes)
2. **Implementar CRUD completo** para todas las entidades
3. **Agregar validaciones de negocio** en los servicios
4. **Dockerizar el proyecto** (cuando sea necesario)
5. **Implementar tests** para los modelos

---

**¡La base de datos está lista para usar!** 🎉

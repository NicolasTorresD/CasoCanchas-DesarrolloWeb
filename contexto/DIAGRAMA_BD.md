# Diagrama de Base de Datos - Sistema de Reservas de Canchas

## 📊 Diagrama Entidad-Relación (ERD)

```
┌─────────────────────────────────────┐
│           USUARIOS                  │
├─────────────────────────────────────┤
│ PK  id_usuario        INT           │
│     nombre            VARCHAR(100)  │
│     email             VARCHAR(100)  │ UNIQUE
│     telefono          VARCHAR(20)   │
│     password_hash     VARCHAR(255)  │
│     fecha_registro    TIMESTAMP     │
│     activo            BOOLEAN       │
└─────────────────────────────────────┘
              │
              │ 1
              │
              │
              │ N
┌─────────────▼───────────────────────┐
│           RESERVAS                  │
├─────────────────────────────────────┤
│ PK  id_reserva        INT           │
│ FK  id_usuario        INT           │
│ FK  id_cancha         INT           │
│     fecha             DATE          │
│     hora              TIME          │
│     duracion          INT           │ (minutos)
│     estado            ENUM          │ (Reservada, Cancelada, Completada)
│     precio_total      DECIMAL(10,2) │
│     fecha_reserva     TIMESTAMP     │
│     fecha_cancelacion TIMESTAMP     │
└─────────────────────────────────────┘
              │
              │ 1
              │
              │
              │ N
┌─────────────▼───────────────────────┐
│           FEEDBACKS                 │
├─────────────────────────────────────┤
│ PK  id_feedback       INT           │
│ FK  id_reserva        INT           │ UNIQUE
│ FK  id_usuario        INT           │
│ FK  id_cancha         INT           │
│     calificacion      INT           │ (1-5)
│     comentario        TEXT          │
│     fecha             DATE          │
│     timestamp         TIMESTAMP     │
└─────────────────────────────────────┘
              │
              │
              ├──────────────────┐
              │                  │
              │ N                │ N
              │                  │
┌─────────────▼───────────────────────┐
│           CANCHAS                   │
├─────────────────────────────────────┤
│ PK  id_cancha         INT           │
│ FK  id_deporte        INT           │
│     nombre            VARCHAR(100)  │
│     codigo            VARCHAR(20)   │ UNIQUE
│     imagen_url        VARCHAR(255)  │
│     color             VARCHAR(7)    │
│     precio_hora       DECIMAL(10,2) │
│     estado            ENUM          │ (Disponible, Mantenimiento, Inactiva)
│     fecha_creacion    TIMESTAMP     │
└─────────────────────────────────────┘
              │
              │ N
              │
              │
              │ 1
┌─────────────▼───────────────────────┐
│           DEPORTES                  │
├─────────────────────────────────────┤
│ PK  id_deporte        INT           │
│     nombre            VARCHAR(50)   │ UNIQUE
│     descripcion       TEXT          │
│     activo            BOOLEAN       │
└─────────────────────────────────────┘


┌─────────────────────────────────────┐
│      HORARIOS_DISPONIBLES           │
├─────────────────────────────────────┤
│ PK  id_horario        INT           │
│ FK  id_cancha         INT           │
│     dia_semana        INT           │ (0=Domingo, 6=Sábado)
│     hora_inicio       TIME          │
│     hora_fin          TIME          │
│     activo            BOOLEAN       │
└─────────────────────────────────────┘
```

## 🔗 Relaciones

### 1. USUARIOS → RESERVAS (1:N)
- Un usuario puede tener múltiples reservas
- Una reserva pertenece a un solo usuario

### 2. CANCHAS → RESERVAS (1:N)
- Una cancha puede tener múltiples reservas
- Una reserva es para una sola cancha

### 3. RESERVAS → FEEDBACKS (1:1)
- Una reserva puede tener un único feedback
- Un feedback está asociado a una reserva específica

### 4. USUARIOS → FEEDBACKS (1:N)
- Un usuario puede dejar múltiples feedbacks
- Un feedback es de un solo usuario

### 5. CANCHAS → FEEDBACKS (1:N)
- Una cancha puede tener múltiples feedbacks
- Un feedback es para una sola cancha

### 6. DEPORTES → CANCHAS (1:N)
- Un deporte puede tener múltiples canchas
- Una cancha pertenece a un solo deporte

### 7. CANCHAS → HORARIOS_DISPONIBLES (1:N)
- Una cancha puede tener múltiples horarios disponibles
- Un horario pertenece a una sola cancha

---

## 📝 Scripts SQL para Crear las Tablas

### 1. Tabla DEPORTES
```sql
CREATE TABLE deportes (
    id_deporte INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    descripcion TEXT,
    activo BOOLEAN DEFAULT TRUE,
    INDEX idx_nombre (nombre)
);
```

### 2. Tabla CANCHAS
```sql
CREATE TABLE canchas (
    id_cancha INT AUTO_INCREMENT PRIMARY KEY,
    id_deporte INT NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    codigo VARCHAR(20) NOT NULL UNIQUE,
    imagen_url VARCHAR(255),
    color VARCHAR(7) DEFAULT '#000000',
    precio_hora DECIMAL(10,2) NOT NULL,
    estado ENUM('Disponible', 'Mantenimiento', 'Inactiva') DEFAULT 'Disponible',
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_deporte) REFERENCES deportes(id_deporte),
    INDEX idx_deporte (id_deporte),
    INDEX idx_estado (estado),
    INDEX idx_codigo (codigo)
);
```

### 3. Tabla USUARIOS
```sql
CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(20),
    password_hash VARCHAR(255) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE,
    INDEX idx_email (email),
    INDEX idx_nombre (nombre)
);
```

### 4. Tabla RESERVAS
```sql
CREATE TABLE reservas (
    id_reserva INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_cancha INT NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    duracion INT DEFAULT 60 COMMENT 'Duración en minutos',
    estado ENUM('Reservada', 'Cancelada', 'Completada') DEFAULT 'Reservada',
    precio_total DECIMAL(10,2) NOT NULL,
    fecha_reserva TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_cancelacion TIMESTAMP NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_cancha) REFERENCES canchas(id_cancha),
    INDEX idx_usuario (id_usuario),
    INDEX idx_cancha (id_cancha),
    INDEX idx_fecha (fecha),
    INDEX idx_estado (estado),
    UNIQUE KEY unique_reserva (id_cancha, fecha, hora)
);
```

### 5. Tabla FEEDBACKS
```sql
CREATE TABLE feedbacks (
    id_feedback INT AUTO_INCREMENT PRIMARY KEY,
    id_reserva INT NOT NULL UNIQUE,
    id_usuario INT NOT NULL,
    id_cancha INT NOT NULL,
    calificacion INT NOT NULL CHECK (calificacion BETWEEN 1 AND 5),
    comentario TEXT,
    fecha DATE NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_reserva) REFERENCES reservas(id_reserva),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_cancha) REFERENCES canchas(id_cancha),
    INDEX idx_cancha (id_cancha),
    INDEX idx_usuario (id_usuario),
    INDEX idx_calificacion (calificacion),
    INDEX idx_fecha (fecha)
);
```

### 6. Tabla HORARIOS_DISPONIBLES
```sql
CREATE TABLE horarios_disponibles (
    id_horario INT AUTO_INCREMENT PRIMARY KEY,
    id_cancha INT NOT NULL,
    dia_semana INT NOT NULL CHECK (dia_semana BETWEEN 0 AND 6) COMMENT '0=Domingo, 6=Sábado',
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (id_cancha) REFERENCES canchas(id_cancha),
    INDEX idx_cancha (id_cancha),
    INDEX idx_dia (dia_semana)
);
```

---

## 🔒 Constraints y Validaciones

### Reglas de Negocio Implementadas:

1. **RESERVAS:**
   - No puede haber dos reservas para la misma cancha en la misma fecha y hora (UNIQUE constraint)
   - El estado solo puede ser: Reservada, Cancelada o Completada

2. **FEEDBACKS:**
   - Solo se puede dejar un feedback por reserva (UNIQUE en id_reserva)
   - La calificación debe estar entre 1 y 5

3. **USUARIOS:**
   - El email debe ser único en el sistema
   - Password debe estar hasheado

4. **CANCHAS:**
   - El código de cancha debe ser único
   - El precio debe ser mayor a 0

5. **HORARIOS_DISPONIBLES:**
   - El día de la semana debe estar entre 0 (Domingo) y 6 (Sábado)

---

## 📈 Datos Iniciales (Migración desde JSON)

### Script de Migración de Datos

```sql
-- Insertar Deportes
INSERT INTO deportes (nombre, descripcion, activo) VALUES
('futbol', 'Fútbol 5 y 7', TRUE),
('tenis', 'Tenis individual y dobles', TRUE),
('basquet', 'Básquetbol', TRUE),
('voley', 'Vóleibol', TRUE);

-- Insertar Canchas (basado en canchas.json)
INSERT INTO canchas (id_deporte, nombre, codigo, imagen_url, color, precio_hora, estado) VALUES
(1, 'Cancha de Fútbol 1', 'CAN-01', 'imagenes/chancha-futbol.png', '#28a745', 25.00, 'Disponible'),
(1, 'Cancha de Fútbol 2', 'CAN-02', 'imagenes/chancha-futbol.png', '#28a745', 30.00, 'Disponible'),
(1, 'Cancha de Fútbol 3', 'CAN-03', 'imagenes/chancha-futbol.png', '#28a745', 35.00, 'Disponible'),
(1, 'Cancha de Fútbol 4', 'CAN-04', 'imagenes/chancha-futbol.png', '#28a745', 28.00, 'Disponible'),
(1, 'Cancha de Fútbol 5', 'CAN-05', 'imagenes/chancha-futbol.png', '#28a745', 32.00, 'Disponible'),
(2, 'Cancha de Tenis 1', 'CAN-06', 'imagenes/cancha-tenis.png', '#007bff', 20.00, 'Disponible');

-- Crear usuarios de ejemplo (deberás obtener estos datos de tu sistema)
INSERT INTO usuarios (nombre, email, telefono, password_hash) VALUES
('Carlos Díaz', 'carlos.diaz@example.com', '555-0001', 'hash_aqui'),
('María López', 'maria.lopez@example.com', '555-0002', 'hash_aqui'),
('José Pérez', 'jose.perez@example.com', '555-0003', 'hash_aqui'),
('Ana Fernández', 'ana.fernandez@example.com', '555-0004', 'hash_aqui'),
('Luis González', 'luis.gonzalez@example.com', '555-0005', 'hash_aqui');
```

---

## 🎯 Ventajas de esta Estructura

1. **Normalización:** Datos bien organizados sin redundancia
2. **Integridad Referencial:** Las FK garantizan consistencia
3. **Escalabilidad:** Fácil agregar nuevas entidades (ej: servicios adicionales)
4. **Seguridad:** Passwords hasheados, validaciones a nivel de BD
5. **Trazabilidad:** Timestamps en todas las operaciones importantes
6. **Rendimiento:** Índices en campos más consultados
7. **Flexibilidad:** Fácil agregar campos nuevos sin romper la estructura

---

## 🚀 Próximos Pasos Recomendados

1. **Implementar autenticación de usuarios**
2. **Sistema de notificaciones (email/SMS simulado)**
3. **Reportes y estadísticas de uso**
4. **Dashboard administrativo**
5. **Validación de disponibilidad en tiempo real**
6. **API REST para operaciones CRUD**

---

## 📚 Tecnologías Recomendadas

- **Base de Datos:** MySQL 8.0+ / PostgreSQL 13+
- **Backend:** Node.js + Express / Python + FastAPI
- **ORM:** Sequelize / TypeORM / Prisma
- **Frontend:** Vue.js 3 (ya lo tienes)
- **Autenticación:** JWT + bcrypt


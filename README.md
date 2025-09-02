# 🏟️ Reservas de Canchas Deportivas – *Frontend Only*

> **Asignatura:** Desarrollo Web y Móvil  
> **Objetivo:** Prototipo de sistema de reservas de canchas deportivas sin backend, desarrollado con **HTML**, **CSS**, **JavaScript**, **Bootstrap** y persistencia en **localStorage**.

---

## 📄 Descripción del Proyecto

Este proyecto implementa un **sistema de reservas de canchas deportivas** para un club. Permite a los usuarios seleccionar el deporte, elegir una cancha, definir fecha y hora de reserva, validar la disponibilidad y confirmar la reserva mediante **modales interactivos**.

**Características principales:**
- Listado dinámico de canchas por deporte.
- Formulario para reservar con validaciones.
- Calendario simple de reservas confirmadas.
- Cancelación de reservas mediante modal de confirmación.
- Persistencia en **localStorage** para simular un backend.
- Uso de **Bootstrap** para diseño responsivo y componentes visuales.

---

## 🔧 Instalación y Configuración

### **1. Clonar el repositorio**
```bash
git clone https://github.com/usuario/CasoCanchas.git
cd CasoCanchas
```

### **2. Abrir el proyecto**
Como es **Frontend Only**, basta con abrir `index.html` en el navegador.

### **3. Requisitos previos**
- Navegador moderno compatible con `localStorage` y `fetch()`.
- **Bootstrap 5** integrado mediante CDN.

---

## 🗂️ Estructura del Proyecto

```bash
CasoCanchas/
├── app.js               # Lógica principal en JavaScript
├── canchas.json         # Datos de canchas
├── feedbacks.json       # Mensajes de feedback
├── index.html           # Página principal de reservas
├── reservas.json        # Datos iniciales de reservas
├── styles.css           # Estilos personalizados
└── imagenes/            # Recursos gráficos
    ├── cancha-padel.png
    ├── cancha-tenis.png
    ├── chancha-futbol.png
    └── d3900ac9-0679-4715-a069-df05ccf749a3.png
```

---

## 🚀 Funcionalidades Principales

- **Selección de canchas**: listado dinámico con filtros por deporte.
- **Formulario de reserva**:
  - Validación de fecha futura.
  - Validación de franja horaria válida.
  - Bloqueo de reservas duplicadas.
- **Confirmación de reservas**:
  - Modales interactivos para confirmar.
- **Gestión de reservas**:
  - Estado: **Reservada** / **Cancelada**.
  - Cancelación mediante modal.
  **Feedback**
  - Sección de comentarios
- **Persistencia local**:
  - Guardado automático en **localStorage**.

---

## 🛠️ Decisiones Técnicas

- **Framework CSS:** **Bootstrap 5** para un diseño responsivo y componentes reutilizables.
- **Persistencia:** `localStorage` simula una base de datos.
- **Datos iniciales:** Cargados desde archivos `JSON` mediante `fetch()`.
- **Validaciones:** Implementadas con **JavaScript puro**, sin librerías externas.
- **Feedbacks:** Uso de **toasts** y **alerts** de Bootstrap para informar al usuario.

---

## 📚 Datos de Ejemplo

**canchas.json**
```json
[
 {
    "id": "CAN-01",
    "nombre": "Cancha de Fútbol 1",
    "deporte": "futbol",
    "imagen": "imagenes/chancha-futbol.png",
    "color": "#28a745"
  },
  {
    "id": "CAN-02",
    "nombre": "Cancha de Fútbol 2",
    "deporte": "futbol",
    "imagen": "imagenes/chancha-futbol.png",
    "color": "#28a745"
  },
  {
    "id": "CAN-03",
    "nombre": "Cancha de Fútbol 3",
    "deporte": "futbol",
    "imagen": "imagenes/chancha-futbol.png",
    "color": "#28a745"
  }
]
```

**reservas.json**
```json
[
  {
    "id": "R001",
    "usuario": "Carlos Díaz",
    "canchaId": "CAN-01",
    "fecha": "2025-09-01",
    "hora": "18:00",
    "estado": "Reservada"
  },
  {
    "id": "R002",
    "usuario": "María López",
    "canchaId": "CAN-02",
    "fecha": "2025-09-02",
    "hora": "16:00",
    "estado": "Reservada"
  },
  {
    "id": "R003",
    "usuario": "José Pérez",
    "canchaId": "CAN-03",
    "fecha": "2025-09-03",
    "hora": "19:00",
    "estado": "Cancelada"
  }
]
```

---

## 👨‍💻 Funciones JavaScript Implementadas

- `obtenerNombreCanchaPorId()` → Devuelve el nombre de una cancha según su ID.
- `obtenerIdCanchaPorNombre()` → Obtiene el ID de una cancha por su nombre.
- `showPage()` → Controla el cambio entre páginas/vistas.
- `cargarCanchasDesdeJSON()` → Carga las canchas desde `canchas.json`.
- `cargarReservasDesdeJSON()` → Carga las reservas iniciales desde `reservas.json`.
- `renderizarCanchas()` → Renderiza tarjetas dinámicas de canchas.
- `generateTimeOptions()` → Genera opciones automáticas de horarios.
- `cargarReservas()` → Muestra las reservas actuales y actualiza la interfaz.

---


## 👥 Autores

- **Pablo Sepúlveda Ulloa**
- **Nicolás Torres Diaz**
- **Benjamín Vivanco Guerra**
- **Bastián Oyanadel Pizarro**

---

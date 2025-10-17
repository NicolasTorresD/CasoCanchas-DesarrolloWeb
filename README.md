# 🏟️ Proyecto: Reservas de Canchas Deportivas con API del Clima (Open-Meteo)


> **Asignatura:** Desarrollo Web y Móvil  
> **Integrantes:** Bastián Oyanadel · Pablo Sepúlveda · Nicolás Torres · Benjamín Vivanco  
> **Tecnologías:** HTML · CSS · JavaScript · Bootstrap · Open-Meteo API  
> **Tipo de proyecto:** Frontend Only  
> **Apoyo:** Desarrollo asistido por Inteligencia Artificial (ChatGPT / Copilot)


---


## 🧩 Descripción del Proyecto


Este proyecto consiste en una **aplicación web interactiva para la reserva de canchas deportivas**, desarrollada con tecnologías frontend y complementada con una **API meteorológica (Open-Meteo)** que permite visualizar el **clima actual** antes de realizar una reserva.

La aplicación está pensada para **simular un sistema real de gestión de reservas** de un club deportivo, con el propósito de ofrecer una experiencia práctica al usuario, integrando conceptos de validación de formularios, persistencia de datos y consumo de servicios externos.  
Además, se mantuvo la filosofía del proyecto original, pero mejorando la organización del código, la interactividad y el diseño visual.


---


## ⚙️ Tecnologías Utilizadas

| Herramienta - Uso principal 

| **HTML5 / CSS3** : Estructura y estilo del sitio.
| **JavaScript (ES6)** : Lógica funcional, validaciones, consumo de API y renderización dinámica.
| **Bootstrap 5** : Diseño responsivo, modales, toasts y componentes visuales.
| **JSON / LocalStorage** : Simulación de persistencia de datos de reservas y canchas.
| **Open-Meteo API** : Obtención del clima actual según coordenadas predefinidas.
| **ChatGPT / Copilot** : Asistencia técnica durante el desarrollo e integración de la API.


---


## 🌐 Uso de la Aplicación


Al ingresar al sitio, el usuario accede a una interfaz simple y funcional, organizada en tres vistas principales:

### **1. Página principal**
- Se presentan las **canchas disponibles**, separadas por deporte (fútbol, tenis y pádel).
- Cada cancha se muestra dentro de una **tarjeta con imagen, nombre y botón de reserva**.
- Desde esta vista el usuario puede seleccionar qué cancha desea reservar.

### **2. Formulario de reserva**
- Una vez seleccionada la cancha, se despliega un formulario donde el usuario ingresa:
  - Su **nombre**.
  - La **fecha y hora** deseada.
  - El **deporte/cancha** (precargado según selección).
- En esta misma vista se muestra la **información del clima actual**, obtenida desde la **API Open-Meteo**.
- El sistema consulta automáticamente la API al cargar la vista y muestra:
  - Temperatura (°C)
  - Velocidad del viento
  - Estado general del clima (interpretado según código meteorológico)
- Si ocurre un error (por ejemplo, sin conexión o coordenadas no válidas), se muestra un **mensaje de advertencia** con Bootstrap.

### **3. Listado de reservas**
- Las reservas confirmadas se almacenan en el navegador usando **localStorage**, simulando una base de datos.
- El usuario puede ver todas sus reservas en una tabla con la siguiente información:
  - Nombre del usuario.
  - Cancha y deporte.
  - Fecha y hora.
  - Estado (Reservada / Cancelada).
- Desde este listado es posible **cancelar una reserva** a través de un **modal de confirmación**, que actualiza el estado en tiempo real.


---


## 🌤️ Integración de la API Open-Meteo

La aplicación utiliza la **API pública Open-Meteo**, que entrega información meteorológica en tiempo real mediante coordenadas geográficas.  
La integración se realiza con `fetch()` directamente desde el frontend.

**Endpoint base:**
``bash
  https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current_weather=true


---


## Datos utilizados:

- Temperatura actual (temperature)
- Velocidad del viento (windspeed)
- Código del clima (weathercode), convertido en texto (“Soleado”, “Nublado”, “Lluvia ligera”, etc.)

## Manejo de errores:

- Si la API no responde, la aplicación muestra un aviso como:
  - “No se pudieron obtener los datos del clima. Intente nuevamente más tarde.”
- En caso de respuesta vacía o datos fuera de rango, se cargan valores por defecto o se oculta el cuadro de clima.

Esta integración permite que el usuario considere las condiciones climáticas antes de confirmar su reserva.


---


## 🧠 Estructura del Código

El código está dividido en partes claras que separan la lógica de la interfaz, la persistencia de datos y el consumo de la API.

# index.html

  - Define la estructura principal de la página.

  - Contiene los contenedores donde se renderizan las canchas, el formulario y el listado de reservas.

  - Importa los scripts de Bootstrap, el archivo principal app.js y los estilos CSS personalizados.

# app.js

Contiene toda la lógica funcional del sitio. Se destacan las siguientes funciones principales:

Función -	Descripción
  - loadCanchas()	: Carga los datos desde canchas.json y genera las tarjetas de canchas.
  - renderReservas()	: Muestra la lista de reservas actuales y las actualiza dinámicamente.
  - reservarCancha()	: Valida los datos ingresados y guarda una nueva reserva en localStorage.
  - cancelarReserva(id)	: Cambia el estado de una reserva a “Cancelada”.
  - obtenerClima()	: Realiza la petición a la API de Open-Meteo y muestra la información del clima.
  - mostrarToast() / mostrarModal()	Muestra mensajes y confirmaciones usando Bootstrap.

# canchas.json / reservas.json

- Archivos de ejemplo que contienen la información inicial del sistema.
- canchas.json define el listado de canchas disponibles.
- reservas.json entrega un formato inicial para pruebas.

# styles.css

- Contiene los estilos personalizados que complementan Bootstrap.
- Se definen colores, espaciados y tamaños específicos para mantener coherencia visual.


---


## 🚀 Instalación y Ejecución

1. Clonar el repositorio:
  git clone https://github.com/usuario/CasoCanchas.git

2. Abrir el proyecto en Visual Studio Code.
3. Iniciar el entorno con Live Server o abrir directamente index.html en el navegador.
4. Comprobar conexión a Internet (requerida para el funcionamiento de la API).


---


## 🤖 Uso de Inteligencia Artificial

Durante el desarrollo, el equipo utilizó ChatGPT y Copilot como asistentes de apoyo para:

  - Solucionar errores al integrar la API del clima.
  - Adaptar la estructura de código de la versión anterior del proyecto.
  - Mejorar la validación de formularios y el manejo de errores.
  - Generar parte del contenido técnico del README y comentarios en el código.

La IA fue utilizada como una herramienta de asistencia técnica y aprendizaje, no como reemplazo del trabajo del equipo.


---


## 👥 Autores

# Bastián Oyanadel
# Pablo Sepúlveda
# Nicolás Torres
# Benjamín Vivanco


---
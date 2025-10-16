# Proyecto: Reservas de Canchas con Vue.js y API del Clima (Open-Meteo)

> **Asignatura:** Desarrollo Web y Móvil
> **Integrantes:** Bastián Oyanadel, Pablo Sepúlveda, Nicolás Torres, Benjamín Vivanco
> **Framework:** Vue.js
> **API utilizada:** Open-Meteo (versión gratuita)
> **Apoyo de IA:** Desarrollo asistido por Inteligencia Artificial (ChatGPT / VSCode Copilot)

---

## Descripción General

Este proyecto extiende el prototipo original de reservas de canchas deportivas, integrando ahora el framework **Vue.js** para una mejor organización del frontend y el consumo de una API externa (Open-Meteo) que permite mostrar el clima actual en la vista de reservas.

El objetivo es ofrecer una experiencia más completa al usuario, mostrando las condiciones climáticas del día antes de confirmar la reserva, ayudando a tomar decisiones informadas según el clima.

---

## Tecnologías y Herramientas

| Herramienta             - Uso principal                                                                                   
| **Vue.js 3**            : Framework frontend para estructurar componentes y gestionar el estado de la app.                
| **Bootstrap 5**         : Framework de CSS para estilos responsivos, modales y componentes visuales.                      
| **Open-Meteo API**      : Fuente externa de datos meteorológicos en tiempo real.                                          
| **JavaScript (ES6)**    : Lógica funcional para manejo de datos y eventos.                                                
| **JSON / LocalStorage** : Persistencia local de reservas y canchas.                                                       
| **Visual Studio Code**  : Entorno de desarrollo.                                                                          
| **ChatGPT / Copilot**   : Asistente de programación para integración de Vue, resolución de errores y conexión con la API. 

---

## Estructura del Proyecto

```bash
CasoCanchasVue/
├── app-vue.js              # Lógica principal con Vue.js y consumo de la API del clima
├── app.js                  # Código base original sin framework
├── public/
│   ├── canchas.json        # Datos locales de canchas disponibles
│   ├── reservas.json       # Datos de reservas iniciales
│   ├── feedbacks.json      # Mensajes y alertas
│   └── imagenes/           # Recursos visuales
├── styles.css              # Estilos personalizados
├── index.html              # Estructura principal de la aplicación
└── README.md               # Documentación del proyecto
```

---

## Explicación Técnica de la API

### API Utilizada: [Open-Meteo](https://open-meteo.com/)

#### Endpoint principal:

```bash
https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current_weather=true
```

#### **Parámetros utilizados:**

| `latitude`        : Latitud de la ubicación (por ejemplo: -33.45 para Santiago).  
| `longitude`       : Longitud de la ubicación (por ejemplo: -70.65 para Santiago). 
| `current_weather` : Si se establece en `true`, devuelve el clima actual.          

#### **Ejemplo de Request:**

```bash
GET https://api.open-meteo.com/v1/forecast?latitude=-33.45&longitude=-70.65&current_weather=true
```

#### Ejemplo de Response:

```json
{
  "latitude": -33.45,
  "longitude": -70.65,
  "generationtime_ms": 0.193,
  "utc_offset_seconds": -10800,
  "current_weather": {
    "temperature": 22.3,
    "windspeed": 3.7,
    "winddirection": 250,
    "weathercode": 1,
    "time": "2025-10-14T15:00"
  }
}
```

#### Manejo de Errores y Carga:

* Si la API no responde o devuelve un error, se muestra un mensaje de alerta usando Bootstrap.
* Durante la carga, se muestra un spinner o texto de *"Obteniendo clima..."*.
* Si los datos no están disponibles, se muestra *"No se pudieron obtener los datos del clima."*.

---

## Integración del Clima en la Aplicación

* En la vista de reserva de canchas, la aplicación consulta automáticamente el clima actual de la ubicación configurada.
* Los datos mostrados incluyen:

  * Temperatura actual (en °C)
  * Velocidad del viento (m/s)
  * Condición general (interpretada según código de clima de Open-Meteo)
* Esta información aparece en la parte superior de la vista, antes de confirmar la reserva.

### Ejemplo de visualización:

> Clima actual: 22°C, Viento 3.7 m/s.

---

## Aporte de la API al Proyecto

El uso de la API Open-Meteo aporta valor directo al usuario al permitirle conocer las condiciones climáticas actuales antes de reservar una cancha, mejorando la experiencia de uso y demostrando la integración de datos en tiempo real mediante una API REST.

---

## Uso de Inteligencia Artificial en el Desarrollo

Durante el desarrollo, se utilizó ChatGPT y Copilot (integrados en Visual Studio Code) como asistencia técnica para:

* Integrar correctamente Vue.js al proyecto existente.
* Resolver errores de selección de cancha y navegación.
* Agregar la funcionalidad de la API del clima (Open-Meteo) a la vista de reservas.
* Optimizar la validación de formularios y mejorar la retroalimentación visual.

---

## Ejecución del Proyecto

> *Actualmente el proyecto se ejecuta localmente.*
> *Puede abrirse mediante Live Server o configurarse para Vue CLI/Vite según las dependencias utilizadas.*

1. Clonar el repositorio:

```bash
git clone https://github.com/usuario/CasoCanchas-Vue.git
```

2. Abrir el proyecto en Visual Studio Code.
3. Ejecutar con Live Server o configurar entorno Vue si aplica.

---

## Autores

* **Pablo Sepúlveda Ulloa**
* **Nicolás Torres Díaz**
* **Benjamín Vivanco Guerra**
* **Bastián Oyanadel Pizarro**

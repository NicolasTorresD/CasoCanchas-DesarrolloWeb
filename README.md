# Proyecto: Reservas de Canchas con Vue.js y API del Clima (OpenWeatherMap)

> **Asignatura:** Desarrollo Web y Móvil
> **Integrantes:** Bastián Oyanadel, Pablo Sepúlveda, Nicolás Torres, Benjamín Vivanco
> **Framework:** Vue.js
> **API utilizada:** OpenWeatherMap (versión gratuita)
> **Apoyo de IA:** Desarrollo asistido por Inteligencia Artificial (ChatGPT / VSCode Copilot)

---

## Descripción General

Este proyecto extiende el proyecto original de reservas de canchas deportivas, integrando ahora el framework Vue.js para una mejor organización del frontend y el consumo de una API externa (OpenWeatherMap) que permite mostrar el clima actual en la vista de reservas.

El objetivo es ofrecer una experiencia más completa al usuario, mostrando las condiciones climáticas del día antes de confirmar la reserva, ayudando a tomar decisiones informadas según el clima.

---

## Tecnologías y Herramientas

| **Vue.js 3**            : Framework frontend para estructurar componentes y gestionar el estado de la app.                
| **Bootstrap 5**         : Framework de CSS para estilos responsivos, modales y componentes visuales.                      
| **OpenWeatherMap API**  : Fuente externa de datos meteorológicos en tiempo real.                                          
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

### API Utilizada: [OpenWeatherMap](https://openweathermap.org/api)

Versión gratuita - One Call API 3.0

#### Endpoint principal:

```bash
https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric&lang=es
```

#### Parámetros utilizados:

| Parámetro - Descripción                                
| --------- - ------------------------------------------ 
| `q`       : Nombre de la ciudad (ejemplo: Santiago)    
| `appid`   : Clave personal de la API (API Key)         
| `units`   : Unidades de medida (`metric` para Celsius) 
| `lang`    : Idioma de respuesta (`es` para español)    

#### Ejemplo de Request:

```bash
GET https://api.openweathermap.org/data/2.5/weather?q=Santiago&appid=TU_API_KEY&units=metric&lang=es
```

#### Ejemplo de Response:

```json
{
  "coord": { "lon": -70.65, "lat": -33.45 },
  "weather": [ { "main": "Clouds", "description": "nublado" } ],
  "main": { "temp": 21.4, "humidity": 68 },
  "wind": { "speed": 3.6 },
  "name": "Santiago"
}
```

#### Manejo de Errores y Carga:

* Si la API no responde o devuelve un error, se muestra un mensaje de alerta usando Bootstrap.
* Durante la carga, se muestra un spinner o texto de *"Obteniendo clima..."*.
* Si no se encuentra la ciudad, se muestra *"No se pudieron obtener los datos del clima."*.

---

## Integración del Clima en la Aplicación

* En la vista de reserva de canchas, la aplicación consulta automáticamente el clima actual de la ciudad configurada.
* Los datos mostrados incluyen:

  * **Temperatura actual** (en Celsius)
  * **Condición general** (nublado, soleado, lluvia, etc.)
  * **Humedad y viento**
* Esta información aparece en la parte superior de la vista, antes de confirmar la reserva.

### **Ejemplo de visualización:**

> Clima actual: 23°C, Cielo despejado, Humedad 60%, Viento 4 m/s.

---

## Aporte de la API al Proyecto

El uso de la API OpenWeatherMap aporta valor directo al usuario al permitirle conocer las condiciones climáticas antes de reservar una cancha, lo que mejora la experiencia de uso y simula una aplicación real conectada a datos externos.

Además, demuestra la capacidad del equipo para integrar datos en tiempo real mediante un servicio REST y aplicar buenas prácticas de desarrollo frontend.

---

## Uso de Inteligencia Artificial en el Desarrollo

Durante el desarrollo, se utilizó ChatGPT y Copilot (integrado en Visual Studio Code) como asistente para:

* Integrar correctamente el framework **Vue.js** al proyecto existente.
* Solucionar errores de selección de cancha y navegación entre vistas.
* Agregar la funcionalidad de la **API del clima (OpenWeatherMap)** a la vista de reservas.
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

- **Pablo Sepúlveda Ulloa**
- **Nicolás Torres Diaz**
- **Benjamín Vivanco Guerra**
- **Bastián Oyanadel Pizarro**

---

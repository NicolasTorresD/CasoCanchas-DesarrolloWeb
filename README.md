# 🏟️ Club Deportivo - Sistema de Reserva de Canchas# 🏟️ Club Deportivo - Sistema de Reserva de Canchas



Sistema web moderno para la gestión y reserva de canchas deportivas, desarrollado con Vue 3 y Vite. Permite a los usuarios reservar canchas, dejar reseñas y consultar información meteorológica para planificar mejor sus actividades deportivas.# Proyecto: Reservas de Canchas con Vue.js y API del Clima (Open-Meteo)



> **Asignatura:** Desarrollo Web y Móvil  Sistema web moderno para la gestión y reserva de canchas deportivas, desarrollado con Vue 3 y Vite. Permite a los usuarios reservar canchas, dejar reseñas y consultar información meteorológica para planificar mejor sus actividades deportivas.

> **Integrantes:** Bastián Oyanadel, Pablo Sepúlveda, Nicolás Torres, Benjamín Vivanco  

> **Framework:** Vue.js 3  ---

> **Apoyo de IA:** GitHub Copilot

![Vue.js](https://img.shields.io/badge/Vue.js-3.x-4FC08D?style=flat&logo=vue.js)

![Vue.js](https://img.shields.io/badge/Vue.js-3.x-4FC08D?style=flat&logo=vue.js)

![Vite](https://img.shields.io/badge/Vite-5.x-646CFF?style=flat&logo=vite)![Vite](https://img.shields.io/badge/Vite-5.x-646CFF?style=flat&logo=vite)

![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat&logo=bootstrap)

![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat&logo=bootstrap)

---

## Descripción General

## 📋 Tabla de Contenidos

Este proyecto extiende el prototipo original de reservas de canchas deportivas, integrando ahora el framework **Vue.js** para una mejor organización del frontend y el consumo de una API externa (Open-Meteo) que permite mostrar el clima actual en la vista de reservas.

- [Características](#-características)

- [Tecnologías](#️-tecnologías)## 📋 Tabla de Contenidos

- [API Externa - Open-Meteo](#-api-externa---open-meteo)

- [Instalación](#-instalación)El objetivo es ofrecer una experiencia más completa al usuario, mostrando las condiciones climáticas del día antes de confirmar la reserva, ayudando a tomar decisiones informadas según el clima.

- [Uso](#-uso)

- [Estructura del Proyecto](#-estructura-del-proyecto)- [Características](#-características)

- [Autores](#-autores)

- [Tecnologías](#️-tecnologías)---

---

- [API Externa - Open-Meteo](#-api-externa---open-meteo)

## ✨ Características

- [Instalación](#-instalación)## Tecnologías y Herramientas

### Funcionalidades Principales

- [Uso](#-uso)

🏟️ **Gestión de Canchas**

- Catálogo de canchas deportivas (Fútbol, Tenis, Pádel)- [Estructura del Proyecto](#-estructura-del-proyecto)| Herramienta             - Uso principal                                                                                   

- Filtrado por deporte y fecha

- Precios en pesos chilenos- [Contribuir](#-contribuir)| **Vue.js 3**            : Framework frontend para estructurar componentes y gestionar el estado de la app.                

- Sistema de calificaciones (1-5 estrellas)

| **Bootstrap 5**         : Framework de CSS para estilos responsivos, modales y componentes visuales.                      

📅 **Sistema de Reservas**

- Reservar canchas con nombre, fecha y hora## ✨ Características| **Open-Meteo API**      : Fuente externa de datos meteorológicos en tiempo real.                                          

- Ver todas las reservas activas

- Cancelación automática bloqueada 1 hora antes| **JavaScript (ES6)**    : Lógica funcional para manejo de datos y eventos.                                                

- Validación de fechas y horarios

### Funcionalidades Principales| **JSON / LocalStorage** : Persistencia local de reservas y canchas.                                                       

⭐ **Reseñas y Opiniones**

- Calificar canchas con estrellas| **Visual Studio Code**  : Entorno de desarrollo.                                                                          

- Dejar comentarios

- Ver reseñas por cancha (click en estrellas)- **📅 Gestión de Reservas**| **ChatGPT / Copilot**   : Asistente de programación para integración de Vue, resolución de errores y conexión con la API. 

- Promedio de calificaciones

  - Reservar canchas deportivas (Fútbol, Tenis, Pádel)

🌤️ **Información Meteorológica**

- Consulta del clima al hacer reserva  - Visualizar mis reservas activas---

- Pronóstico de 7 días para Santiago, Chile

- Datos históricos disponibles  - Cancelación automática deshabilitada 1 hora antes de la reserva

- Integración con API Open-Meteo

  - Validación de fechas y horarios## Estructura del Proyecto

---



## 🛠️ Tecnologías

- **🌤️ Información Meteorológica**```bash

| Tecnología | Uso |

|------------|-----|  - Consulta del clima en tiempo real para Santiago, ChileCasoCanchasVue/

| **Vue 3** | Framework JavaScript progresivo |

| **Vite** | Build tool y servidor de desarrollo |  - Pronóstico de 7 días├── app-vue.js              # Lógica principal con Vue.js y consumo de la API del clima

| **Bootstrap 5.3** | Framework CSS responsivo |

| **Font Awesome 6** | Biblioteca de iconos |  - Recomendaciones según condiciones climáticas├── app.js                  # Código base original sin framework

| **Open-Meteo API** | Datos meteorológicos gratuitos |

| **LocalStorage** | Persistencia de datos |  - Integración con API Open-Meteo├── public/



---│   ├── canchas.json        # Datos locales de canchas disponibles



## 🌐 API Externa - Open-Meteo- **⭐ Sistema de Reseñas**│   ├── reservas.json       # Datos de reservas iniciales



### Descripción  - Calificación de canchas (1-5 estrellas)│   ├── feedbacks.json      # Mensajes y alertas



Este proyecto consume la **Open-Meteo Weather Forecast API**, una API meteorológica gratuita que no requiere autenticación. Proporciona datos climáticos históricos, actuales y pronósticos.  - Comentarios y opiniones de usuarios│   └── imagenes/           # Recursos visuales



### Información Técnica  - Visualización de reseñas por cancha (clickeando en las estrellas)├── styles.css              # Estilos personalizados



#### Endpoint Base  - Promedio de calificaciones├── index.html              # Estructura principal de la aplicación

```

https://api.open-meteo.com/v1/forecast└── README.md               # Documentación del proyecto

```

- **🔍 Filtrado Inteligente**```

#### Autenticación

- ✅ No requiere API key  - Filtrar canchas por deporte

- ✅ Gratuita (10,000 requests/día)

- ✅ CORS habilitado  - Filtrar por fecha disponible---



#### Parámetros Utilizados  - Precios en pesos chilenos ($CLP)



| Parámetro | Valor | Descripción |## Explicación Técnica de la API

|-----------|-------|-------------|

| `latitude` | `-33.4489` | Latitud de Santiago, Chile |## 🛠️ Tecnologías

| `longitude` | `-70.6693` | Longitud de Santiago, Chile |

| `timezone` | `America/Santiago` | Zona horaria |### API Utilizada: [Open-Meteo](https://open-meteo.com/)

| `daily` | `temperature_2m_max,temperature_2m_min,precipitation_probability_max,weathercode` | Variables meteorológicas |

| `forecast_days` | `7` | Días de pronóstico |### Frontend Framework



#### Ejemplo de Request- **Vue 3** - Framework JavaScript progresivo#### Endpoint principal:



```javascript- **Vite** - Build tool y dev server de última generación

const url = 'https://api.open-meteo.com/v1/forecast?' +

  'latitude=-33.4489&' +- **Composition API** - API moderna de Vue para componentes```bash

  'longitude=-70.6693&' +

  'daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,weathercode&' +https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current_weather=true

  'timezone=America/Santiago&' +

  'forecast_days=7';### Estilos y UI```



const response = await fetch(url);- **Bootstrap 5.3** - Framework CSS responsivo

const data = await response.json();

```- **Font Awesome 6** - Iconos vectoriales#### **Parámetros utilizados:**



#### Ejemplo de Response- **CSS Custom** - Estilos personalizados con gradientes



```json| `latitude`        : Latitud de la ubicación (por ejemplo: -33.45 para Santiago).  

{

  "latitude": -33.4489,### Almacenamiento| `longitude`       : Longitud de la ubicación (por ejemplo: -70.65 para Santiago). 

  "longitude": -70.6693,

  "timezone": "America/Santiago",- **LocalStorage** - Persistencia de datos en el navegador| `current_weather` : Si se establece en `true`, devuelve el clima actual.          

  "daily": {

    "time": ["2025-10-17", "2025-10-18", "2025-10-19"],- **JSON** - Formato de datos para canchas, reservas y feedbacks

    "temperature_2m_max": [22.5, 24.1, 23.8],

    "temperature_2m_min": [12.3, 13.1, 12.9],#### **Ejemplo de Request:**

    "precipitation_probability_max": [10, 5, 0],

    "weathercode": [1, 0, 2]### API Externa

  }

}- **Open-Meteo Weather API** - Datos meteorológicos gratuitos y de código abierto```bash

```

GET https://api.open-meteo.com/v1/forecast?latitude=-33.45&longitude=-70.65&current_weather=true

#### Códigos de Clima (Weather Codes WMO)

## 🌐 API Externa - Open-Meteo```

| Código | Descripción | Icono |

|--------|-------------|-------|

| 0-1 | Despejado | ☀️ |

| 2-3 | Parcialmente nublado | ⛅ |### Descripción General#### Ejemplo de Response:

| 45-48 | Niebla | 🌫️ |

| 51-55 | Llovizna | 🌦️ |

| 61-65 | Lluvia | 🌧️ |

| 71-77 | Nieve | ❄️ |Este proyecto consume la **Open-Meteo Weather Forecast API**, una API meteorológica gratuita y de código abierto que no requiere autenticación mediante API key. Proporciona datos climáticos históricos, actuales y pronósticos.```json

| 80-82 | Chubascos | 🌧️ |

| 95-99 | Tormenta | ⛈️ |{



#### Manejo de Errores### Información Técnica  "latitude": -33.45,



El sistema maneja los siguientes errores:  "longitude": -70.65,



```javascript#### 🔗 Endpoint Base  "generationtime_ms": 0.193,

// 1. Validación de fecha

if (!fecha) {```  "utc_offset_seconds": -10800,

  return { success: false, error: 'Fecha no válida' };

}https://api.open-meteo.com/v1/forecast  "current_weather": {



// 2. Error de red```    "temperature": 22.3,

catch (error) {

  return { success: false, error: 'Error al conectar con el servicio' };    "windspeed": 3.7,

}

#### 🔐 Autenticación    "winddirection": 250,

// 3. Datos no disponibles

if (indice === -1) {- **Tipo:** No requiere autenticación    "weathercode": 1,

  return { success: false, error: 'No hay datos para esta fecha' };

}- **API Key:** No es necesaria    "time": "2025-10-14T15:00"

```

- **Límite de uso:** 10,000 requests/día (uso gratuito)  }

#### Integración en el Proyecto

- **CORS:** Habilitado para requests desde navegador}

**Configuración con variables de entorno:**

```

```javascript

// src/services/api.js#### 📍 Parámetros Principales

const CLIMA_CONFIG = {

  baseUrl: import.meta.env.VITE_CLIMA_API_URL,#### Manejo de Errores y Carga:

  latitude: import.meta.env.VITE_CLIMA_LATITUDE,

  longitude: import.meta.env.VITE_CLIMA_LONGITUDE,| Parámetro | Tipo | Descripción | Valor en Proyecto |

  timezone: import.meta.env.VITE_CLIMA_TIMEZONE

};|-----------|------|-------------|-------------------|* Si la API no responde o devuelve un error, se muestra un mensaje de alerta usando Bootstrap.

```

| `latitude` | float | Latitud de la ubicación | `-33.4489` (Santiago) |* Durante la carga, se muestra un spinner o texto de *"Obteniendo clima..."*.

**Archivo `.env`:**

| `longitude` | float | Longitud de la ubicación | `-70.6693` (Santiago) |* Si los datos no están disponibles, se muestra *"No se pudieron obtener los datos del clima."*.

```bash

VITE_CLIMA_API_URL=https://api.open-meteo.com/v1/forecast| `daily` | string | Variables meteorológicas diarias | `temperature_2m_max,temperature_2m_min,precipitation_probability_max,weathercode` |

VITE_CLIMA_LATITUDE=-33.4489

VITE_CLIMA_LONGITUDE=-70.6693| `timezone` | string | Zona horaria | `America/Santiago` |---

VITE_CLIMA_TIMEZONE=America/Santiago

```| `forecast_days` | int | Días de pronóstico (1-16) | `7` |



#### Funciones Disponibles## Integración del Clima en la Aplicación



```javascript#### 📤 Ejemplo de Request

// Obtener clima para una fecha

obtenerClima(fecha: string) → Promise<Object>* En la vista de reserva de canchas, la aplicación consulta automáticamente el clima actual de la ubicación configurada.



// Descripción en español del código**Pronóstico de 7 días para Santiago, Chile:*** Los datos mostrados incluyen:

obtenerDescripcionClima(codigo: number) → string



// Emoji según condición climática

obtenerIconoClima(codigo: number) → string```javascript  * Temperatura actual (en °C)

```

const url = 'https://api.open-meteo.com/v1/forecast?' +  * Velocidad del viento (m/s)

#### Aporte a la Experiencia de Usuario

  'latitude=-33.4489&' +  * Condición general (interpretada según código de clima de Open-Meteo)

1. **Al Reservar:** El usuario ve el pronóstico del clima antes de confirmar

2. **Toma de Decisiones:** Ayuda a elegir la mejor fecha según el clima  'longitude=-70.6693&' +* Esta información aparece en la parte superior de la vista, antes de confirmar la reserva.

3. **Visualización Clara:** Iconos y colores según las condiciones

  'daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,weathercode&' +

#### Consideraciones de CORS

  'timezone=America/Santiago&' +### Ejemplo de visualización:

Open-Meteo tiene CORS habilitado por defecto:

  'forecast_days=7';

```

Access-Control-Allow-Origin: *> Clima actual: 22°C, Viento 3.7 m/s.

Access-Control-Allow-Methods: GET

```const response = await fetch(url);



No requiere configuración adicional para funcionar desde el navegador.const data = await response.json();---



#### Límites y Restricciones```



| Límite | Valor |## Aporte de la API al Proyecto

|--------|-------|

| Requests/día | 10,000 (gratuito) |#### 📥 Ejemplo de Response

| Días de pronóstico | 16 días máximo |

| Datos históricos | Desde 1940 |El uso de la API Open-Meteo aporta valor directo al usuario al permitirle conocer las condiciones climáticas actuales antes de reservar una cancha, mejorando la experiencia de uso y demostrando la integración de datos en tiempo real mediante una API REST.

| Cobertura | Global |

```json

#### Documentación Oficial

{---

- **Docs:** [https://open-meteo.com/en/docs](https://open-meteo.com/en/docs)

- **Playground:** [https://open-meteo.com/en/docs#api-playground](https://open-meteo.com/en/docs#api-playground)  "latitude": -33.4489,

- **GitHub:** [https://github.com/open-meteo/open-meteo](https://github.com/open-meteo/open-meteo)

- **Licencia:** CC BY 4.0  "longitude": -70.6693,## Uso de Inteligencia Artificial en el Desarrollo



---  "timezone": "America/Santiago",



## 🚀 Instalación  "daily": {Durante el desarrollo, se utilizó ChatGPT y Copilot (integrados en Visual Studio Code) como asistencia técnica para:



### Prerrequisitos    "time": ["2025-10-17", "2025-10-18", "2025-10-19"],



- Node.js 18.x o superior    "temperature_2m_max": [22.5, 24.1, 23.8],* Integrar correctamente Vue.js al proyecto existente.

- npm 9.x o superior

    "temperature_2m_min": [12.3, 13.1, 12.9],* Resolver errores de selección de cancha y navegación.

### Pasos

    "precipitation_probability_max": [10, 5, 0],* Agregar la funcionalidad de la API del clima (Open-Meteo) a la vista de reservas.

1. **Clonar el repositorio**

   ```bash    "weathercode": [1, 0, 2]* Optimizar la validación de formularios y mejorar la retroalimentación visual.

   git clone https://github.com/NicolasTorresD/CasoCanchas-DesarrolloWeb.git

   cd CasoCanchas-DesarrolloWeb  }

   ```

}---

2. **Instalar dependencias**

   ```bash```

   npm install

   ```## Ejecución del Proyecto



3. **Configurar variables de entorno**#### 🌦️ Códigos de Clima (Weather Codes)

   ```bash

   cp .env.example .env> *Actualmente el proyecto se ejecuta localmente.*

   # La configuración por defecto funciona para Santiago, Chile

   ```| Código | Descripción | Icono |> *Puede abrirse mediante Live Server o configurarse para Vue CLI/Vite según las dependencias utilizadas.*



4. **Iniciar servidor de desarrollo**|--------|-------------|-------|

   ```bash

   npm run dev| `0-1` | Despejado | ☀️ |1. Clonar el repositorio:

   ```

| `2-3` | Parcialmente nublado | ⛅ |

5. **Abrir en navegador**

   ```| `45-48` | Niebla | 🌫️ |```bash

   http://localhost:5173

   ```| `51-55` | Llovizna | 🌦️ |git clone https://github.com/usuario/CasoCanchas-Vue.git



---| `61-65` | Lluvia | 🌧️ |```



## 📖 Uso| `71-77` | Nieve | ❄️ |



### Comandos| `80-82` | Chubascos | 🌧️ |2. Abrir el proyecto en Visual Studio Code.



```bash| `95-99` | Tormenta | ⛈️ |3. Ejecutar con Live Server o configurar entorno Vue si aplica.

npm run dev      # Desarrollo con hot-reload

npm run build    # Build de producción

npm run preview  # Previsualizar build

```#### ⚠️ Manejo de Errores---



### Flujo de Usuario



#### 1️⃣ Ver CanchasEl servicio implementa un manejo robusto de errores:## Autores

- Filtrar por deporte o fecha

- Ver precios y calificaciones

- Click en estrellas para ver reseñas

```javascript* **Pablo Sepúlveda Ulloa**

#### 2️⃣ Reservar

- Click en "Reservar"export async function obtenerClima(fecha) {* **Nicolás Torres Díaz**

- Completar nombre, fecha y hora

- Ver pronóstico del clima  try {* **Benjamín Vivanco Guerra**

- Confirmar reserva

    const response = await fetch(url);* **Bastián Oyanadel Pizarro**

#### 3️⃣ Mis Reservas

- Ver reservas activas    

- Cancelar (hasta 1 hora antes)    // Verificar estado HTTP

- Botón gris si ya no se puede cancelar    if (!response.ok) {

      throw new Error(`HTTP Error: ${response.status}`);

#### 4️⃣ Dejar Opinión    }

- Seleccionar cancha    

- Calificar con estrellas (1-5)    const data = await response.json();

- Escribir comentario    

- Enviar    // Verificar disponibilidad de datos para la fecha

    const indice = data.daily.time.indexOf(fecha);

---    if (indice === -1) {

      return {

## 📁 Estructura del Proyecto        success: false,

        error: 'No hay datos disponibles para esta fecha'

```      };

CasoCanchas-DesarrolloWeb/    }

│    

├── public/                   # Archivos estáticos    // Retornar datos exitosos

│   ├── canchas.json         # Datos de canchas    return {

│   ├── reservas.json        # Reservas iniciales      success: true,

│   ├── feedbacks.json       # Reseñas iniciales      data: {

│   └── imagenes/            # Imágenes        fecha: fechaBuscada,

│        temperaturaMax: data.daily.temperature_2m_max[indice],

├── src/        temperaturaMin: data.daily.temperature_2m_min[indice],

│   ├── components/          # Componentes Vue        probabilidadPrecipitacion: data.daily.precipitation_probability_max[indice],

│   │   ├── ListadoCanchas.vue        codigoClima: data.daily.weathercode[indice]

│   │   ├── MisReservas.vue      }

│   │   ├── FormularioFeedback.vue    };

│   │   └── ModalReserva.vue  } catch (error) {

│   │    console.error('Error obteniendo clima:', error);

│   ├── services/            # Lógica de negocio    return {

│   │   └── api.js          # Servicio de API      success: false,

│   │      error: 'Error al conectar con el servicio de clima'

│   ├── App.vue             # Componente raíz    };

│   └── main.js             # Punto de entrada  }

│}

├── .env                     # Variables de entorno (no en git)```

├── .env.example            # Plantilla de configuración

├── package.json            # Dependencias**Casos de error manejados:**

├── vite.config.js          # Configuración Vite1. ❌ Error de red / timeout

└── README.md               # Este archivo2. ❌ Respuesta HTTP no exitosa (4xx, 5xx)

```3. ❌ Datos no disponibles para la fecha solicitada

4. ❌ Error al parsear JSON

### Descripción de Componentes5. ❌ Parámetros inválidos



**ListadoCanchas.vue**#### 🎯 Casos de Uso en la Aplicación

- Lista de canchas con filtros

- Modal de reseñas1. **Consulta al Reservar**

- Calificaciones promedio   - El usuario selecciona una fecha para reservar

   - El sistema consulta automáticamente el clima previsto

**MisReservas.vue**   - Se muestra temperatura, probabilidad de lluvia y condiciones

- Gestión de reservas

- Validación de cancelación2. **Recomendaciones Inteligentes**

- Formato de fechas   - Si hay alta probabilidad de lluvia (>60%), se advierte al usuario

   - Se sugiere cambiar de fecha si las condiciones son desfavorables

**FormularioFeedback.vue**   - Icono visual del clima para referencia rápida

- Formulario de reseñas

- Selector de estrellas3. **Datos Históricos**

- Vista previa de opiniones   - Para fechas pasadas, muestra el clima real registrado

   - Útil para análisis y referencia

**ModalReserva.vue**

- Modal para reservar#### 🔄 Consideraciones de CORS

- Integración con clima

- ValidacionesLa API Open-Meteo tiene **CORS habilitado**, permitiendo requests directos desde el navegador sin necesidad de un proxy backend.



**api.js**```javascript

- Llamadas a API Open-Meteo// Headers permitidos por Open-Meteo

- Manejo de LocalStorageAccess-Control-Allow-Origin: *

- Funciones de helpersAccess-Control-Allow-Methods: GET

Access-Control-Allow-Headers: Content-Type

---```



## 👥 AutoresEsto permite llamadas directas desde el frontend sin configuración adicional.



- **Bastián Oyanadel**#### 📊 Límites y Restricciones

- **Pablo Sepúlveda**

- **Nicolás Torres** - [GitHub](https://github.com/NicolasTorresD)| Límite | Valor | Notas |

- **Benjamín Vivanco**|--------|-------|-------|

| Requests/día | 10,000 | Uso gratuito, suficiente para proyectos educativos |

---| Requests/segundo | Sin límite estricto | ~600 req/s |

| Días de pronóstico | 16 días | Máximo hacia el futuro |

## 📄 Licencia| Datos históricos | Desde 1940 | Dependiendo de la ubicación |

| Ubicaciones | Ilimitadas | Cobertura global |

Este proyecto es un trabajo académico para la asignatura de Desarrollo Web y Móvil.| Caching recomendado | 15 minutos | Para optimizar rendimiento |



---#### 🔗 Documentación y Recursos



## 🙏 Agradecimientos- **Documentación oficial:** [https://open-meteo.com/en/docs](https://open-meteo.com/en/docs)

- **API Playground:** [https://open-meteo.com/en/docs#api-playground](https://open-meteo.com/en/docs#api-playground)

- [Vue.js](https://vuejs.org/)- **GitHub:** [https://github.com/open-meteo/open-meteo](https://github.com/open-meteo/open-meteo)

- [Vite](https://vitejs.dev/)- **Licencia:** CC BY 4.0 (Atribución requerida)

- [Bootstrap](https://getbootstrap.com/)

- [Open-Meteo](https://open-meteo.com/)### Integración en el Proyecto

- [Font Awesome](https://fontawesome.com/)

- GitHub Copilot#### Configuración Centralizada



---La API está integrada mediante un servicio dedicado en `src/services/api.js` utilizando variables de entorno:



## ✅ Cumplimiento de Requisitos```javascript

// src/services/api.js

| Requisito | Estado |const CLIMA_CONFIG = {

|-----------|--------|  baseUrl: import.meta.env.VITE_CLIMA_API_URL || 'https://api.open-meteo.com/v1/forecast',

| Framework Frontend | ✅ Vue 3 |  latitude: import.meta.env.VITE_CLIMA_LATITUDE || -33.4489,

| API Externa | ✅ Open-Meteo |  longitude: import.meta.env.VITE_CLIMA_LONGITUDE || -70.6693,

| Documentación Técnica API | ✅ Completa |  timezone: import.meta.env.VITE_CLIMA_TIMEZONE || 'America/Santiago'

| Aporte a UX | ✅ Clima al reservar |};

| Buenas Prácticas | ✅ Componentes + servicios |```

| README completo | ✅ Este documento |

#### Variables de Entorno

---

En el archivo `.env`:

**Desarrollado con ❤️ usando Vue.js**

```bash
# API de Clima - Open Meteo
VITE_CLIMA_API_URL=https://api.open-meteo.com/v1/forecast
VITE_CLIMA_LATITUDE=-33.4489
VITE_CLIMA_LONGITUDE=-70.6693
VITE_CLIMA_TIMEZONE=America/Santiago
```

#### Funciones Disponibles

El servicio exporta las siguientes funciones:

```javascript
// Obtener datos del clima para una fecha específica
obtenerClima(fecha: string) → Promise<Object>

// Obtener descripción en español del código de clima
obtenerDescripcionClima(codigo: number) → string

// Obtener emoji/icono apropiado para el clima
obtenerIconoClima(codigo: number) → string
```

**Ventajas de usar Open-Meteo:**
- ✅ **Gratuita:** No requiere tarjeta de crédito ni API key
- ✅ **Sin autenticación:** Implementación simple y rápida
- ✅ **CORS habilitado:** Funciona directamente desde el navegador
- ✅ **Datos precisos:** Modelos meteorológicos de alta calidad
- ✅ **Código abierto:** Transparente y confiable
- ✅ **Cobertura global:** Cualquier ubicación del mundo
- ✅ **Documentación excelente:** Fácil de entender e implementar
- ✅ **Actualizaciones frecuentes:** Datos actualizados cada hora

## 🚀 Instalación

### Prerrequisitos

- **Node.js** 18.x o superior
- **npm** 9.x o superior (viene con Node.js)
- Navegador web moderno (Chrome, Firefox, Edge, Safari)

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/NicolasTorresD/CasoCanchas-DesarrolloWeb.git
   cd CasoCanchas-DesarrolloWeb
   ```

2. **Instalar dependencias**
   ```bash
   npm install
   ```

3. **Configurar variables de entorno**
   ```bash
   # Copiar el archivo de ejemplo
   cp .env.example .env
   
   # La configuración por defecto ya funciona para Santiago, Chile
   # Editar .env solo si deseas cambiar la ubicación
   ```

4. **Iniciar el servidor de desarrollo**
   ```bash
   npm run dev
   ```

5. **Abrir en el navegador**
   ```
   http://localhost:5173
   ```

## 📖 Uso

### Comandos Disponibles

```bash
# Desarrollo - Inicia servidor con hot-reload
npm run dev

# Compilación - Genera build de producción en /dist
npm run build

# Preview - Previsualiza el build de producción
npm run preview
```

### Flujo de Usuario

#### 1. Ver Canchas Disponibles
- Navega a "Canchas Disponibles" (vista por defecto)
- Usa los filtros para buscar:
  - **Por deporte:** Fútbol, Tenis, Pádel
  - **Por fecha:** Selecciona una fecha específica
- Revisa información de cada cancha:
  - 📸 Imagen
  - ⚽ Tipo de deporte
  - 💰 Precio por hora (en $CLP)
  - ⭐ Calificación promedio
  - 🔍 Click en las estrellas para ver reseñas detalladas

#### 2. Hacer una Reserva
- Click en **"Reservar"** en la cancha deseada
- Completa el formulario en el modal:
  - 👤 Tu nombre
  - 📅 Fecha de la reserva
  - ⏰ Hora de inicio
- Visualiza el **clima previsto** para la fecha seleccionada:
  - 🌡️ Temperatura máxima y mínima
  - 🌧️ Probabilidad de precipitación
  - 🌤️ Condiciones generales con icono
- Click en **"Confirmar Reserva"**

#### 3. Gestionar Mis Reservas
- Ve a la sección **"Mis Reservas"**
- Visualiza todas tus reservas activas:
  - Información completa de cada reserva
  - Fecha, hora y cancha
- **Cancelar reservas:**
  - ✅ **Botón rojo:** Puedes cancelar (más de 1 hora antes)
  - ❌ **Botón gris:** No se puede cancelar (menos de 1 hora o fecha pasada)

#### 4. Dejar Reseñas
- Accede a **"Dejar Opinión"**
- Completa el formulario:
  - 👤 Tu nombre
  - 🏟️ Selecciona la cancha
  - ⭐ Califica con estrellas (1-5)
  - 💬 Escribe tu comentario
- Las reseñas se guardan y aparecen inmediatamente

#### 5. Ver Reseñas de una Cancha
- En la lista de canchas, **click en las estrellas** de cualquier cancha
- Se abre un modal con:
  - Calificación promedio grande
  - Número total de reseñas
  - Lista completa de comentarios con:
    - Nombre del usuario
    - Fecha de la reseña
    - Calificación individual
    - Comentario completo

## 📁 Estructura del Proyecto

```
CasoCanchas-DesarrolloWeb/
│
├── public/                    # Archivos estáticos públicos
│   ├── canchas.json          # Base de datos de canchas
│   ├── reservas.json         # Reservas de ejemplo
│   ├── feedbacks.json        # Reseñas de ejemplo
│   └── imagenes/             # Imágenes de canchas
│       ├── chancha-futbol.png
│       ├── cancha-tenis.png
│       └── cancha-padel.png
│
├── src/
│   ├── components/           # Componentes Vue reutilizables
│   │   ├── ListadoCanchas.vue       # Lista + filtros + reseñas
│   │   ├── MisReservas.vue          # Gestión de reservas
│   │   ├── FormularioFeedback.vue   # Formulario de opiniones
│   │   └── ModalReserva.vue         # Modal para crear reserva
│   │
│   ├── services/             # Capa de servicios
│   │   └── api.js           # API de clima + manejo de datos
│   │
│   ├── App.vue              # Componente raíz de la aplicación
│   ├── main.js              # Punto de entrada de Vue
│   └── styles.css           # Estilos globales personalizados
│
├── .env                      # Variables de entorno (NO en git)
├── .env.example             # Ejemplo de configuración
├── .gitignore               # Archivos ignorados por Git
├── index.html               # HTML principal
├── package.json             # Dependencias y scripts npm
├── vite.config.js           # Configuración de Vite
└── README.md                # Documentación del proyecto
```

### Descripción de Componentes

#### `ListadoCanchas.vue`
- Muestra grid de canchas disponibles
- Implementa filtros por deporte y fecha
- Calcula y muestra calificaciones promedio
- Modal de reseñas clickeable en estrellas
- Formatea precios en pesos chilenos

#### `MisReservas.vue`
- Lista de reservas del usuario
- Validación de tiempo para cancelación
- Botones dinámicos según disponibilidad
- Formato de fechas legible

#### `FormularioFeedback.vue`
- Formulario interactivo con estrellas
- Selector de cancha
- Vista previa de reseñas recientes
- Validación de campos

#### `ModalReserva.vue`
- Modal Bootstrap para crear reservas
- Integración con API de clima
- Validaciones de fecha/hora
- Feedback visual del clima

#### `api.js` (Servicio)
- Centraliza todas las llamadas a APIs
- Manejo de errores consistente
- Funciones de helpers (clima, storage)
- Configuración mediante variables de entorno

## 🤝 Contribuir

Las contribuciones son bienvenidas. Para cambios importantes:

1. **Fork** el proyecto
2. Crea una rama para tu feature
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus cambios y **commit**
   ```bash
   git commit -m 'Add: descripción de la funcionalidad'
   ```
4. **Push** a la rama
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
5. Abre un **Pull Request**

### Convenciones de Commits

- `Add:` Nueva funcionalidad
- `Fix:` Corrección de bugs
- `Update:` Actualización de código existente
- `Docs:` Cambios en documentación
- `Style:` Cambios de formato (sin afectar lógica)
- `Refactor:` Refactorización de código

## 👥 Autores

- **Bastián Oyanadel**
- **Pablo Sepúlveda**
- **Nicolás Torres** - [NicolasTorresD](https://github.com/NicolasTorresD)
- **Benjamín Vivanco**

## 📄 Licencia

Este proyecto es un trabajo académico para la asignatura de Desarrollo Web y Móvil.

## 🙏 Agradecimientos

- [Vue.js](https://vuejs.org/) - Framework JavaScript progresivo
- [Vite](https://vitejs.dev/) - Build tool ultra rápido
- [Bootstrap](https://getbootstrap.com/) - Framework CSS responsivo
- [Open-Meteo](https://open-meteo.com/) - API meteorológica gratuita
- [Font Awesome](https://fontawesome.com/) - Biblioteca de iconos
- GitHub Copilot - Asistente de desarrollo con IA

---

## 📊 Estado del Proyecto

✅ **Requisitos Cumplidos:**
- ✅ Framework Frontend: Vue 3
- ✅ API Externa: Open-Meteo (clima)
- ✅ Documentación técnica de API
- ✅ Experiencia de usuario mejorada con clima
- ✅ Buenas prácticas: componentes, servicios, variables de entorno
- ✅ README completo con instrucciones

⭐ **Si te gusta el proyecto, dale una estrella en GitHub**

📧 **Contacto:** [GitHub Issues](https://github.com/NicolasTorresD/CasoCanchas-DesarrolloWeb/issues)

---

**Desarrollado con ❤️ usando Vue.js y asistencia de IA**

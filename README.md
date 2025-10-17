# 🏟️ Club Deportivo - Sistema de Reserva de Canchas

# Proyecto: Reservas de Canchas con Vue.js y API del Clima (Open-Meteo)

Sistema web moderno para la gestión y reserva de canchas deportivas, desarrollado con Vue 3 y Vite. Permite a los usuarios reservar canchas, dejar reseñas y consultar información meteorológica para planificar mejor sus actividades deportivas.

> **Integrantes:** Bastián Oyanadel, Pablo Sepúlveda, Nicolás Torres, Benjamín Vivanco

> **Asignatura:** Desarrollo Web y Móvil

> **Framework:** Vue.js

> **Integrantes:** Bastián Oyanadel, Pablo Sepúlveda, Nicolás Torres, Benjamín Vivanco

> **API utilizada:** Open-Meteo (versión gratuita)

---

![Vue.js](https://img.shields.io/badge/Vue.js-3.x-4FC08D?style=flat&logo=vue.js)

![Vite](https://img.shields.io/badge/Vite-5.x-646CFF?style=flat&logo=vite)

![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat&logo=bootstrap)

## Descripción General

Este proyecto extiende el prototipo original de reservas de canchas deportivas, integrando ahora el framework **Vue.js** para una mejor organización del frontend y el consumo de una API externa (Open-Meteo) que permite mostrar el clima actual en la vista de reservas.

## 📋 Tabla de Contenidos

El objetivo es ofrecer una experiencia más completa al usuario, mostrando las condiciones climáticas del día antes de confirmar la reserva, ayudando a tomar decisiones informadas según el clima.

- [Características](#-características)

- [Tecnologías](#️-tecnologías)---

- [API Externa - Open-Meteo](#-api-externa---open-meteo)

- [Instalación](#-instalación)## Tecnologías y Herramientas

- [Uso](#-uso)

- [Estructura del Proyecto](#-estructura-del-proyecto)| Herramienta             - Uso principal                                                                                   

- [Contribuir](#-contribuir)| **Vue.js 3**            : Framework frontend para estructurar componentes y gestionar el estado de la app.                

| **Bootstrap 5**         : Framework de CSS para estilos responsivos, modales y componentes visuales.                      

## ✨ Características| **Open-Meteo API**      : Fuente externa de datos meteorológicos en tiempo real.                                          

| **JavaScript (ES6)**    : Lógica funcional para manejo de datos y eventos.                                                

### Funcionalidades Principales| **JSON / LocalStorage** : Persistencia local de reservas y canchas.                                                       

| **Visual Studio Code**  : Entorno de desarrollo.                                                                          

- **📅 Gestión de Reservas**| **ChatGPT / Copilot**   : Asistente de programación para integración de Vue, resolución de errores y conexión con la API. 

  - Reservar canchas deportivas (Fútbol, Tenis, Pádel)

  - Visualizar mis reservas activas---

  - Cancelación automática deshabilitada 1 hora antes de la reserva

  - Validación de fechas y horarios## Estructura del Proyecto



- **🌤️ Información Meteorológica**```bash

  - Consulta del clima en tiempo real para Santiago, ChileCasoCanchasVue/

  - Pronóstico de 7 días├── app-vue.js              # Lógica principal con Vue.js y consumo de la API del clima

  - Recomendaciones según condiciones climáticas├── app.js                  # Código base original sin framework

  - Integración con API Open-Meteo├── public/

│   ├── canchas.json        # Datos locales de canchas disponibles

- **⭐ Sistema de Reseñas**│   ├── reservas.json       # Datos de reservas iniciales

  - Calificación de canchas (1-5 estrellas)│   ├── feedbacks.json      # Mensajes y alertas

  - Comentarios y opiniones de usuarios│   └── imagenes/           # Recursos visuales

  - Visualización de reseñas por cancha (clickeando en las estrellas)├── styles.css              # Estilos personalizados

  - Promedio de calificaciones├── index.html              # Estructura principal de la aplicación

└── README.md               # Documentación del proyecto

- **🔍 Filtrado Inteligente**```

  - Filtrar canchas por deporte

  - Filtrar por fecha disponible---

  - Precios en pesos chilenos ($CLP)

## Explicación Técnica de la API

## 🛠️ Tecnologías

### API Utilizada: [Open-Meteo](https://open-meteo.com/)

### Frontend Framework

- **Vue 3** - Framework JavaScript progresivo#### Endpoint principal:

- **Vite** - Build tool y dev server de última generación

- **Composition API** - API moderna de Vue para componentes```bash

https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&current_weather=true

### Estilos y UI```

- **Bootstrap 5.3** - Framework CSS responsivo

- **Font Awesome 6** - Iconos vectoriales#### **Parámetros utilizados:**

- **CSS Custom** - Estilos personalizados con gradientes

| `latitude`        : Latitud de la ubicación (por ejemplo: -33.45 para Santiago).  

### Almacenamiento| `longitude`       : Longitud de la ubicación (por ejemplo: -70.65 para Santiago). 

- **LocalStorage** - Persistencia de datos en el navegador| `current_weather` : Si se establece en `true`, devuelve el clima actual.          

- **JSON** - Formato de datos para canchas, reservas y feedbacks

#### **Ejemplo de Request:**

### API Externa

- **Open-Meteo Weather API** - Datos meteorológicos gratuitos y de código abierto```bash

GET https://api.open-meteo.com/v1/forecast?latitude=-33.45&longitude=-70.65&current_weather=true

## 🌐 API Externa - Open-Meteo```



### Descripción General#### Ejemplo de Response:



Este proyecto consume la **Open-Meteo Weather Forecast API**, una API meteorológica gratuita y de código abierto que no requiere autenticación mediante API key. Proporciona datos climáticos históricos, actuales y pronósticos.```json

{

### Información Técnica  "latitude": -33.45,

  "longitude": -70.65,

#### 🔗 Endpoint Base  "generationtime_ms": 0.193,

```  "utc_offset_seconds": -10800,

https://api.open-meteo.com/v1/forecast  "current_weather": {

```    "temperature": 22.3,

    "windspeed": 3.7,

#### 🔐 Autenticación    "winddirection": 250,

- **Tipo:** No requiere autenticación    "weathercode": 1,

- **API Key:** No es necesaria    "time": "2025-10-14T15:00"

- **Límite de uso:** 10,000 requests/día (uso gratuito)  }

- **CORS:** Habilitado para requests desde navegador}

```

#### 📍 Parámetros Principales

#### Manejo de Errores y Carga:

| Parámetro | Tipo | Descripción | Valor en Proyecto |

|-----------|------|-------------|-------------------|* Si la API no responde o devuelve un error, se muestra un mensaje de alerta usando Bootstrap.

| `latitude` | float | Latitud de la ubicación | `-33.4489` (Santiago) |* Durante la carga, se muestra un spinner o texto de *"Obteniendo clima..."*.

| `longitude` | float | Longitud de la ubicación | `-70.6693` (Santiago) |* Si los datos no están disponibles, se muestra *"No se pudieron obtener los datos del clima."*.

| `daily` | string | Variables meteorológicas diarias | `temperature_2m_max,temperature_2m_min,precipitation_probability_max,weathercode` |

| `timezone` | string | Zona horaria | `America/Santiago` |---

| `forecast_days` | int | Días de pronóstico (1-16) | `7` |

## Integración del Clima en la Aplicación

#### 📤 Ejemplo de Request

* En la vista de reserva de canchas, la aplicación consulta automáticamente el clima actual de la ubicación configurada.

**Pronóstico de 7 días para Santiago, Chile:*** Los datos mostrados incluyen:



```javascript  * Temperatura actual (en °C)

const url = 'https://api.open-meteo.com/v1/forecast?' +  * Velocidad del viento (m/s)

  'latitude=-33.4489&' +  * Condición general (interpretada según código de clima de Open-Meteo)

  'longitude=-70.6693&' +* Esta información aparece en la parte superior de la vista, antes de confirmar la reserva.

  'daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,weathercode&' +

  'timezone=America/Santiago&' +### Ejemplo de visualización:

  'forecast_days=7';

> Clima actual: 22°C, Viento 3.7 m/s.

const response = await fetch(url);

const data = await response.json();---

```

## Aporte de la API al Proyecto

#### 📥 Ejemplo de Response

El uso de la API Open-Meteo aporta valor directo al usuario al permitirle conocer las condiciones climáticas actuales antes de reservar una cancha, mejorando la experiencia de uso y demostrando la integración de datos en tiempo real mediante una API REST.

```json

{---

  "latitude": -33.4489,

  "longitude": -70.6693,## Uso de Inteligencia Artificial en el Desarrollo

  "timezone": "America/Santiago",

  "daily": {Durante el desarrollo, se utilizó ChatGPT y Copilot (integrados en Visual Studio Code) como asistencia técnica para:

    "time": ["2025-10-17", "2025-10-18", "2025-10-19"],

    "temperature_2m_max": [22.5, 24.1, 23.8],* Integrar correctamente Vue.js al proyecto existente.

    "temperature_2m_min": [12.3, 13.1, 12.9],* Resolver errores de selección de cancha y navegación.

    "precipitation_probability_max": [10, 5, 0],* Agregar la funcionalidad de la API del clima (Open-Meteo) a la vista de reservas.

    "weathercode": [1, 0, 2]* Optimizar la validación de formularios y mejorar la retroalimentación visual.

  }

}---

```

## Ejecución del Proyecto

#### 🌦️ Códigos de Clima (Weather Codes)

> *Actualmente el proyecto se ejecuta localmente.*

| Código | Descripción | Icono |> *Puede abrirse mediante Live Server o configurarse para Vue CLI/Vite según las dependencias utilizadas.*

|--------|-------------|-------|

| `0-1` | Despejado | ☀️ |1. Clonar el repositorio:

| `2-3` | Parcialmente nublado | ⛅ |

| `45-48` | Niebla | 🌫️ |```bash

| `51-55` | Llovizna | 🌦️ |git clone https://github.com/usuario/CasoCanchas-Vue.git

| `61-65` | Lluvia | 🌧️ |```

| `71-77` | Nieve | ❄️ |

| `80-82` | Chubascos | 🌧️ |2. Abrir el proyecto en Visual Studio Code.

| `95-99` | Tormenta | ⛈️ |3. Ejecutar con Live Server o configurar entorno Vue si aplica.



#### ⚠️ Manejo de Errores---



El servicio implementa un manejo robusto de errores:## Autores



```javascript* **Pablo Sepúlveda Ulloa**

export async function obtenerClima(fecha) {* **Nicolás Torres Díaz**

  try {* **Benjamín Vivanco Guerra**

    const response = await fetch(url);* **Bastián Oyanadel Pizarro**

    
    // Verificar estado HTTP
    if (!response.ok) {
      throw new Error(`HTTP Error: ${response.status}`);
    }
    
    const data = await response.json();
    
    // Verificar disponibilidad de datos para la fecha
    const indice = data.daily.time.indexOf(fecha);
    if (indice === -1) {
      return {
        success: false,
        error: 'No hay datos disponibles para esta fecha'
      };
    }
    
    // Retornar datos exitosos
    return {
      success: true,
      data: {
        fecha: fechaBuscada,
        temperaturaMax: data.daily.temperature_2m_max[indice],
        temperaturaMin: data.daily.temperature_2m_min[indice],
        probabilidadPrecipitacion: data.daily.precipitation_probability_max[indice],
        codigoClima: data.daily.weathercode[indice]
      }
    };
  } catch (error) {
    console.error('Error obteniendo clima:', error);
    return {
      success: false,
      error: 'Error al conectar con el servicio de clima'
    };
  }
}
```

**Casos de error manejados:**
1. ❌ Error de red / timeout
2. ❌ Respuesta HTTP no exitosa (4xx, 5xx)
3. ❌ Datos no disponibles para la fecha solicitada
4. ❌ Error al parsear JSON
5. ❌ Parámetros inválidos

#### 🎯 Casos de Uso en la Aplicación

1. **Consulta al Reservar**
   - El usuario selecciona una fecha para reservar
   - El sistema consulta automáticamente el clima previsto
   - Se muestra temperatura, probabilidad de lluvia y condiciones

2. **Recomendaciones Inteligentes**
   - Si hay alta probabilidad de lluvia (>60%), se advierte al usuario
   - Se sugiere cambiar de fecha si las condiciones son desfavorables
   - Icono visual del clima para referencia rápida

3. **Datos Históricos**
   - Para fechas pasadas, muestra el clima real registrado
   - Útil para análisis y referencia

#### 🔄 Consideraciones de CORS

La API Open-Meteo tiene **CORS habilitado**, permitiendo requests directos desde el navegador sin necesidad de un proxy backend.

```javascript
// Headers permitidos por Open-Meteo
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET
Access-Control-Allow-Headers: Content-Type
```

Esto permite llamadas directas desde el frontend sin configuración adicional.

#### 📊 Límites y Restricciones

| Límite | Valor | Notas |
|--------|-------|-------|
| Requests/día | 10,000 | Uso gratuito, suficiente para proyectos educativos |
| Requests/segundo | Sin límite estricto | ~600 req/s |
| Días de pronóstico | 16 días | Máximo hacia el futuro |
| Datos históricos | Desde 1940 | Dependiendo de la ubicación |
| Ubicaciones | Ilimitadas | Cobertura global |
| Caching recomendado | 15 minutos | Para optimizar rendimiento |

#### 🔗 Documentación y Recursos

- **Documentación oficial:** [https://open-meteo.com/en/docs](https://open-meteo.com/en/docs)
- **API Playground:** [https://open-meteo.com/en/docs#api-playground](https://open-meteo.com/en/docs#api-playground)
- **GitHub:** [https://github.com/open-meteo/open-meteo](https://github.com/open-meteo/open-meteo)
- **Licencia:** CC BY 4.0 (Atribución requerida)

### Integración en el Proyecto

#### Configuración Centralizada

La API está integrada mediante un servicio dedicado en `src/services/api.js` utilizando variables de entorno:

```javascript
// src/services/api.js
const CLIMA_CONFIG = {
  baseUrl: import.meta.env.VITE_CLIMA_API_URL || 'https://api.open-meteo.com/v1/forecast',
  latitude: import.meta.env.VITE_CLIMA_LATITUDE || -33.4489,
  longitude: import.meta.env.VITE_CLIMA_LONGITUDE || -70.6693,
  timezone: import.meta.env.VITE_CLIMA_TIMEZONE || 'America/Santiago'
};
```

#### Variables de Entorno

En el archivo `.env`:

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

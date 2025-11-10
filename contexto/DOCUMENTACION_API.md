# 📡 Documentación Técnica - API Open-Meteo

## Resumen Ejecutivo

Este documento detalla la implementación y uso de la API Open-Meteo en el proyecto Club Deportivo para proporcionar información meteorológica en tiempo real y pronósticos.

---

## 🎯 Propósito

La integración de la API Open-Meteo permite:
- Mostrar condiciones climáticas al momento de reservar
- Ayudar a los usuarios a tomar decisiones informadas
- Mejorar la experiencia de usuario con datos relevantes
- Prevenir reservas en condiciones climáticas adversas

---

## 🔧 Configuración Técnica

### Variables de Entorno

```bash
# .env
VITE_CLIMA_API_URL=https://api.open-meteo.com/v1/forecast
VITE_CLIMA_LATITUDE=-33.4489    # Santiago, Chile
VITE_CLIMA_LONGITUDE=-70.6693    # Santiago, Chile
VITE_CLIMA_TIMEZONE=America/Santiago
```

### Inicialización en el Código

```javascript
// src/services/api.js
const CLIMA_CONFIG = {
  baseUrl: import.meta.env.VITE_CLIMA_API_URL,
  latitude: import.meta.env.VITE_CLIMA_LATITUDE,
  longitude: import.meta.env.VITE_CLIMA_LONGITUDE,
  timezone: import.meta.env.VITE_CLIMA_TIMEZONE
};
```

---

## 📋 Endpoints Utilizados

### Pronóstico Futuro (Forecast)

**URL:** `GET https://api.open-meteo.com/v1/forecast`

**Parámetros:**
```javascript
{
  latitude: -33.4489,
  longitude: -70.6693,
  daily: [
    'temperature_2m_max',
    'temperature_2m_min',
    'precipitation_probability_max',
    'weathercode'
  ],
  timezone: 'America/Santiago',
  forecast_days: 7
}
```

**Ejemplo de URL completa:**
```
https://api.open-meteo.com/v1/forecast?latitude=-33.4489&longitude=-70.6693&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,weathercode&timezone=America/Santiago&forecast_days=7
```

### Datos Históricos (Past Days)

**URL:** `GET https://api.open-meteo.com/v1/forecast`

**Parámetros:**
```javascript
{
  latitude: -33.4489,
  longitude: -70.6693,
  daily: [
    'temperature_2m_max',
    'temperature_2m_min',
    'weathercode'
  ],
  timezone: 'America/Santiago',
  past_days: 7
}
```

---

## 📊 Estructura de Respuesta

### Response Exitoso

```json
{
  "latitude": -33.4489,
  "longitude": -70.6693,
  "generationtime_ms": 0.8299350738525391,
  "utc_offset_seconds": -10800,
  "timezone": "America/Santiago",
  "timezone_abbreviation": "-03",
  "elevation": 570.0,
  "daily_units": {
    "time": "iso8601",
    "temperature_2m_max": "°C",
    "temperature_2m_min": "°C",
    "precipitation_probability_max": "%",
    "weathercode": "wmo code"
  },
  "daily": {
    "time": [
      "2025-10-17",
      "2025-10-18",
      "2025-10-19",
      "2025-10-20",
      "2025-10-21",
      "2025-10-22",
      "2025-10-23"
    ],
    "temperature_2m_max": [22.5, 24.1, 23.8, 21.2, 20.5, 22.8, 25.3],
    "temperature_2m_min": [12.3, 13.1, 12.9, 11.5, 10.8, 12.2, 13.5],
    "precipitation_probability_max": [10, 5, 0, 20, 45, 15, 5],
    "weathercode": [1, 0, 2, 3, 61, 2, 1]
  }
}
```

### Campos Importantes

| Campo | Tipo | Descripción | Ejemplo |
|-------|------|-------------|---------|
| `daily.time` | array[string] | Fechas en formato ISO | `["2025-10-17"]` |
| `daily.temperature_2m_max` | array[float] | Temperatura máxima en °C | `[22.5]` |
| `daily.temperature_2m_min` | array[float] | Temperatura mínima en °C | `[12.3]` |
| `daily.precipitation_probability_max` | array[int] | Probabilidad de lluvia (%) | `[10]` |
| `daily.weathercode` | array[int] | Código WMO del clima | `[1]` |

---

## 🔢 Códigos de Clima WMO

### Tabla Completa de Weather Codes

| Código | Descripción ES | Descripción EN | Icono | Categoría |
|--------|---------------|----------------|-------|-----------|
| 0 | Despejado | Clear sky | ☀️ | Bueno |
| 1 | Principalmente despejado | Mainly clear | ☀️ | Bueno |
| 2 | Parcialmente nublado | Partly cloudy | ⛅ | Moderado |
| 3 | Nublado | Overcast | ☁️ | Moderado |
| 45 | Niebla | Fog | 🌫️ | Moderado |
| 48 | Niebla con escarcha | Depositing rime fog | 🌫️ | Moderado |
| 51 | Llovizna ligera | Light drizzle | 🌦️ | Moderado |
| 53 | Llovizna moderada | Moderate drizzle | 🌦️ | Moderado |
| 55 | Llovizna intensa | Dense drizzle | 🌦️ | Malo |
| 61 | Lluvia ligera | Slight rain | 🌧️ | Moderado |
| 63 | Lluvia moderada | Moderate rain | 🌧️ | Malo |
| 65 | Lluvia intensa | Heavy rain | 🌧️ | Malo |
| 71 | Nevada ligera | Slight snow fall | ❄️ | Moderado |
| 73 | Nevada moderada | Moderate snow fall | ❄️ | Malo |
| 75 | Nevada intensa | Heavy snow fall | ❄️ | Malo |
| 77 | Granizo | Snow grains | ❄️ | Malo |
| 80 | Chubascos ligeros | Slight rain showers | 🌧️ | Moderado |
| 81 | Chubascos moderados | Moderate rain showers | 🌧️ | Malo |
| 82 | Chubascos intensos | Violent rain showers | 🌧️ | Malo |
| 85 | Nevadas ligeras | Slight snow showers | ❄️ | Moderado |
| 86 | Nevadas intensas | Heavy snow showers | ❄️ | Malo |
| 95 | Tormenta | Thunderstorm | ⛈️ | Malo |
| 96 | Tormenta con granizo ligero | Thunderstorm with slight hail | ⛈️ | Malo |
| 99 | Tormenta con granizo intenso | Thunderstorm with heavy hail | ⛈️ | Malo |

---

## 💻 Implementación en el Código

### Función Principal: `obtenerClima()`

```javascript
export async function obtenerClima(fecha) {
  // 1. Validación de parámetros
  if (!fecha) {
    return {
      success: false,
      error: 'Fecha no válida'
    };
  }

  // 2. Determinar si es fecha futura o pasada
  const fechaObj = new Date(fecha + 'T12:00:00');
  const hoy = new Date();
  hoy.setHours(0, 0, 0, 0);
  const fechaSeleccionada = new Date(fechaObj);
  fechaSeleccionada.setHours(0, 0, 0, 0);
  
  const esFuturo = fechaSeleccionada >= hoy;

  // 3. Construir URL según tipo de consulta
  let url;
  if (esFuturo) {
    // Pronóstico futuro
    url = `${CLIMA_CONFIG.baseUrl}?latitude=${CLIMA_CONFIG.latitude}&longitude=${CLIMA_CONFIG.longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,weathercode&timezone=${CLIMA_CONFIG.timezone}&forecast_days=7`;
  } else {
    // Datos históricos
    url = `${CLIMA_CONFIG.baseUrl}?latitude=${CLIMA_CONFIG.latitude}&longitude=${CLIMA_CONFIG.longitude}&daily=temperature_2m_max,temperature_2m_min,weathercode&timezone=${CLIMA_CONFIG.timezone}&past_days=7`;
  }

  try {
    // 4. Realizar petición HTTP
    const response = await fetch(url);
    
    // 5. Verificar respuesta HTTP
    if (!response.ok) {
      throw new Error('Error al obtener datos del clima');
    }

    // 6. Parsear JSON
    const data = await response.json();
    
    // 7. Buscar datos específicos de la fecha
    const fechaBuscada = fecha;
    const indice = data.daily.time.indexOf(fechaBuscada);

    // 8. Validar disponibilidad de datos
    if (indice === -1) {
      return {
        success: false,
        error: 'No hay datos disponibles para esta fecha'
      };
    }

    // 9. Retornar datos estructurados
    return {
      success: true,
      data: {
        fecha: fechaBuscada,
        temperaturaMax: data.daily.temperature_2m_max[indice],
        temperaturaMin: data.daily.temperature_2m_min[indice],
        probabilidadPrecipitacion: data.daily.precipitation_probability_max ? 
          data.daily.precipitation_probability_max[indice] : 0,
        codigoClima: data.daily.weathercode[indice]
      }
    };
  } catch (error) {
    // 10. Manejo de errores
    console.error('Error obteniendo clima:', error);
    return {
      success: false,
      error: 'Error al conectar con el servicio de clima'
    };
  }
}
```

### Funciones Helper

#### `obtenerDescripcionClima(codigo)`

Convierte códigos numéricos WMO a descripciones en español.

```javascript
export function obtenerDescripcionClima(codigo) {
  const descripciones = {
    0: 'Despejado',
    1: 'Principalmente despejado',
    2: 'Parcialmente nublado',
    3: 'Nublado',
    45: 'Niebla',
    48: 'Niebla con escarcha',
    51: 'Llovizna ligera',
    53: 'Llovizna moderada',
    55: 'Llovizna intensa',
    61: 'Lluvia ligera',
    63: 'Lluvia moderada',
    65: 'Lluvia intensa',
    71: 'Nevada ligera',
    73: 'Nevada moderada',
    75: 'Nevada intensa',
    77: 'Granizo',
    80: 'Chubascos ligeros',
    81: 'Chubascos moderados',
    82: 'Chubascos intensos',
    85: 'Nevadas ligeras',
    86: 'Nevadas intensas',
    95: 'Tormenta',
    96: 'Tormenta con granizo ligero',
    99: 'Tormenta con granizo intenso'
  };
  return descripciones[codigo] || 'Desconocido';
}
```

#### `obtenerIconoClima(codigo)`

Retorna un emoji apropiado para cada condición climática.

```javascript
export function obtenerIconoClima(codigo) {
  if (codigo === 0 || codigo === 1) return '☀️';
  if (codigo === 2 || codigo === 3) return '⛅';
  if (codigo === 45 || codigo === 48) return '🌫️';
  if (codigo >= 51 && codigo <= 55) return '🌦️';
  if (codigo >= 61 && codigo <= 65) return '🌧️';
  if (codigo >= 71 && codigo <= 77) return '❄️';
  if (codigo >= 80 && codigo <= 82) return '🌧️';
  if (codigo >= 85 && codigo <= 86) return '❄️';
  if (codigo >= 95 && codigo <= 99) return '⛈️';
  return '🌤️';
}
```

---

## 🎨 Uso en Componentes Vue

### En ModalReserva.vue

```vue
<script setup>
import { ref, watch } from 'vue';
import { obtenerClima, obtenerDescripcionClima, obtenerIconoClima } from '@/services/api';

const climaData = ref(null);
const climaCargando = ref(false);
const climaError = ref(null);

// Observar cambios en la fecha seleccionada
watch(() => props.fecha, async (nuevaFecha) => {
  if (nuevaFecha) {
    climaCargando.value = true;
    climaError.value = null;
    
    const resultado = await obtenerClima(nuevaFecha);
    
    if (resultado.success) {
      climaData.value = resultado.data;
    } else {
      climaError.value = resultado.error;
    }
    
    climaCargando.value = false;
  }
});
</script>

<template>
  <div v-if="climaData" class="clima-info">
    <h6>
      {{ obtenerIconoClima(climaData.codigoClima) }}
      {{ obtenerDescripcionClima(climaData.codigoClima) }}
    </h6>
    <p>
      🌡️ {{ climaData.temperaturaMin }}°C - {{ climaData.temperaturaMax }}°C
    </p>
    <p>
      💧 Prob. lluvia: {{ climaData.probabilidadPrecipitacion }}%
    </p>
  </div>
</template>
```

---

## ⚠️ Manejo de Errores

### Tipos de Errores Manejados

1. **Fecha inválida**
   ```javascript
   { success: false, error: 'Fecha no válida' }
   ```

2. **Error de red**
   ```javascript
   { success: false, error: 'Error al conectar con el servicio de clima' }
   ```

3. **Datos no disponibles**
   ```javascript
   { success: false, error: 'No hay datos disponibles para esta fecha' }
   ```

4. **Error HTTP**
   ```javascript
   { success: false, error: 'HTTP Error: 500' }
   ```

### Estrategia de Manejo

```javascript
// En el componente
const resultado = await obtenerClima(fecha);

if (resultado.success) {
  // Usar resultado.data
  mostrarClima(resultado.data);
} else {
  // Mostrar error al usuario
  mostrarError(resultado.error);
}
```

---

## 🚀 Optimizaciones

### Caching (Recomendado)

```javascript
const cacheClima = new Map();
const CACHE_DURATION = 15 * 60 * 1000; // 15 minutos

export async function obtenerClimaConCache(fecha) {
  const ahora = Date.now();
  const cached = cacheClima.get(fecha);
  
  if (cached && (ahora - cached.timestamp) < CACHE_DURATION) {
    return cached.data;
  }
  
  const data = await obtenerClima(fecha);
  cacheClima.set(fecha, { data, timestamp: ahora });
  
  return data;
}
```

### Debounce en Inputs

```javascript
import { debounce } from 'lodash-es';

const consultarClima = debounce(async (fecha) => {
  const resultado = await obtenerClima(fecha);
  // ...
}, 500);
```

---

## 📈 Limitaciones y Consideraciones

### Límites de la API

- **10,000 requests/día** en tier gratuito
- Recomendado implementar caching para reducir llamadas
- Los datos históricos pueden variar según la ubicación

### Precisión de Datos

- **Pronósticos:** Más precisos para los primeros 3-5 días
- **Históricos:** Dependen de la disponibilidad de estaciones meteorológicas
- **Ubicación:** Coordenadas fijas de Santiago, Chile

### CORS

- ✅ Habilitado por defecto en Open-Meteo
- No requiere configuración adicional
- Funciona directamente desde el navegador

---

## 🔗 Referencias

- **Documentación oficial:** https://open-meteo.com/en/docs
- **WMO Weather Codes:** https://www.nodc.noaa.gov/archive/arc0021/0002199/1.1/data/0-data/HTML/WMO-CODE/WMO4677.HTM
- **Licencia:** CC BY 4.0 - https://creativecommons.org/licenses/by/4.0/

---

**Última actualización:** Octubre 2025  
**Versión de API:** v1  
**Mantenido por:** Equipo Club Deportivo

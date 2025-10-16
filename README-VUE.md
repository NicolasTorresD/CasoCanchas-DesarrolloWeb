# 🏟️ Sistema de Reserva de Canchas Deportivas - Vue 3

Sistema moderno de reserva de canchas deportivas construido con **Vue 3**, **Vite** y la **Composition API**. Incluye integración con API de clima en tiempo real.

## 🎯 Características

- ✅ **Vue 3 con Composition API**: Código modular y mantenible
- ✅ **Componentes separados**: Arquitectura limpia y escalable
- ✅ **API separada**: Servicios en archivo independiente
- ✅ **Integración de clima**: Open-Meteo API para pronósticos
- ✅ **Responsive**: Compatible con dispositivos móviles
- ✅ **Filtros dinámicos**: Por deporte y fecha
- ✅ **Sistema de calificaciones**: Con estrellas y comentarios
- ✅ **Hot Module Replacement (HMR)**: Desarrollo rápido con Vite

## 📁 Estructura del Proyecto

```
CasoCanchas-DesarrolloWeb-master/
├── src/
│   ├── components/
│   │   ├── ListadoCanchas.vue      # Lista de canchas con filtros
│   │   ├── MisReservas.vue         # Gestión de reservas
│   │   ├── FormularioFeedback.vue  # Comentarios y calificaciones
│   │   └── ModalReserva.vue        # Modal con clima integrado
│   ├── services/
│   │   └── api.js                  # Servicios de API separados
│   ├── App.vue                     # Componente principal
│   └── main.js                     # Punto de entrada
├── public/
│   ├── canchas.json               # Datos de canchas
│   ├── reservas.json              # Reservas guardadas
│   ├── feedbacks.json             # Comentarios
│   └── imagenes/                  # Imágenes de canchas
├── index-vue.html                 # HTML principal
├── vite.config.js                 # Configuración de Vite
└── package.json                   # Dependencias
```

## 🛠️ Tecnologías Utilizadas

### Frontend Framework
- **Vue 3.4.0**: Framework progresivo de JavaScript
- **Composition API**: API moderna de Vue para mejor composición

### Build Tool
- **Vite 5.0.0**: Build tool ultrarrápido con HMR
- **@vitejs/plugin-vue 5.0.0**: Plugin oficial de Vue para Vite

### UI Framework
- **Bootstrap 5.3.0**: Framework CSS responsive
- **Font Awesome 6.0.0**: Librería de iconos

### APIs Externas
- **Open-Meteo API**: Datos meteorológicos gratuitos
  - Pronóstico de 7 días
  - Datos históricos
  - Temperatura, precipitación, códigos de clima

### Data Management
- **LocalStorage**: Persistencia de reservas y comentarios
- **JSON Files**: Datos iniciales de canchas

## 🚀 Instalación y Uso

### Prerequisitos
- Node.js 16+ instalado
- npm o yarn

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/NicolasTorresD/CasoCanchas-DesarrolloWeb.git
cd CasoCanchas-DesarrolloWeb-master
```

2. **Instalar dependencias**
```bash
npm install
```

3. **Iniciar servidor de desarrollo**
```bash
npm run dev
```

El servidor se abrirá automáticamente en `http://localhost:8000`

4. **Build para producción**
```bash
npm run build
```

5. **Preview del build de producción**
```bash
npm run preview
```

## 📦 Scripts Disponibles

- `npm run dev` - Inicia servidor de desarrollo con HMR
- `npm run build` - Construye la aplicación para producción
- `npm run preview` - Preview del build de producción

## 🎨 Componentes Vue

### 1. **ListadoCanchas.vue**
- Muestra grid de canchas disponibles
- Filtros por deporte y fecha
- Sistema de calificaciones con estrellas
- Botón de reserva por cancha

**Props:**
- `canchas`: Array de objetos cancha
- `feedbacks`: Array de feedbacks para calificaciones

**Events:**
- `reservar`: Emitido al hacer clic en "Reservar"

**Models:**
- `filtroDeporte`: Filtro de deporte seleccionado
- `filtroFecha`: Filtro de fecha seleccionada

### 2. **MisReservas.vue**
- Lista todas las reservas del usuario
- Muestra información completa de cada reserva
- Botón para cancelar reservas

**Props:**
- `reservas`: Array de reservas
- `canchas`: Array de canchas (para nombres)

**Events:**
- `cancelar`: Emitido al cancelar una reserva

### 3. **FormularioFeedback.vue**
- Formulario para enviar comentarios
- Selector de cancha
- Sistema de calificación con estrellas interactivas
- Lista de opiniones recientes

**Props:**
- `canchas`: Array de canchas disponibles
- `feedbacks`: Array de feedbacks existentes

**Events:**
- `enviar`: Emitido al enviar nuevo feedback

### 4. **ModalReserva.vue**
- Modal de Bootstrap para nueva reserva
- Selección de fecha y hora
- **Integración de clima automática**
- Validación de formulario

**Props:**
- `canchaSeleccionada`: Objeto con datos de la cancha

**Events:**
- `confirmar`: Emitido al confirmar reserva

**Características especiales:**
- Carga automática de clima al seleccionar fecha
- Muestra temperatura máx/mín
- Probabilidad de precipitación
- Icono y descripción del clima

## 🌐 Servicio de API (api.js)

### Funciones de Datos
```javascript
cargarCanchas()      // Carga datos de canchas.json
cargarReservas()     // Carga datos de reservas.json
cargarFeedbacks()    // Carga datos de feedbacks.json
```

### Funciones de Clima
```javascript
obtenerClima(fecha)              // Obtiene clima para fecha específica
obtenerDescripcionClima(codigo)  // Convierte código a descripción
obtenerIconoClima(codigo)        // Obtiene emoji para código
```

### Funciones de Persistencia
```javascript
guardarReserva(reserva)      // Guarda en localStorage
cancelarReserva(id)          // Elimina de localStorage
guardarFeedback(feedback)    // Guarda en localStorage
```

## 🌤️ Integración de API de Clima

### Configuración
```javascript
const CLIMA_CONFIG = {
  baseUrl: 'https://api.open-meteo.com/v1/forecast',
  latitude: -33.4489,  // Santiago, Chile
  longitude: -70.6693,
  timezone: 'auto'
};
```

### Flujo de Trabajo
1. Usuario selecciona fecha en modal de reserva
2. Sistema determina si es fecha futura o pasada
3. Llamada a Open-Meteo API con parámetros correctos
4. Procesamiento de respuesta
5. Actualización reactiva de UI con:
   - Temperatura máxima y mínima
   - Probabilidad de precipitación
   - Descripción del clima
   - Icono representativo

### Códigos de Clima Soportados
- 0-3: Despejado/Nublado
- 45-48: Niebla
- 51-55: Llovizna
- 61-65: Lluvia
- 71-77: Nieve/Granizo
- 80-82: Chubascos
- 95-99: Tormentas

## 🎯 Características de Vue 3 Implementadas

### Composition API
```javascript
import { ref, computed, onMounted, watch } from 'vue';

const canchas = ref([]);
const reservas = computed(() => filtrarReservas());
watch(fecha, () => cargarClima());
onMounted(() => cargarDatos());
```

### Reactive State Management
- `ref()` para valores primitivos
- `reactive()` para objetos
- `computed()` para valores derivados
- `watch()` para efectos secundarios

### Component Communication
- **Props**: Datos del padre al hijo
- **Emits**: Eventos del hijo al padre
- **v-model**: Binding bidireccional

### Lifecycle Hooks
- `onMounted()`: Inicialización
- Carga de datos
- Setup de event listeners

## 🔧 Configuración de Vite

```javascript
export default defineConfig({
  plugins: [vue()],
  server: {
    port: 8000,
    open: true  // Abre navegador automáticamente
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  }
});
```

## 📱 Responsive Design

- Mobile-first approach
- Bootstrap grid system
- Media queries personalizadas
- Componentes adaptables

## 🔒 Seguridad

- Validación de formularios
- Sanitización de inputs
- No exposición de API keys (Open-Meteo es público)
- CORS configurado correctamente

## 🐛 Debugging

Para ver logs en consola:
```javascript
console.log('🚀 Aplicación Vue montada');
console.log('📊 Datos cargados:', canchas.length);
console.log('📅 Preparando reserva para:', cancha.nombre);
console.log('✅ Nueva reserva creada:', nuevaReserva);
```

## 🤝 Contribución

1. Fork el proyecto
2. Crea tu rama de features (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👨‍💻 Autor

- **GitHub**: [@NicolasTorresD](https://github.com/NicolasTorresD)

## 📞 Contacto

¿Preguntas o sugerencias? Abre un issue en GitHub.

---

**Hecho con ❤️ usando Vue 3 + Vite**

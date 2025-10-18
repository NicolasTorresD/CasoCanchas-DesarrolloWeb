<template>
  <div 
    class="modal fade" 
    id="modalReserva" 
    tabindex="-1" 
    aria-labelledby="modalReservaLabel" 
    aria-hidden="true"
    ref="modalElement"
  >
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="modalReservaLabel">
            <i class="fas fa-calendar-plus me-2"></i>Reservar Cancha
          </h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="confirmarReserva">
            <div class="mb-3">
              <label for="nombre-reserva" class="form-label">Nombre Completo</label>
              <input 
                type="text" 
                class="form-control" 
                id="nombre-reserva" 
                v-model="reserva.nombre"
                required
              >
            </div>
            <div class="mb-3">
              <label for="cancha-seleccionada" class="form-label">Cancha Seleccionada</label>
              <input 
                type="text" 
                class="form-control" 
                id="cancha-seleccionada" 
                :value="canchaSeleccionada?.nombre || ''"
                readonly
              >
            </div>
            <div class="mb-3">
              <label for="fecha-reserva" class="form-label">Fecha de Reserva</label>
              <input 
                type="date" 
                class="form-control" 
                id="fecha-reserva" 
                v-model="reserva.fecha"
                :min="fechaMinima"
                @change="cargarClima"
                required
              >
              <small class="form-text text-muted">
                Solo puedes reservar desde hoy en adelante
              </small>
            </div>
            <div class="mb-3">
              <label for="hora-reserva" class="form-label">Hora de Reserva</label>
              <select 
                class="form-select" 
                id="hora-reserva" 
                v-model="reserva.hora"
                required
              >
                <option value="">Selecciona una hora</option>
                <option 
                  v-for="hora in horasDisponibles" 
                  :key="hora" 
                  :value="hora"
                  :disabled="!esHoraValida(hora)"
                >
                  {{ hora }} {{ !esHoraValida(hora) ? '(No disponible)' : '' }}
                </option>
              </select>
              <small class="form-text text-muted" v-if="esHoy">
                Para hoy solo puedes reservar desde 2 horas en adelante
              </small>
            </div>

            <!-- Sección de Clima -->
            <div class="clima-container mb-3" v-if="reserva.fecha">
              <h6 class="mb-3">
                <i class="fas fa-cloud-sun me-2"></i>Condiciones Climáticas
              </h6>
              
              <div v-if="clima.cargando" class="text-center">
                <div class="spinner-border text-primary" role="status">
                  <span class="visually-hidden">Cargando clima...</span>
                </div>
                <p class="mt-2">Obteniendo información del clima...</p>
              </div>

              <div v-else-if="clima.error" class="alert alert-warning">
                <i class="fas fa-exclamation-triangle me-2"></i>
                {{ clima.error }}
              </div>

              <div v-else-if="clima.data" class="clima-card">
                <div class="row align-items-center">
                  <div class="col-md-4 text-center">
                    <div class="clima-icono-grande">{{ clima.icono }}</div>
                    <p class="fw-bold mb-0">{{ clima.descripcion }}</p>
                  </div>
                  <div class="col-md-8">
                    <div class="row">
                      <div class="col-6">
                        <div class="clima-info-item">
                          <i class="fas fa-temperature-high text-danger"></i>
                          <span class="ms-2">Máx: {{ clima.data.temperaturaMax }}°C</span>
                        </div>
                      </div>
                      <div class="col-6">
                        <div class="clima-info-item">
                          <i class="fas fa-temperature-low text-primary"></i>
                          <span class="ms-2">Mín: {{ clima.data.temperaturaMin }}°C</span>
                        </div>
                      </div>
                      <div class="col-12 mt-2">
                        <div class="clima-info-item">
                          <i class="fas fa-umbrella text-info"></i>
                          <span class="ms-2">Precipitación: {{ clima.data.probabilidadPrecipitacion }}%</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                Cancelar
              </button>
              <button type="submit" class="btn btn-primary">
                <i class="fas fa-check me-2"></i>Confirmar Reserva
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, watch, computed } from 'vue';
import { obtenerClima, obtenerDescripcionClima, obtenerIconoClima } from '@/services/api';

const props = defineProps({
  canchaSeleccionada: {
    type: Object,
    default: null
  }
});

const emit = defineEmits(['confirmar']);

const reserva = reactive({
  nombre: '',
  fecha: '',
  hora: ''
});

const clima = reactive({
  data: null,
  cargando: false,
  error: null,
  icono: '',
  descripcion: ''
});

const modalElement = ref(null);

// Horarios disponibles
const horasDisponibles = [
  '08:00', '09:00', '10:00', '11:00', '12:00', 
  '13:00', '14:00', '15:00', '16:00', '17:00', 
  '18:00', '19:00', '20:00', '21:00'
];

// Fecha mínima (hoy)
const fechaMinima = computed(() => {
  const hoy = new Date();
  return hoy.toISOString().split('T')[0];
});

// Verificar si la fecha seleccionada es hoy
const esHoy = computed(() => {
  if (!reserva.fecha) return false;
  const hoy = new Date();
  const fechaSeleccionada = new Date(reserva.fecha + 'T12:00:00');
  
  return (
    fechaSeleccionada.getFullYear() === hoy.getFullYear() &&
    fechaSeleccionada.getMonth() === hoy.getMonth() &&
    fechaSeleccionada.getDate() === hoy.getDate()
  );
});

watch(() => props.canchaSeleccionada, (newCancha) => {
  if (newCancha) {
    limpiarFormulario();
  }
});

// Verificar si una hora es válida para reservar
function esHoraValida(hora) {
  // Si no es hoy, todas las horas son válidas
  if (!esHoy.value) return true;
  
  // Si es hoy, validar que la hora sea al menos 2 horas después de ahora
  const ahora = new Date();
  const horaActual = ahora.getHours();
  const [horaReserva] = hora.split(':').map(Number);
  
  // Debe ser al menos 2 horas después de la hora actual
  return horaReserva >= (horaActual + 2);
}

async function cargarClima() {
  if (!reserva.fecha) return;

  clima.cargando = true;
  clima.error = null;
  clima.data = null;

  const resultado = await obtenerClima(reserva.fecha);

  clima.cargando = false;

  if (resultado.success) {
    clima.data = resultado.data;
    clima.icono = obtenerIconoClima(resultado.data.codigoClima);
    clima.descripcion = obtenerDescripcionClima(resultado.data.codigoClima);
  } else {
    clima.error = resultado.error;
  }
}

function confirmarReserva() {
  if (!reserva.nombre || !reserva.fecha || !reserva.hora) {
    alert('Por favor completa todos los campos');
    return;
  }

  // Validar que la fecha no sea del pasado
  const hoy = new Date();
  hoy.setHours(0, 0, 0, 0);
  const fechaSeleccionada = new Date(reserva.fecha + 'T12:00:00');
  
  if (fechaSeleccionada < hoy) {
    alert('❌ No puedes reservar en una fecha pasada');
    return;
  }

  // Validar que la hora no sea del pasado si es hoy
  if (esHoy.value) {
    const ahora = new Date();
    const horaActual = ahora.getHours();
    const [horaReserva] = reserva.hora.split(':').map(Number);
    
    if (horaReserva < (horaActual + 2)) {
      alert('❌ Para hoy, debes reservar con al menos 2 horas de anticipación');
      return;
    }
  }

  const nuevaReserva = {
    id: Date.now().toString(),
    nombre: reserva.nombre,
    canchaId: props.canchaSeleccionada.id,
    fecha: reserva.fecha,
    hora: reserva.hora
  };

  emit('confirmar', nuevaReserva);
  
  // Cerrar modal usando Bootstrap
  const modal = window.bootstrap.Modal.getInstance(modalElement.value);
  if (modal) {
    modal.hide();
  }

  limpiarFormulario();
}

function limpiarFormulario() {
  reserva.nombre = '';
  reserva.fecha = '';
  reserva.hora = '';
  clima.data = null;
  clima.cargando = false;
  clima.error = null;
  clima.icono = '';
  clima.descripcion = '';
}

defineExpose({
  limpiarFormulario
});
</script>

<style scoped>
.clima-card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 20px;
  border-radius: 15px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.clima-icono-grande {
  font-size: 3rem;
  margin-bottom: 10px;
}

.clima-info-item {
  display: flex;
  align-items: center;
  padding: 8px 0;
  font-size: 1.1rem;
}
</style>

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
                @change="cargarClima"
                required
              >
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
                <option value="08:00">08:00</option>
                <option value="09:00">09:00</option>
                <option value="10:00">10:00</option>
                <option value="11:00">11:00</option>
                <option value="12:00">12:00</option>
                <option value="13:00">13:00</option>
                <option value="14:00">14:00</option>
                <option value="15:00">15:00</option>
                <option value="16:00">16:00</option>
                <option value="17:00">17:00</option>
                <option value="18:00">18:00</option>
                <option value="19:00">19:00</option>
                <option value="20:00">20:00</option>
                <option value="21:00">21:00</option>
              </select>
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
import { ref, reactive, watch } from 'vue';
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

watch(() => props.canchaSeleccionada, (newCancha) => {
  if (newCancha) {
    limpiarFormulario();
  }
});

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

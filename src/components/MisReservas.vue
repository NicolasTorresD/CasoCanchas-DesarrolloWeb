<template>
  <div class="container mt-4">
    <h2 class="text-center mb-4 titulo-seccion">
      <i class="fas fa-calendar-check me-2"></i>Mis Reservas
    </h2>

    <div v-if="cargando" class="text-center">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Cargando...</span>
      </div>
      <p class="mt-2">Cargando reservas...</p>
    </div>

    <div v-else-if="error" class="alert alert-danger text-center">
      <i class="fas fa-exclamation-triangle me-2"></i>{{ error }}
    </div>

    <div v-else-if="reservas.length === 0" class="alert alert-info text-center">
      <i class="fas fa-info-circle me-2"></i>
      No tienes reservas registradas aún.
    </div>

    <div v-else class="row" id="listado-reservas">
      <div 
        v-for="reserva in reservas" 
        :key="reserva.id_reserva" 
        class="col-md-6 mb-4"
      >
        <div class="card reserva-card h-100">
          <div class="card-body">
            <h5 class="card-title">
              <i class="fas fa-user me-2"></i>{{ usuario?.nombre || 'Usuario' }}
            </h5>
            <p class="card-text">
              <strong><i class="fas fa-futbol me-2"></i>Cancha:</strong> 
              {{ obtenerNombreCancha(reserva.id_cancha) }}
            </p>
            <p class="card-text">
              <strong><i class="fas fa-calendar me-2"></i>Fecha:</strong> 
              {{ formatearFecha(reserva.fecha) }}
            </p>
            <p class="card-text">
              <strong><i class="fas fa-clock me-2"></i>Hora:</strong> 
              {{ reserva.hora }}
            </p>
            <p class="card-text">
              <strong><i class="fas fa-dollar-sign me-2"></i>Precio:</strong> 
              ${{ reserva.precio_total }}
            </p>
            <p class="card-text">
              <strong><i class="fas fa-info-circle me-2"></i>Estado:</strong> 
              {{ reserva.estado }}
            </p>
            <button 
              v-if="puedeCancelar(reserva)"
              class="btn btn-danger w-100" 
              @click="cancelarReserva(reserva.id_reserva)">
              <i class="fas fa-times-circle me-2"></i>Cancelar Reserva
            </button>
            <button 
              v-else
              class="btn btn-secondary w-100" 
              disabled
              title="No se puede cancelar: La reserva está muy próxima o ya pasó"
            >
              <i class="fas fa-ban me-2"></i>No se puede cancelar la reserva
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { cargarReservas, cancelarReservaBackend } from '@/services/api';
import { ref, onMounted } from 'vue';

const reservas = ref([]);
const cargando = ref(false);
const error = ref(null);

const props = defineProps({
  reservas: {
    type: Array,
    required: true
  },
  canchas: {
    type: Array,
    required: true
  },
  usuario: {
    type: Object,
    required: true
  }
});

onMounted(async () => {
  cargando.value = true;
  try {
    const todas = await cargarReservas();
    console.log("Usuario actual en MisReservas:", props.usuario);
    if (props.usuario && props.usuario.id_usuario) {
      reservas.value = todas.filter(r => r.id_usuario === props.usuario.id_usuario);
    } else {
      reservas.value = [];
    }
  } catch (err) {
    console.error(err);
    error.value = 'No se pudieron cargar las reservas';
  } finally {
    cargando.value = false;
  }
});

defineEmits(['cancelar']);

function obtenerNombreCancha(canchaId) {
  const cancha = props.canchas.find(c => c.id === canchaId);
  return cancha ? cancha.nombre : canchaId;
}

function formatearFecha(fecha) {
  const opciones = { year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(fecha + 'T12:00:00').toLocaleDateString('es-ES', opciones);
}

function puedeCancelar(reserva) {
  // Obtener fecha y hora actual
  const ahora = new Date();
  
  // Crear fecha y hora de la reserva
  const [año, mes, dia] = reserva.fecha.split('-');
  const [hora, minutos] = reserva.hora.split(':');
  
  const fechaReserva = new Date(año, mes - 1, dia, hora, minutos);
  
  // Calcular la diferencia en milisegundos
  const diferencia = fechaReserva - ahora;
  
  // Convertir a horas (1 hora = 3600000 milisegundos)
  const horasHastaReserva = diferencia / (1000 * 60 * 60);
  
  // Permitir cancelación solo si faltan más de 1 hora
  // Si la diferencia es negativa, significa que la fecha ya pasó
  return horasHastaReserva > 1;
}

async function cancelarReserva(id_reserva) {
  const confirmacion = confirm("¿Seguro que quieres cancelar esta reserva?");
  if (!confirmacion) return;

  const resultado = await cancelarReservaBackend(id_reserva);
  if (resultado.success) {
    // Eliminar de la lista local
    reservas.value = reservas.value.filter(r => r.id_reserva !== id_reserva);
    alert("✅ Reserva cancelada exitosamente");
  } else {
    alert("❌ Error al cancelar la reserva: " + resultado.error);
  }
}
</script>

<style scoped>
.reserva-card {
  border-left: 4px solid #0d6efd;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.reserva-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.btn-secondary:disabled {
  background-color: #6c757d;
  border-color: #6c757d;
  cursor: not-allowed;
  opacity: 0.65;
}

.btn-secondary:disabled:hover {
  background-color: #6c757d;
  border-color: #6c757d;
}
</style>

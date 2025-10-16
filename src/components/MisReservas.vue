<template>
  <div class="container mt-4">
    <h2 class="text-center mb-4 titulo-seccion">
      <i class="fas fa-calendar-check me-2"></i>Mis Reservas
    </h2>

    <div v-if="reservas.length === 0" class="alert alert-info text-center">
      <i class="fas fa-info-circle me-2"></i>
      No tienes reservas registradas aún.
    </div>

    <div v-else class="row" id="listado-reservas">
      <div 
        v-for="reserva in reservas" 
        :key="reserva.id" 
        class="col-md-6 mb-4"
      >
        <div class="card reserva-card h-100">
          <div class="card-body">
            <h5 class="card-title">
              <i class="fas fa-user me-2"></i>{{ reserva.nombre }}
            </h5>
            <p class="card-text">
              <strong><i class="fas fa-futbol me-2"></i>Cancha:</strong> 
              {{ obtenerNombreCancha(reserva.canchaId) }}
            </p>
            <p class="card-text">
              <strong><i class="fas fa-calendar me-2"></i>Fecha:</strong> 
              {{ formatearFecha(reserva.fecha) }}
            </p>
            <p class="card-text">
              <strong><i class="fas fa-clock me-2"></i>Hora:</strong> 
              {{ reserva.hora }}
            </p>
            <button 
              class="btn btn-danger w-100" 
              @click="$emit('cancelar', reserva.id)"
            >
              <i class="fas fa-times-circle me-2"></i>Cancelar Reserva
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  reservas: {
    type: Array,
    required: true
  },
  canchas: {
    type: Array,
    required: true
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
</style>

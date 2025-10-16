<template>
  <div class="container mt-4">
    <h2 class="text-center mb-4 titulo-seccion">
      <i class="fas fa-list me-2"></i>Canchas Disponibles
    </h2>

    <!-- Filtros -->
    <div class="row mb-4">
      <div class="col-md-6">
        <label for="filtro-deporte" class="form-label">Filtrar por deporte</label>
        <select id="filtro-deporte" class="form-select" v-model="filtroDeporte">
          <option value="todos">Todos los deportes</option>
          <option value="Fútbol">Fútbol</option>
          <option value="Tenis">Tenis</option>
          <option value="Básquetbol">Básquetbol</option>
          <option value="Pádel">Pádel</option>
          <option value="Vóleibol">Vóleibol</option>
        </select>
      </div>
      <div class="col-md-6">
        <label for="filtro-fecha" class="form-label">Filtrar por fecha disponible</label>
        <input type="date" id="filtro-fecha" class="form-control" v-model="filtroFecha">
      </div>
    </div>

    <!-- Lista de canchas -->
    <div class="row" id="listado-canchas">
      <div 
        v-for="cancha in canchasFiltradas" 
        :key="cancha.id" 
        class="col-md-4 mb-4"
      >
        <div class="card cancha-card h-100">
          <img :src="cancha.imagen" class="card-img-top" :alt="cancha.nombre">
          <div class="card-body">
            <h5 class="card-title">{{ cancha.nombre }}</h5>
            <p class="card-text">
              <span class="badge bg-primary">{{ cancha.deporte }}</span>
              <span class="badge bg-success ms-2">${{ cancha.precio }}/hora</span>
            </p>
            <div class="calificacion mb-2">
              <span v-html="generarEstrellas(promedioCalificacion(cancha.id))"></span>
              <small class="text-muted ms-2">({{ promedioCalificacion(cancha.id) }})</small>
            </div>
            <p class="card-text">{{ cancha.descripcion }}</p>
            <button 
              class="btn btn-primary w-100" 
              @click="$emit('reservar', cancha)"
            >
              <i class="fas fa-calendar-plus me-2"></i>Reservar
            </button>
          </div>
        </div>
      </div>
    </div>

    <div v-if="canchasFiltradas.length === 0" class="alert alert-info text-center">
      No hay canchas disponibles con los filtros seleccionados.
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  canchas: {
    type: Array,
    required: true
  },
  feedbacks: {
    type: Array,
    required: true
  }
});

defineEmits(['reservar']);

const filtroDeporte = defineModel('filtroDeporte', { default: 'todos' });
const filtroFecha = defineModel('filtroFecha', { default: '' });

const canchasFiltradas = computed(() => {
  return props.canchas.filter(cancha => {
    const cumpleDeporte = filtroDeporte.value === 'todos' || cancha.deporte === filtroDeporte.value;
    const cumpleFecha = !filtroFecha.value || cancha.disponibilidad.includes(filtroFecha.value);
    return cumpleDeporte && cumpleFecha;
  });
});

function promedioCalificacion(canchaId) {
  const feedbacksCancha = props.feedbacks.filter(f => f.canchaId === canchaId);
  if (feedbacksCancha.length === 0) return 0;
  const suma = feedbacksCancha.reduce((total, fb) => total + fb.calificacion, 0);
  return (suma / feedbacksCancha.length).toFixed(1);
}

function generarEstrellas(calificacion) {
  let estrellas = '';
  const calificacionRedondeada = Math.round(calificacion);
  for (let i = 1; i <= 5; i++) {
    if (i <= calificacionRedondeada) {
      estrellas += '<i class="fas fa-star"></i>';
    } else {
      estrellas += '<i class="far fa-star"></i>';
    }
  }
  return estrellas;
}
</script>

<style scoped>
.cancha-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.cancha-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.calificacion {
  color: #ffc107;
}
</style>

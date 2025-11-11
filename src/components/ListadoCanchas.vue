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
          <option value="futbol">Fútbol</option>
          <option value="tenis">Tenis</option>
          <option value="padel">Pádel</option>
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
          <img :src="`${cancha.imagen_url}`" :alt="cancha.nombre">
          <div class="card-body">
            <h5 class="card-title">{{ cancha.nombre }}</h5>
            <p class="card-text">
              <span class="badge bg-primary">{{ nombreDeporte(cancha.id_deporte) }}</span>
              <span class="badge bg-success ms-2">{{ formatearPrecio(cancha.precio_hora) }}/hora</span>
            </p>
            <div 
              class="calificacion mb-2" 
              @click="verResenas(cancha)" 
              style="cursor: pointer;"
              :title="'Ver reseñas de ' + cancha.nombre"
            >
              <span v-html="generarEstrellas(promedioCalificacion(cancha.id_cancha))"></span>
              <small class="text-muted ms-2">({{ promedioCalificacion(cancha.id_cancha) }})</small>
            </div>
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

    <!-- Modal de Reseñas -->
    <div 
      class="modal fade" 
      id="modalResenas" 
      tabindex="-1" 
      aria-labelledby="modalResenasLabel" 
      aria-hidden="true"
      ref="modalResenas"
    >
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="modalResenasLabel">
              <i class="fas fa-star me-2"></i>Reseñas de {{ canchaSeleccionada?.nombre }}
            </h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div v-if="resenasCanchaSeleccionada.length === 0" class="alert alert-info">
              Esta cancha aún no tiene reseñas.
            </div>
            <div v-else>
              <div class="mb-3 text-center">
                <h4>Calificación Promedio</h4>
                <div class="calificacion-grande">
                  <span v-html="generarEstrellas(promedioCalificacion(canchaSeleccionada?.id))"></span>
                  <span class="ms-2 fs-4">{{ promedioCalificacion(canchaSeleccionada?.id) }} / 5.0</span>
                </div>
                <small class="text-muted">({{ resenasCanchaSeleccionada.length }} reseña{{ resenasCanchaSeleccionada.length !== 1 ? 's' : '' }})</small>
              </div>
              <hr>
              <div 
                v-for="resena in resenasCanchaSeleccionada" 
                :key="resena.id"
                class="card mb-3"
              >
                <div class="card-body">
                  <div class="d-flex justify-content-between align-items-start mb-2">
                    <div>
                      <h6 class="mb-1">{{ resena.usuario }}</h6>
                      <small class="text-muted">{{ formatearFecha(resena.fecha) }}</small>
                    </div>
                    <div class="calificacion">
                      <span v-html="generarEstrellas(resena.calificacion)"></span>
                    </div>
                  </div>
                  <p class="mb-0">{{ resena.comentario }}</p>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue';

const props = defineProps({
  canchas: {
    type: Array,
    required: true
  },
  feedbacks: {
    type: Array,
    required: true
  },
  deportes: {
    type: Array,
    required: true
  }
});

defineEmits(['reservar']);

const filtroDeporte = defineModel('filtroDeporte', { default: 'todos' });
const filtroFecha = defineModel('filtroFecha', { default: '' });

const canchaSeleccionada = ref(null);
const modalResenas = ref(null);

const canchasFiltradas = computed(() => {
  return props.canchas.filter(cancha => {
    const cumpleDeporte = filtroDeporte.value === 'todos' || cancha.deporte.toLowerCase() === filtroDeporte.value.toLowerCase();
    const cumpleFecha = !filtroFecha.value || (cancha.disponibilidad && cancha.disponibilidad.includes(filtroFecha.value));
    return cumpleDeporte && cumpleFecha;
  });
});

const resenasCanchaSeleccionada = computed(() => {
  if (!canchaSeleccionada.value) return [];
  return props.feedbacks.filter(f => f.id_cancha === canchaSeleccionada.value.id);
});

function promedioCalificacion(canchaId) {
  const feedbacksCancha = props.feedbacks.filter(f => f.id_cancha === canchaId);
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

function capitalizarDeporte(deporte) {
  return deporte.charAt(0).toUpperCase() + deporte.slice(1);
}

function formatearPrecio(precio) {
  // Multiplicar por 1000 para convertir a pesos chilenos
  const precioChileno = precio * 1000;
  // Formatear con puntos como separadores de miles
  return `$${precioChileno.toLocaleString('es-CL')}`;
}

function verResenas(cancha) {
  canchaSeleccionada.value = cancha;
  const modalElement = document.getElementById('modalResenas');
  const modal = new window.bootstrap.Modal(modalElement);
  modal.show();
}

function formatearFecha(fecha) {
  const opciones = { year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(fecha).toLocaleDateString('es-ES', opciones);
}

function nombreDeporte(idDeporte) {
  const dep = props.deportes.find(d => d.id_deporte === idDeporte);
  if (!dep || !dep.nombre) return 'Sin deporte';
  return dep.nombre.charAt(0).toUpperCase() + dep.nombre.slice(1);
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

.calificacion-grande {
  color: #ffc107;
  font-size: 2rem;
}

.calificacion:hover {
  opacity: 0.8;
}
</style>

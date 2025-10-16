<template>
  <div class="container mt-4">
    <h2 class="text-center mb-4 titulo-seccion">
      <i class="fas fa-comment-dots me-2"></i>Deja tu Opinión
    </h2>

    <div class="row">
      <div class="col-md-6">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title mb-4">Enviar Comentario</h5>
            <form @submit.prevent="enviarFeedback">
              <div class="mb-3">
                <label for="usuario" class="form-label">Tu Nombre</label>
                <input 
                  type="text" 
                  class="form-control" 
                  id="usuario" 
                  v-model="nuevoFeedback.usuario"
                  required
                >
              </div>
              <div class="mb-3">
                <label for="cancha-fb" class="form-label">Cancha</label>
                <select 
                  class="form-select" 
                  id="cancha-fb" 
                  v-model="nuevoFeedback.canchaId"
                  required
                >
                  <option value="">Selecciona una cancha</option>
                  <option 
                    v-for="cancha in canchas" 
                    :key="cancha.id" 
                    :value="cancha.id"
                  >
                    {{ cancha.nombre }}
                  </option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Calificación</label>
                <div class="calificacion-selector">
                  <i 
                    v-for="estrella in 5" 
                    :key="estrella"
                    :class="['fas', 'fa-star', 'estrella', { 'seleccionada': estrella <= nuevoFeedback.calificacion }]"
                    @click="nuevoFeedback.calificacion = estrella"
                  ></i>
                </div>
              </div>
              <div class="mb-3">
                <label for="comentario" class="form-label">Comentario</label>
                <textarea 
                  class="form-control" 
                  id="comentario" 
                  rows="4" 
                  v-model="nuevoFeedback.comentario"
                  required
                ></textarea>
              </div>
              <button type="submit" class="btn btn-primary w-100">
                <i class="fas fa-paper-plane me-2"></i>Enviar Opinión
              </button>
            </form>
          </div>
        </div>
      </div>

      <div class="col-md-6">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title mb-4">Opiniones Recientes</h5>
            <div class="feedback-list">
              <div 
                v-for="feedback in feedbacks.slice(-5).reverse()" 
                :key="feedback.id"
                class="feedback-item mb-3 p-3 border rounded"
              >
                <div class="d-flex justify-content-between align-items-start mb-2">
                  <strong>{{ feedback.usuario }}</strong>
                  <div class="calificacion-mostrar">
                    <span v-html="generarEstrellas(feedback.calificacion)"></span>
                  </div>
                </div>
                <small class="text-muted d-block mb-2">
                  <i class="fas fa-futbol me-1"></i>{{ obtenerNombreCancha(feedback.canchaId) }}
                </small>
                <p class="mb-0">{{ feedback.comentario }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue';

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

const emit = defineEmits(['enviar']);

const nuevoFeedback = reactive({
  usuario: '',
  canchaId: '',
  calificacion: 0,
  comentario: ''
});

function enviarFeedback() {
  if (nuevoFeedback.calificacion === 0) {
    alert('Por favor selecciona una calificación');
    return;
  }

  emit('enviar', { ...nuevoFeedback });

  // Limpiar formulario
  nuevoFeedback.usuario = '';
  nuevoFeedback.canchaId = '';
  nuevoFeedback.calificacion = 0;
  nuevoFeedback.comentario = '';
}

function obtenerNombreCancha(canchaId) {
  const cancha = props.canchas.find(c => c.id === canchaId);
  return cancha ? cancha.nombre : canchaId;
}

function generarEstrellas(calificacion) {
  let estrellas = '';
  for (let i = 1; i <= 5; i++) {
    if (i <= calificacion) {
      estrellas += '<i class="fas fa-star"></i>';
    } else {
      estrellas += '<i class="far fa-star"></i>';
    }
  }
  return estrellas;
}
</script>

<style scoped>
.calificacion-selector {
  display: flex;
  gap: 10px;
  font-size: 2rem;
}

.estrella {
  cursor: pointer;
  color: #ddd;
  transition: color 0.2s;
}

.estrella.seleccionada {
  color: #ffc107;
}

.estrella:hover {
  color: #ffdb4d;
}

.calificacion-mostrar {
  color: #ffc107;
}

.feedback-item {
  background-color: rgba(255, 255, 255, 0.05);
  transition: background-color 0.3s;
}

.feedback-item:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.feedback-list {
  max-height: 600px;
  overflow-y: auto;
}
</style>

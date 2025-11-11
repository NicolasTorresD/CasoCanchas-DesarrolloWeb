<template>
  <div class="container mt-4">
    <h2 class="text-center mb-4 titulo-seccion">
      <i class="fas fa-comment-dots me-2"></i>Deja tu Opinión
    </h2>

    <div class="row">
      <!-- Sección enviar comentario (la dejamos igual por ahora) -->
 <div class="col-md-6">
  <div class="card">
    <div class="card-body">
      <h5 class="card-title mb-4">Enviar Comentario</h5>
      <form @submit.prevent="enviarFeedbackForm">
      <div class="mb-3">
        <label for="reserva-fb" class="form-label">Reserva</label>
        <select 
        class="form-select" 
          id="reserva-fb" 
        v-model="nuevoFeedback.reservaId"
        required
    >
        <option value="">Selecciona una reserva</option>
<option 
  v-for="reserva in (reservas || []).filter(r => r.id_usuario === usuario?.id_usuario)" 
  :key="reserva.id_reserva" 
  :value="reserva.id_reserva"
>
  📅 {{ formatearFecha(reserva.fecha) }} ⏰ {{ reserva.hora }} - 🏟️ {{ obtenerNombreCancha(reserva.id_cancha) }}
</option>
        </select>
        </div>

<div class="mb-3">
  <label class="form-label">Calificación</label>
  <div class="calificacion-selector">
    <i 
      v-for="estrella in 5" 
      :key="estrella"
      :class="[
        'fa-star',
        estrella <= nuevoFeedback.calificacion ? 'fas seleccionada' : 'far'
      ]"
      @click="nuevoFeedback.calificacion = estrella"
      style="cursor: pointer; font-size: 1.5rem; color: gold;"
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

        <button type="submit" class="btn btn-primary w-100" :disabled="cargando">
          <i class="fas fa-paper-plane me-2"></i>
          {{ cargando ? 'Enviando...' : 'Enviar Opinión' }}
        </button>
      </form>
    </div>
  </div>
</div>

      <!-- Sección opiniones recientes -->
      <div class="col-md-6">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title mb-4">Opiniones Recientes</h5>

            <div v-if="cargando" class="text-center"> 
              <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Cargando...</span>
              </div>
              <p class="mt-2">Cargando reseñas...</p>
            </div>

            <div v-else-if="error" class="alert alert-danger text-center">
              <i class="fas fa-exclamation-triangle me-2"></i>{{ error }}
            </div>

            <div v-else-if="feedbacks.length === 0" class="alert alert-info text-center">
              <i class="fas fa-info-circle me-2"></i>No hay reseñas disponibles aún.
            </div>

            <div v-else class="feedback-list">
              <div 
                v-for="feedback in feedbacks.slice(-5).reverse()" 
                :key="feedback.id_feedback"
                class="feedback-item mb-3 p-3 border rounded"
              >
                <div class="d-flex justify-content-between align-items-start mb-2">
                  <div>
                    <strong>{{ feedback.usuario }}</strong>
                    <small class="text-muted d-block">
                      <i class="fas fa-calendar me-1"></i>{{ formatearFecha(feedback.fecha) }}
                    </small>
                  </div>
                  <div class="calificacion-mostrar">
                    <span v-html="generarEstrellas(feedback.calificacion)"></span>
                  </div>
                </div>
                <small class="text-muted d-block mb-2">
                  <i class="fas fa-futbol me-1"></i>{{ obtenerNombreCancha(feedback.id_cancha) }}
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
import { ref, onMounted, reactive } from 'vue';
import { enviarFeedback, cargarFeedbacks } from '@/services/api';

const props = defineProps({
  canchas: {
    type: Array,
    required: true
  },
  reservas: { // 👈 necesitamos las reservas del usuario
    type: Array,
    required: true
  },
  usuario: {
    type: Object,
    required: true
  }
});

const feedbacks = ref([]);
const cargando = ref(false);
const error = ref(null);

const nuevoFeedback = reactive({
  reservaId: '',
  calificacion: 0,
  comentario: ''
});

onMounted(async () => {
  cargando.value = true;
  try {
    feedbacks.value = await cargarFeedbacks();
  } catch (err) {
    console.error(err);
    error.value = 'No se pudieron cargar las reseñas';
  } finally {
    cargando.value = false;
  }
});

// Helpers
function obtenerNombreCancha(id_cancha) {
  const cancha = props.canchas.find(c => c.id_cancha === id_cancha);
  return cancha ? cancha.nombre : 'Cancha desconocida';
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

function formatearFecha(fecha) {
  if (!fecha) return 'Fecha no disponible';
  try {
    return new Date(fecha).toLocaleDateString('es-CL', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  } catch {
    return fecha;
  }
}

async function enviarFeedbackForm() {
  if (!nuevoFeedback.reservaId || nuevoFeedback.calificacion === 0 || !nuevoFeedback.comentario) {
    alert("Por favor completa todos los campos");
    return;
  }

  // Validar que la reserva pertenece al usuario actual
  const reserva = props.reservas.find(r => r.id_reserva === Number(nuevoFeedback.reservaId));
  if (!reserva || reserva.id_usuario !== props.usuario.id_usuario) {
    alert("❌ No puedes enviar feedback sobre una reserva que no te pertenece");
    return;
  }

  cargando.value = true;
  try {
    await enviarFeedback(
      nuevoFeedback.reservaId,
      props.usuario.id_usuario,
      {
        calificacion: nuevoFeedback.calificacion,
        comentario: nuevoFeedback.comentario
      }
    );
    alert("✅ Feedback enviado con éxito");

      feedbacks.value = await cargarFeedbacks();
      

    // limpiar formulario
    nuevoFeedback.reservaId = '';
    nuevoFeedback.calificacion = 0;
    nuevoFeedback.comentario = '';
  } catch (err) {
    alert("❌ Error al enviar feedback");
  } finally {
    cargando.value = false;
  }
}
</script>

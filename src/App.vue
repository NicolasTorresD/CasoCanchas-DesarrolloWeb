<template>
  <div id="app">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <span class="navbar-brand fw-bold" style="cursor: default;">
          <i class="fas fa-futbol me-2"></i>Club Deportivo
        </span>
        <button 
          class="navbar-toggler" 
          type="button" 
          data-bs-toggle="collapse" 
          data-bs-target="#navbarNav"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a 
                class="nav-link" 
                :class="{ active: paginaActual === 'listado' }"
                href="#" 
                @click.prevent="cambiarPagina('listado')"
              >
                <i class="fas fa-list me-2"></i>Canchas Disponibles
              </a>
            </li>
            <li class="nav-item">
              <a 
                class="nav-link" 
                :class="{ active: paginaActual === 'reservas' }"
                href="#" 
                @click.prevent="cambiarPagina('reservas')"
              >
                <i class="fas fa-calendar-check me-2"></i>Mis Reservas
              </a>
            </li>
            <li class="nav-item">
              <a 
                class="nav-link" 
                :class="{ active: paginaActual === 'feedback' }"
                href="#" 
                @click.prevent="cambiarPagina('feedback')"
              >
                <i class="fas fa-comment-dots me-2"></i>Dejar Opinión
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Contenido Principal -->
    <div class="container-fluid">
      <transition name="fade" mode="out-in">
        <ListadoCanchas 
          v-if="paginaActual === 'listado'"
          :canchas="canchas"
          :feedbacks="feedbacks"
          v-model:filtroDeporte="filtroDeporte"
          v-model:filtroFecha="filtroFecha"
          @reservar="prepararReserva"
        />

        <MisReservas 
          v-else-if="paginaActual === 'reservas'"
          :reservas="reservas"
          :canchas="canchas"
          @cancelar="mostrarModalCancelacion"
        />

        <FormularioFeedback 
          v-else-if="paginaActual === 'feedback'"
          :canchas="canchas"
          :feedbacks="feedbacks"
          @enviar="agregarFeedback"
        />
      </transition>
    </div>

    <!-- Modal de Reserva -->
    <ModalReserva 
      :canchaSeleccionada="canchaSeleccionada"
      @confirmar="agregarReserva"
      ref="modalReserva"
    />

    <!-- Modal de Cancelación -->
    <div 
      class="modal fade" 
      id="modalCancelar" 
      tabindex="-1" 
      aria-labelledby="modalCancelarLabel" 
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="modalCancelarLabel">
              <i class="fas fa-exclamation-triangle me-2"></i>Confirmar Cancelación
            </h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            ¿Estás seguro de que deseas cancelar esta reserva?
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
              No, mantener
            </button>
            <button type="button" class="btn btn-danger" @click="confirmarCancelacion">
              Sí, cancelar
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import ListadoCanchas from './components/ListadoCanchas.vue';
import MisReservas from './components/MisReservas.vue';
import FormularioFeedback from './components/FormularioFeedback.vue';
import ModalReserva from './components/ModalReserva.vue';
import { 
  cargarCanchas, 
  cargarReservas, 
  cargarFeedbacks,
  guardarReserva,
  cancelarReserva,
  guardarFeedback
} from './services/api';

// Estado de la aplicación
const paginaActual = ref('listado');
const canchas = ref([]);
const reservas = ref([]);
const feedbacks = ref([]);
const canchaSeleccionada = ref(null);
const idReservaACancelar = ref(null);

// Filtros
const filtroDeporte = ref('todos');
const filtroFecha = ref('');

// Referencias a modals
const modalReserva = ref(null);

// Cargar datos al montar el componente
onMounted(async () => {
  console.log('🚀 Aplicación Vue montada');
  
  // Cargar datos desde JSONs
  canchas.value = await cargarCanchas();
  reservas.value = await cargarReservas();
  feedbacks.value = await cargarFeedbacks();

  // Cargar datos del localStorage si existen
  const reservasGuardadas = localStorage.getItem('reservas');
  if (reservasGuardadas) {
    try {
      const reservasLS = JSON.parse(reservasGuardadas);
      reservas.value = [...reservas.value, ...reservasLS];
    } catch (e) {
      console.error('Error cargando reservas del localStorage', e);
    }
  }

  const feedbacksGuardados = localStorage.getItem('feedbacks');
  if (feedbacksGuardados) {
    try {
      const feedbacksLS = JSON.parse(feedbacksGuardados);
      feedbacks.value = [...feedbacks.value, ...feedbacksLS];
    } catch (e) {
      console.error('Error cargando feedbacks del localStorage', e);
    }
  }

  console.log(`📊 Datos cargados: ${canchas.value.length} canchas, ${reservas.value.length} reservas, ${feedbacks.value.length} feedbacks`);
});

// Navegación entre páginas
function cambiarPagina(pagina) {
  paginaActual.value = pagina;
}

// Gestión de reservas
function prepararReserva(cancha) {
  console.log('📅 Preparando reserva para:', cancha.nombre);
  canchaSeleccionada.value = cancha;
  
  // Abrir modal usando Bootstrap
  const modalElement = document.getElementById('modalReserva');
  const modal = new window.bootstrap.Modal(modalElement);
  modal.show();
}

function agregarReserva(nuevaReserva) {
  console.log('✅ Nueva reserva creada:', nuevaReserva);
  
  // Agregar a la lista de reservas
  reservas.value.push(nuevaReserva);
  
  // Guardar en localStorage
  guardarReserva(nuevaReserva);
  
  // Mostrar alerta de éxito
  alert('¡Reserva realizada con éxito!');
  
  // Cambiar a la página de reservas
  cambiarPagina('reservas');
}

function mostrarModalCancelacion(idReserva) {
  idReservaACancelar.value = idReserva;
  
  const modalElement = document.getElementById('modalCancelar');
  const modal = new window.bootstrap.Modal(modalElement);
  modal.show();
}

function confirmarCancelacion() {
  if (!idReservaACancelar.value) return;
  
  // Eliminar de la lista
  reservas.value = reservas.value.filter(r => r.id !== idReservaACancelar.value);
  
  // Eliminar del localStorage
  cancelarReserva(idReservaACancelar.value);
  
  console.log('🗑️ Reserva cancelada:', idReservaACancelar.value);
  
  // Cerrar modal
  const modalElement = document.getElementById('modalCancelar');
  const modal = window.bootstrap.Modal.getInstance(modalElement);
  if (modal) {
    modal.hide();
  }
  
  alert('Reserva cancelada exitosamente');
  idReservaACancelar.value = null;
}

// Gestión de feedbacks
function agregarFeedback(nuevoFeedback) {
  const fechaActual = new Date();
  const fechaFormateada = fechaActual.toISOString().split('T')[0]; // Formato YYYY-MM-DD
  
  const feedbackCompleto = {
    id: Date.now().toString(),
    ...nuevoFeedback,
    fecha: fechaFormateada,
    timestamp: fechaActual.toISOString()
  };
  
  console.log('💬 Nuevo feedback agregado:', feedbackCompleto);
  
  // Agregar a la lista
  feedbacks.value.push(feedbackCompleto);
  
  // Guardar en localStorage
  guardarFeedback(feedbackCompleto);
  
  alert('¡Gracias por tu opinión!');
}
</script>

<style>
/* Importar estilos globales */
@import url('https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');

/* Estilos globales */
body {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  background-attachment: fixed;
  min-height: 100vh;
  color: #fff;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

#app {
  min-height: 100vh;
}

.navbar {
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

.titulo-seccion {
  color: #fff;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.card {
  background: rgba(255, 255, 255, 0.95);
  border: none;
  border-radius: 15px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  color: #333;
}

.modal-content {
  background: rgba(255, 255, 255, 0.98);
  border-radius: 15px;
  color: #333;
}

/* Transiciones */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* Scrollbar personalizado */
::-webkit-scrollbar {
  width: 10px;
}

::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.1);
}

::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.3);
  border-radius: 5px;
}

::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.5);
}
</style>

<template>
  <div id="app">
    <!-- Si NO está logueado, mostrar login -->
    <Login v-if="!logueado" @login-exitoso="manejarLogin" />


    <!-- Si está logueado, mostrar dashboard -->
    <div v-else>
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
            <ul class="navbar-nav ms-auto">
              <li class="nav-item d-flex align-items-center me-3">
                <span class="nav-link disabled">
                Hola, {{ usuario?.nombre || 'Usuario' }}
                </span>
              </li>
              <li class="nav-item">
                <button class="btn btn-outline-danger" @click="cerrarSesion">
                <i class="fas fa-sign-out-alt me-2"></i>Cerrar sesión
                </button>
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
            :usuario="usuario"
            @cancelar="mostrarModalCancelacion"
          />

          <FormularioFeedback 
            v-else-if="paginaActual === 'feedback'"
            :canchas="canchas"
            :feedbacks="feedbacks"
            :usuario="usuario"
            @enviar="agregarFeedback"
          />
        </transition>
      </div>

      <!-- Modal de Reserva -->
      <ModalReserva 
        :canchaSeleccionada="canchaSeleccionada"
        :usuario="usuario"
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
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Login from './components/Login.vue';
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

// Estado de login
const logueado = ref(false);

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

const usuario = ref(null);

// Función para cargar todos los datos necesarios
async function cargarDatos() {
  try {
    canchas.value = await cargarCanchas();
    const userId = usuario.value?.id_usuario;
    reservas.value = await cargarReservas(userId);
    feedbacks.value = await cargarFeedbacks();
    console.log(`📊 Datos cargados: ${canchas.value.length} canchas, ${reservas.value.length} reservas, ${feedbacks.value.length} feedbacks`);
  } catch (e) {
    console.error('Error cargando datos:', e);
  }
}

function manejarLogin(user) {
  usuario.value = user; // guardar el objeto completo del usuario
  logueado.value = true;
  // Guardar usuario en localStorage para persistencia
  localStorage.setItem('usuario', JSON.stringify(user));
  // Cargar datos después del login
  cargarDatos();
}

// Referencias a modals
const modalReserva = ref(null);

function cerrarSesion() {
  localStorage.removeItem('token');
  localStorage.removeItem('user_id');
  localStorage.removeItem('usuario');
  usuario.value = null;
  logueado.value = false;
  paginaActual.value = 'listado'; // opcional
}


// Cargar datos al montar el componente
onMounted(async () => {
  // Intentar restaurar usuario desde localStorage
  const usuarioGuardado = localStorage.getItem('usuario');
  if (usuarioGuardado) {
    try {
      usuario.value = JSON.parse(usuarioGuardado);
      logueado.value = true;
      // Cargar datos si estamos logueados
      await cargarDatos();
    } catch (e) {
      console.error('Error restaurando usuario:', e);
      localStorage.removeItem('usuario');
    }
  }
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

async function agregarReserva(nuevaReserva) {
  // nuevaReserva: { id (tmp), nombre, canchaId, fecha, hora }
  if (!usuario.value?.id_usuario) {
    alert('Debes iniciar sesión para reservar');
    return;
  }

  const cancha = canchas.value.find(c => c.id === nuevaReserva.canchaId);
  const precioHora = cancha?.precio ?? 0;
  
  const result = await guardarReserva({
    usuarioId: usuario.value.id_usuario,
    canchaId: nuevaReserva.canchaId,
    fecha: nuevaReserva.fecha,
    hora: nuevaReserva.hora,
    precioHora
  });

  if (!result.success) {
    alert(`No se pudo crear la reserva: ${result.error}`);
    return;
  }

  // Refrescar reservas desde API para mantener consistencia
  reservas.value = await cargarReservas(usuario.value.id_usuario);
  alert('¡Reserva realizada con éxito!');
  cambiarPagina('reservas');
}

function mostrarModalCancelacion(idReserva) {
  idReservaACancelar.value = idReserva;
  
  const modalElement = document.getElementById('modalCancelar');
  const modal = new window.bootstrap.Modal(modalElement);
  modal.show();
}

async function confirmarCancelacion() {
  if (!idReservaACancelar.value) return;

  const resp = await cancelarReserva(idReservaACancelar.value);
  if (!resp.success) {
    alert(`No se pudo cancelar la reserva: ${resp.error}`);
    return;
  }

  // Refrescar lista
  if (usuario.value?.id_usuario) {
    reservas.value = await cargarReservas(usuario.value.id_usuario);
  } else {
    reservas.value = await cargarReservas();
  }

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
async function agregarFeedback(nuevoFeedback) {
  if (!usuario.value?.id_usuario) {
    alert('Debes iniciar sesión para dejar una opinión');
    return;
  }

  const fechaActual = new Date();
  const fechaFormateada = fechaActual.toISOString().split('T')[0]; // YYYY-MM-DD

  const resp = await guardarFeedback({
    usuarioId: usuario.value.id_usuario,
    canchaId: nuevoFeedback.canchaId,
    calificacion: nuevoFeedback.calificacion,
    comentario: nuevoFeedback.comentario,
    fechaPreferida: fechaFormateada
  });

  if (!resp.success) {
    alert(`No se pudo guardar tu opinión: ${resp.error}`);
    return;
  }

  // Refrescar feedbacks desde API
  feedbacks.value = await cargarFeedbacks();
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

<template>
  <div class="d-flex justify-content-center align-items-center vh-100">
    <div class="row w-75">
      <!-- Cuadro de Login -->
      <div class="col-md-6">
        <div class="card shadow">
          <div class="card-body">
            <h5 class="card-title mb-3">Iniciar sesión</h5>
            <form @submit.prevent="onLogin">
              <div class="mb-3">
                <label>Email</label>
                <input v-model="loginEmail" type="email" class="form-control" required />
              </div>
              <div class="mb-3">
                <label>Password</label>
                <input v-model="loginPassword" type="password" class="form-control" required />
              </div>
              <button class="btn btn-primary w-100" :disabled="loading">
                {{ loading ? 'Cargando...' : 'Ingresar' }}
              </button>
              <p v-if="error" class="text-danger mt-2">{{ error }}</p>
            </form>
          </div>
        </div>
      </div>

      <!-- Cuadro de Registro -->
      <div class="col-md-6">
        <div class="card shadow">
          <div class="card-body">
            <h5 class="card-title mb-3">Registrarse</h5>
            <form @submit.prevent="onRegister">
              <div class="mb-3">
                <label>Nombre</label>
                <input v-model="regNombre" type="text" class="form-control" required />
              </div>
              <div class="mb-3">
                <label>Email</label>
                <input v-model="regEmail" type="email" class="form-control" required />
              </div>
              <div class="mb-3">
                <label>Teléfono</label>
                <input v-model="regTelefono" type="text" class="form-control" required />
              </div>
              <div class="mb-3">
                <label>Password</label>
                <input v-model="regPassword" type="password" class="form-control" required />
              </div>
              <button class="btn btn-success w-100" :disabled="loading">
                {{ loading ? 'Cargando...' : 'Registrarse' }}
              </button>
              <p v-if="error" class="text-danger mt-2">{{ error }}</p>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { login, register, getUserById } from '@/services/auth';

const loginEmail = ref('');
const loginPassword = ref('');
const regNombre = ref('');
const regEmail = ref('');
const regTelefono = ref('');
const regPassword = ref('');

const loading = ref(false);
const error = ref('');

const emit = defineEmits(['login-exitoso']);

async function onLogin() {
  loading.value = true;
  error.value = '';
  try {
    const data = await login({ email: loginEmail.value, password: loginPassword.value });
    const user = await getUserById(data.user_id);
    emit('login-exitoso', user);
  } catch (e) {
    error.value = e.response?.data?.detail || 'Error al iniciar sesión';
  } finally {
    loading.value = false;
  }
}

async function onRegister() {
  loading.value = true;
  error.value = '';
  try {
    // 1. Registrar usuario
    const nuevoUsuario = await register({
      nombre: regNombre.value,
      email: regEmail.value,
      telefono: regTelefono.value,
      password: regPassword.value,
    });
    console.log('Usuario registrado:', nuevoUsuario);

    // 2. Hacer login inmediatamente con email + password
    const data = await login({
      email: regEmail.value,
      password: regPassword.value,
    });

    // 3. Obtener datos del usuario con el user_id del login
    const user = await getUserById(data.user_id);

    // 4. Emitir login exitoso → App.vue muestra dashboard
    emit('login-exitoso', user);
  } catch (e) {
    error.value = e.response?.data?.detail || 'Error al registrarse';
  } finally {
    loading.value = false;
  }
}
</script>





<style scoped>
.login-container {
  max-width: 400px;
  margin: 80px auto;
  color: #333;
}
</style>

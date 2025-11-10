<template>
  <div class="login-container">
    <h1>Iniciar Sesión</h1>
    <form @submit.prevent="onSubmit" class="card p-4">
      <div class="mb-3">
        <label>Email</label>
        <input v-model="email" type="email" class="form-control" required />
      </div>
      <div class="mb-3">
        <label>Contraseña</label>
        <input v-model="password" type="password" class="form-control" required />
      </div>
      <button class="btn btn-primary w-100" :disabled="loading">
        {{ loading ? 'Ingresando...' : 'Entrar' }}
      </button>
      <p v-if="error" class="text-danger mt-2">{{ error }}</p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { login, me } from '@/services/auth';

const email = ref('');
const password = ref('');
const loading = ref(false);
const error = ref('');

const emit = defineEmits(['login-exitoso']);

async function onSubmit() {
  loading.value = true;
  error.value = '';
  try {
    // Llamada al backend
    const data = await login({ email: email.value, password: password.value });
    localStorage.setItem('token', data.access_token);

    // Opcional: obtener datos del usuario
    const user = await me();
    console.log('Usuario autenticado:', user);

    // Avisar al App.vue que el login fue exitoso
    emit('login-exitoso');
  } catch (e) {
    error.value = e.response?.data?.detail || 'Credenciales inválidas';
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

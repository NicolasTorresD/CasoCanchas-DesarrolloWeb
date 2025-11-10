// src/services/auth.js
import backend from './backend';

export async function login(payload) {
  // ahora usamos la ruta completa
  const { data } = await backend.post('/api/v1/auth/login', payload);
  return data; // { access_token, token_type }
}

export async function me() {
  const { data } = await backend.get('/api/v1/users/me'); // ajusta si tu backend expone /api/v1/users/me
  return data;
}

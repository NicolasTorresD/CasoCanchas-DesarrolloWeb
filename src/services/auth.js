// src/services/auth.js
import backend from './backend';

export async function login(payload) {
  // POST al login
  const { data } = await backend.post('/api/v1/auth/login', payload);
  return data; // { access_token, token_type, user_id }
}

export async function getUserById(id) {
  // GET al usuario por id
  const { data } = await backend.get(`/api/v1/users/${id}`);
  return data;
}

export async function register(payload) {
  const { data } = await backend.post('/api/v1/auth/register', payload);
  return data; // { access_token, token_type, user_id }
}

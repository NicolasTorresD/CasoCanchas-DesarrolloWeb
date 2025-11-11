/**
 * Servicio de API para manejo de datos
 * Separa la lógica de comunicación con APIs externas y datos locales
 */

import backend from './backend';

// Configuración de la API de clima usando variables de entorno
const CLIMA_CONFIG = {
  baseUrl: import.meta.env.VITE_CLIMA_API_URL || 'https://api.open-meteo.com/v1/forecast',
  latitude: import.meta.env.VITE_CLIMA_LATITUDE || -33.4489,  // Santiago, Chile
  longitude: import.meta.env.VITE_CLIMA_LONGITUDE || -70.6693,
  timezone: import.meta.env.VITE_CLIMA_TIMEZONE || 'America/Santiago'
};

/**
 * Carga datos JSON desde archivos locales
 */
export async function cargarCanchas() {
  try {
    const { data } = await backend.get('/api/v1/canchas');
    return data; // array de canchas
  } catch (error) {
    console.error('Error cargando canchas:', error);
    return [];
  }
}

export async function cargarReservas() {
  try {
    const { data } = await backend.get('/api/v1/reservas');
    return data;
  } catch (error) {
    console.error('Error cargando reservas:', error);
    return [];
  }
  
}

export async function cargarFeedbacks() {
  try {
    const { data } = await backend.get('/api/v1/feedbacks');
    return data;
  } catch (error) {
    console.error('Error cargando feedbacks:', error);
    return [];
  }
}

export async function cargarDeportes() {
  try {
    const { data } = await backend.get('/api/v1/deportes');
    return data; // array de deportes [{ id_deporte: 1, nombre: "futbol" }, ...]
  } catch (error) {
    console.error('Error cargando deportes:', error);
    return [];
  }
}

/**
 * Obtiene información del clima para una fecha específica
 * @param {string} fecha - Fecha en formato YYYY-MM-DD
 * @returns {Promise<Object>} Datos del clima
 */
export async function obtenerClima(fecha) {
  if (!fecha) {
    return {
      success: false,
      error: 'Fecha no válida'
    };
  }

  const fechaObj = new Date(fecha + 'T12:00:00');
  const hoy = new Date();
  hoy.setHours(0, 0, 0, 0);
  const fechaSeleccionada = new Date(fechaObj);
  fechaSeleccionada.setHours(0, 0, 0, 0);

  const esFuturo = fechaSeleccionada >= hoy;

  try {
    let url;
    if (esFuturo) {
      url = `${CLIMA_CONFIG.baseUrl}?latitude=${CLIMA_CONFIG.latitude}&longitude=${CLIMA_CONFIG.longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,weathercode&timezone=${CLIMA_CONFIG.timezone}&forecast_days=7`;
    } else {
      url = `${CLIMA_CONFIG.baseUrl}?latitude=${CLIMA_CONFIG.latitude}&longitude=${CLIMA_CONFIG.longitude}&daily=temperature_2m_max,temperature_2m_min,weathercode&timezone=${CLIMA_CONFIG.timezone}&past_days=7`;
    }

    const response = await fetch(url);
    if (!response.ok) {
      throw new Error('Error al obtener datos del clima');
    }

    const data = await response.json();
    const fechaBuscada = fecha;
    const indice = data.daily.time.indexOf(fechaBuscada);

    if (indice === -1) {
      return {
        success: false,
        error: 'No hay datos disponibles para esta fecha'
      };
    }

    return {
      success: true,
      data: {
        fecha: fechaBuscada,
        temperaturaMax: data.daily.temperature_2m_max[indice],
        temperaturaMin: data.daily.temperature_2m_min[indice],
        probabilidadPrecipitacion: data.daily.precipitation_probability_max ? 
          data.daily.precipitation_probability_max[indice] : 0,
        codigoClima: data.daily.weathercode[indice]
      }
    };
  } catch (error) {
    console.error('Error obteniendo clima:', error);
    return {
      success: false,
      error: 'Error al conectar con el servicio de clima'
    };
  }
}

/**
 * Mapea códigos de clima de Open-Meteo a descripciones en español
 */
export function obtenerDescripcionClima(codigo) {
  const descripciones = {
    0: 'Despejado',
    1: 'Principalmente despejado',
    2: 'Parcialmente nublado',
    3: 'Nublado',
    45: 'Niebla',
    48: 'Niebla con escarcha',
    51: 'Llovizna ligera',
    53: 'Llovizna moderada',
    55: 'Llovizna intensa',
    61: 'Lluvia ligera',
    63: 'Lluvia moderada',
    65: 'Lluvia intensa',
    71: 'Nevada ligera',
    73: 'Nevada moderada',
    75: 'Nevada intensa',
    77: 'Granizo',
    80: 'Chubascos ligeros',
    81: 'Chubascos moderados',
    82: 'Chubascos intensos',
    85: 'Nevadas ligeras',
    86: 'Nevadas intensas',
    95: 'Tormenta',
    96: 'Tormenta con granizo ligero',
    99: 'Tormenta con granizo intenso'
  };
  return descripciones[codigo] || 'Desconocido';
}

/**
 * Obtiene el icono apropiado para el código de clima
 */
export function obtenerIconoClima(codigo) {
  if (codigo === 0 || codigo === 1) return '☀️';
  if (codigo === 2 || codigo === 3) return '⛅';
  if (codigo === 45 || codigo === 48) return '🌫️';
  if (codigo >= 51 && codigo <= 55) return '🌦️';
  if (codigo >= 61 && codigo <= 65) return '🌧️';
  if (codigo >= 71 && codigo <= 77) return '❄️';
  if (codigo >= 80 && codigo <= 82) return '🌧️';
  if (codigo >= 85 && codigo <= 86) return '❄️';
  if (codigo >= 95 && codigo <= 99) return '⛈️';
  return '🌤️';
}

/**
 * Guarda una nueva reserva (simulado con localStorage)
 */
export async function guardarReserva(reserva) {
  try {
    const { data } = await backend.post('/api/v1/reservas', reserva);
    return data;
  } catch (error) {
    console.error('Error creando reserva:', error);
    throw error;
  }
}

/**
 * Cancela una reserva por ID
 */
export async function cancelarReservaBackend(id_reserva) {
  try {
    await backend.delete(`/api/v1/reservas/${id_reserva}`);
    return { success: true };
  } catch (error) {
    console.error('Error cancelando reserva en backend:', error);
    return { success: false, error: 'No se pudo cancelar la reserva' };
  }
}

/**
 * Guarda un nuevo feedback
 */
export function guardarFeedback(feedback) {
  try {
    const feedbacksGuardados = JSON.parse(localStorage.getItem('feedbacks') || '[]');
    feedbacksGuardados.push(feedback);
    localStorage.setItem('feedbacks', JSON.stringify(feedbacksGuardados));
    return { success: true };
  } catch (error) {
    console.error('Error guardando feedback:', error);
    return { success: false, error: 'Error al guardar el comentario' };
  }
}

export async function enviarFeedback(reservaId, usuarioId, payload) {
  try {
    const response = await backend.post(
      `/api/v1/feedbacks/reserva/${reservaId}?usuario_id=${usuarioId}`,
      payload
    );
    return response.data;
  } catch (error) {
    console.error("Error enviando feedback:", error);
    throw error;
  }
}

export async function cargarFeedbacksPorCancha(id_cancha) {
  try {
    const response = await backend.get(`/api/v1/feedbacks/cancha/${id_cancha}`);
    return response.data;
  } catch (error) {
    console.error("Error cargando feedbacks de cancha:", error);
    return [];
  }
}



/**
 * Servicio de API para manejo de datos
 * Separa la lógica de comunicación con APIs externas y datos locales
 */

// Configuración de la API de clima
const CLIMA_CONFIG = {
  baseUrl: 'https://api.open-meteo.com/v1/forecast',
  latitude: -33.4489,  // Santiago, Chile
  longitude: -70.6693,
  timezone: 'auto'
};

/**
 * Carga datos JSON desde archivos locales
 */
export async function cargarCanchas() {
  try {
    const response = await fetch('/canchas.json');
    if (!response.ok) throw new Error('Error al cargar canchas');
    return await response.json();
  } catch (error) {
    console.error('Error cargando canchas:', error);
    return [];
  }
}

export async function cargarReservas() {
  try {
    const response = await fetch('/reservas.json');
    if (!response.ok) throw new Error('Error al cargar reservas');
    return await response.json();
  } catch (error) {
    console.error('Error cargando reservas:', error);
    return [];
  }
}

export async function cargarFeedbacks() {
  try {
    const response = await fetch('/feedbacks.json');
    if (!response.ok) throw new Error('Error al cargar feedbacks');
    return await response.json();
  } catch (error) {
    console.error('Error cargando feedbacks:', error);
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
export function guardarReserva(reserva) {
  try {
    const reservasGuardadas = JSON.parse(localStorage.getItem('reservas') || '[]');
    reservasGuardadas.push(reserva);
    localStorage.setItem('reservas', JSON.stringify(reservasGuardadas));
    return { success: true };
  } catch (error) {
    console.error('Error guardando reserva:', error);
    return { success: false, error: 'Error al guardar la reserva' };
  }
}

/**
 * Cancela una reserva por ID
 */
export function cancelarReserva(id) {
  try {
    const reservasGuardadas = JSON.parse(localStorage.getItem('reservas') || '[]');
    const reservasFiltradas = reservasGuardadas.filter(r => r.id !== id);
    localStorage.setItem('reservas', JSON.stringify(reservasFiltradas));
    return { success: true };
  } catch (error) {
    console.error('Error cancelando reserva:', error);
    return { success: false, error: 'Error al cancelar la reserva' };
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

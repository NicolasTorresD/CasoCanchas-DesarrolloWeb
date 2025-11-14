/**
 * Servicio de API para manejo de datos
 * - Clima: servicio público Open-Meteo
 * - Datos de negocio (canchas, reservas, feedbacks): FastAPI (MySQL)
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
    // Traer canchas y deportes para mapear id_deporte -> nombre
    const [canchasRes, deportesRes] = await Promise.all([
      backend.get('/api/v1/canchas'),
      backend.get('/api/v1/deportes')
    ]);

    const deportesMap = new Map(
      (deportesRes.data || []).map((d) => [d.id_deporte, d.nombre])
    );

    // Adaptar el payload del backend al formato esperado por la UI
    return (canchasRes.data || []).map((c) => ({
      id: c.id_cancha,
      codigo: c.codigo,
      nombre: c.nombre,
      deporte: deportesMap.get(c.id_deporte) || 'desconocido',
      imagen: c.imagen_url || '',
      color: c.color || '#000000',
      precio: Number(c.precio_hora), // La UI lo multiplica x1000 al mostrar
      disponibilidad: [] // TODO: integrar horarios/ocupación real si se requiere filtrar por fecha
    }));
  } catch (error) {
    console.error('Error cargando canchas desde API:', error);
    return [];
  }
}

export async function cargarReservas(usuarioId) {
  try {
    const url = usuarioId
      ? `/api/v1/reservas?usuario_id=${encodeURIComponent(usuarioId)}`
      : '/api/v1/reservas';
    const { data } = await backend.get(url);
    // Adaptar al formato esperado por la UI
    return (data || []).map((r) => ({
      id: r.id_reserva,
      // nombre: lo muestra la UI con el usuario logueado, no viene en la reserva
      canchaId: r.id_cancha,
      fecha: r.fecha,
      hora: r.hora
    }));
  } catch (error) {
    console.error('Error cargando reservas desde API:', error);
    return [];
  }
}

export async function cargarFeedbacks() {
  try {
    const { data } = await backend.get('/api/v1/feedbacks');
    // Adaptar: la API devuelve ids; la UI espera usuario (string) para mostrar
    // Mostramos sin nombre de usuario y mapeamos campos clave usados (canchaId, calificacion, fecha)
    return (data || []).map((f) => ({
      id: f.id_feedback,
      usuario: f.usuario_nombre || '',
      canchaId: f.id_cancha,
      calificacion: f.calificacion,
      comentario: f.comentario || '',
      fecha: f.fecha
    }));
  } catch (error) {
    console.error('Error cargando feedbacks desde API:', error);
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
export async function guardarReserva({ usuarioId, canchaId, fecha, hora, precioHora }) {
  try {
    const payload = {
      id_usuario: Number(usuarioId),
      id_cancha: Number(canchaId),
      fecha,
      hora,
      duracion: 60, // minutos
      estado: 'Reservada',
      precio_total: Number(precioHora ?? 0)
    };
    const { data } = await backend.post('/api/v1/reservas', payload);
    return { success: true, data };
  } catch (error) {
    console.error('Error guardando reserva en API:', error?.response?.data || error);
    const detail = error?.response?.data?.detail || 'Error al guardar la reserva';
    return { success: false, error: detail };
  }
}

/**
 * Cancela una reserva por ID
 */
export async function cancelarReserva(id) {
  try {
    const { data } = await backend.delete(`/api/v1/reservas/${id}`);
    return { success: true, data };
  } catch (error) {
    console.error('Error cancelando reserva en API:', error?.response?.data || error);
    const detail = error?.response?.data?.detail || 'Error al cancelar la reserva';
    return { success: false, error: detail };
  }
}

/**
 * Guarda un nuevo feedback
 */
// NOTA: crear feedback en API requiere id_reserva. La UI actual no lo solicita.
// Dejamos este método como no implementado hacia el backend por ahora y
// podríamos ampliarlo más adelante vinculando feedbacks a reservas del usuario.
export async function guardarFeedback({ usuarioId, canchaId, calificacion, comentario, fechaPreferida }) {
  try {
    // 1) Obtener reservas del usuario
    const { data: reservasUsuario } = await backend.get(`/api/v1/reservas?usuario_id=${encodeURIComponent(usuarioId)}`);
    if (!reservasUsuario || reservasUsuario.length === 0) {
      return { success: false, error: 'No tienes reservas asociadas para dejar un comentario' };
    }

    // 2) Intentar encontrar una reserva para esa cancha; si se provee fechaPreferida (YYYY-MM-DD), priorizar esa
    let candidata = null;
    const mismasCancha = reservasUsuario.filter(r => r.id_cancha === Number(canchaId));
    if (mismasCancha.length === 0) {
      return { success: false, error: 'No encontramos una reserva tuya para esa cancha' };
    }

    if (fechaPreferida) {
      candidata = mismasCancha.find(r => r.fecha === fechaPreferida) || null;
    }
    // Si no se indicó fecha o no se encontró, tomar la más reciente por fecha
    if (!candidata) {
      candidata = [...mismasCancha].sort((a, b) => (a.fecha < b.fecha ? 1 : -1))[0];
    }

    if (!candidata) {
      return { success: false, error: 'No encontramos una reserva válida para asociar el feedback' };
    }

    // 3) Crear feedback en API
    const body = { calificacion: Number(calificacion), comentario: comentario || '' };
    const { data } = await backend.post(`/api/v1/feedbacks/reserva/${candidata.id_reserva}?usuario_id=${encodeURIComponent(usuarioId)}`, body);
    return { success: true, data };
  } catch (error) {
    console.error('Error guardando feedback en API:', error?.response?.data || error);
    const detail = error?.response?.data?.detail || 'Error al guardar el comentario';
    return { success: false, error: detail };
  }
}

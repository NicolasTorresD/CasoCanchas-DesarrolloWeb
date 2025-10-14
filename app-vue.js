const { createApp, ref, computed, onMounted, watch } = Vue;

createApp({
    setup() {
        const canchas = ref([]);
        const reservas = ref([]);
        const feedbacks = ref([]);
        const idReservaACancelar = ref(null);
        const calificacionSeleccionada = ref(0);

        const filtroDeporte = ref('todos');
        const filtroFecha = ref('');

        const nombreReserva = ref('');
        const canchaSeleccionadaNombre = ref('');
        const canchaSeleccionadaId = ref('');
        const fechaReserva = ref('');
        const horaReserva = ref('');

        const usuarioFeedback = ref('');
        const canchaFeedback = ref('');
        const comentarioFeedback = ref('');

        // Variables para clima
        const climaData = ref(null);
        const climaCargando = ref(false);
        const climaError = ref(null);

        function obtenerNombreCanchaPorId(canchaId) {
            const cancha = canchas.value.find(c => c.id === canchaId);
            return cancha ? cancha.nombre : canchaId;
        }

        function calcularPromedioCalificacion(canchaId) {
            const feedbacksCancha = feedbacks.value.filter(f => f.canchaId === canchaId);
            if (feedbacksCancha.length === 0) return 0;
            const suma = feedbacksCancha.reduce((total, feedback) => total + feedback.calificacion, 0);
            return (suma / feedbacksCancha.length).toFixed(1);
        }

        function generarEstrellas(calificacion) {
            let estrellas = '';
            const calificacionRedondeada = Math.round(calificacion);
            for (let i = 1; i <= 5; i++) {
                if (i <= calificacionRedondeada) {
                    estrellas += '<i class="fas fa-star"></i>';
                } else {
                    estrellas += '<i class="far fa-star"></i>';
                }
            }
            return estrellas;
        }

        const canchasFiltradas = computed(() => {
            let lista = [...canchas.value];
            if (filtroDeporte.value !== 'todos') {
                lista = lista.filter(c => c.deporte === filtroDeporte.value);
            }
            if (filtroFecha.value) {
                lista = lista.filter(cancha => {
                    const reservasEnFecha = reservas.value.filter(reserva => 
                        reserva.canchaId === cancha.id && 
                        reserva.fecha === filtroFecha.value && 
                        reserva.estado === 'Reservada'
                    );
                    return reservasEnFecha.length === 0;
                });
            }
            return lista;
        });

        // Renderizar canchas cuando cambien los datos o filtros
        function renderizarCanchas() {
            const listado = document.getElementById('canchas-listado');
            if (!listado) return;
            
            listado.innerHTML = '';
            
            if (canchasFiltradas.value.length === 0) {
                listado.innerHTML = '<p class="text-center text-light mt-4">No hay canchas disponibles con los filtros seleccionados.</p>';
                return;
            }
            
            canchasFiltradas.value.forEach(cancha => {
                const promedio = calcularPromedioCalificacion(cancha.id);
                const estrellas = generarEstrellas(promedio);
                const totalFeedbacks = feedbacks.value.filter(f => f.canchaId === cancha.id).length;
                
                const card = document.createElement('div');
                card.className = 'col-md-4 mb-4';
                card.setAttribute('data-deporte', cancha.deporte);
                card.innerHTML = `
                    <div class="card h-100">
                        <img src="${cancha.imagen}" class="card-img-top" alt="${cancha.nombre}">
                        ${promedio > 0 ? `
                        <div class="card-rating" onclick="window.mostrarComentarios('${cancha.id}')" data-bs-toggle="modal" data-bs-target="#comentariosModal" style="cursor: pointer;">
                            ${estrellas} ${promedio} (${totalFeedbacks})
                        </div>
                        ` : ''}
                        <div class="card-body">
                            <h5 class="card-title fw-bold">${cancha.nombre}</h5>
                            <p class="card-text text-muted">Deporte: ${cancha.deporte.charAt(0).toUpperCase() + cancha.deporte.slice(1)}</p>
                            <button class="btn w-100 btn-rounded reservar-btn" style="background-color: ${cancha.color}; border-color: ${cancha.color};" data-cancha-id="${cancha.id}" data-cancha-nombre="${cancha.nombre}">Reservar</button>
                        </div>
                    </div>
                `;
                listado.appendChild(card);
            });
            
            // Agregar event listeners a los botones de reservar
            document.querySelectorAll('.reservar-btn').forEach(button => {
                button.addEventListener('click', function() {
                    const canchaId = this.getAttribute('data-cancha-id');
                    const canchaNombre = this.getAttribute('data-cancha-nombre');
                    prepararReserva(canchaId, canchaNombre);
                });
            });
        }

        // Watch para re-renderizar cuando cambien las canchas o feedbacks
        watch([canchas, feedbacks, canchasFiltradas], () => {
            renderizarCanchas();
        });

        async function cargarCanchasDesdeJSON() {
            try {
                const response = await fetch('canchas.json');
                if (!response.ok) throw new Error(`Error HTTP: ${response.status}`);
                canchas.value = await response.json();
            } catch (error) {
                console.error('Error al cargar canchas:', error);
            }
        }

        async function cargarReservasDesdeJSON() {
            try {
                const response = await fetch('reservas.json');
                if (!response.ok) throw new Error(`Error HTTP: ${response.status}`);
                reservas.value = await response.json();
            } catch (error) {
                console.error('Error al cargar reservas:', error);
                reservas.value = [];
            }
        }

        async function cargarFeedbacksDesdeJSON() {
            try {
                const response = await fetch('feedbacks.json');
                if (!response.ok) throw new Error(`Error HTTP: ${response.status}`);
                feedbacks.value = await response.json();
            } catch (error) {
                console.error('Error al cargar feedbacks:', error);
                feedbacks.value = [];
            }
        }

        async function obtenerClima(fecha) {
            if (!fecha) {
                climaData.value = null;
                return;
            }

            climaCargando.value = true;
            climaError.value = null;

            try {
                // Usando coordenadas de Santiago, Chile (puedes cambiarlas a tu ubicación)
                const latitud = -33.4489;
                const longitud = -70.6693;
                
                const fechaObj = new Date(fecha + 'T00:00:00');
                const hoy = new Date();
                hoy.setHours(0, 0, 0, 0);
                
                // Determinar si es pronóstico o datos históricos
                const esFuturo = fechaObj >= hoy;
                
                let url;
                if (esFuturo) {
                    // API de pronóstico (hasta 7 días)
                    url = `https://api.open-meteo.com/v1/forecast?latitude=${latitud}&longitude=${longitud}&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max,weathercode&timezone=auto&forecast_days=7`;
                } else {
                    // API de datos históricos
                    url = `https://api.open-meteo.com/v1/forecast?latitude=${latitud}&longitude=${longitud}&daily=temperature_2m_max,temperature_2m_min,weathercode&timezone=auto&past_days=7`;
                }

                console.log('Obteniendo clima para fecha:', fecha);
                console.log('URL API:', url);

                const response = await fetch(url);
                if (!response.ok) throw new Error(`Error HTTP: ${response.status}`);
                
                const data = await response.json();
                console.log('Datos de clima recibidos:', data);

                // Buscar el índice de la fecha seleccionada
                const fechaIndex = data.daily.time.findIndex(d => d === fecha);
                
                if (fechaIndex === -1) {
                    throw new Error('Fecha no disponible en el pronóstico');
                }

                // Obtener descripción del código del clima
                const weathercode = data.daily.weathercode[fechaIndex];
                const descripcion = obtenerDescripcionClima(weathercode);
                const icono = obtenerIconoClima(weathercode);

                climaData.value = {
                    fecha: fecha,
                    tempMax: Math.round(data.daily.temperature_2m_max[fechaIndex]),
                    tempMin: Math.round(data.daily.temperature_2m_min[fechaIndex]),
                    precipitacion: data.daily.precipitation_probability_max ? data.daily.precipitation_probability_max[fechaIndex] : 0,
                    descripcion: descripcion,
                    icono: icono,
                    weathercode: weathercode
                };

                console.log('Clima procesado:', climaData.value);

            } catch (error) {
                console.error('Error al obtener clima:', error);
                climaError.value = 'No se pudo obtener información del clima';
                climaData.value = null;
            } finally {
                climaCargando.value = false;
            }
        }

        function obtenerDescripcionClima(code) {
            const descripciones = {
                0: 'Despejado',
                1: 'Principalmente despejado',
                2: 'Parcialmente nublado',
                3: 'Nublado',
                45: 'Neblina',
                48: 'Neblina con escarcha',
                51: 'Llovizna ligera',
                53: 'Llovizna moderada',
                55: 'Llovizna intensa',
                61: 'Lluvia ligera',
                63: 'Lluvia moderada',
                65: 'Lluvia intensa',
                71: 'Nieve ligera',
                73: 'Nieve moderada',
                75: 'Nieve intensa',
                77: 'Granizo',
                80: 'Chubascos ligeros',
                81: 'Chubascos moderados',
                82: 'Chubascos intensos',
                85: 'Nieve ligera',
                86: 'Nieve intensa',
                95: 'Tormenta',
                96: 'Tormenta con granizo ligero',
                99: 'Tormenta con granizo intenso'
            };
            return descripciones[code] || 'Condiciones variables';
        }

        function obtenerIconoClima(code) {
            if (code === 0 || code === 1) return '☀️';
            if (code === 2) return '⛅';
            if (code === 3) return '☁️';
            if (code >= 45 && code <= 48) return '🌫️';
            if (code >= 51 && code <= 55) return '🌦️';
            if (code >= 61 && code <= 65) return '🌧️';
            if (code >= 71 && code <= 77) return '❄️';
            if (code >= 80 && code <= 82) return '🌧️';
            if (code >= 85 && code <= 86) return '🌨️';
            if (code >= 95 && code <= 99) return '⛈️';
            return '🌤️';
        }

        function actualizarUIClima() {
            const climaContainer = document.getElementById('clima-container');
            const climaCargandoEl = document.getElementById('clima-cargando');
            const climaDataEl = document.getElementById('clima-data');
            const climaErrorEl = document.getElementById('clima-error');

            if (!climaContainer) return;

            // Mostrar/ocultar contenedor principal
            if (climaCargando.value || climaData.value || climaError.value) {
                climaContainer.style.display = 'block';
            } else {
                climaContainer.style.display = 'none';
                return;
            }

            // Mostrar estado de carga
            if (climaCargando.value) {
                climaCargandoEl.style.display = 'block';
                climaDataEl.style.display = 'none';
                climaErrorEl.style.display = 'none';
                return;
            }

            // Mostrar error
            if (climaError.value) {
                climaCargandoEl.style.display = 'none';
                climaDataEl.style.display = 'none';
                climaErrorEl.style.display = 'block';
                return;
            }

            // Mostrar datos del clima
            if (climaData.value) {
                climaCargandoEl.style.display = 'none';
                climaDataEl.style.display = 'block';
                climaErrorEl.style.display = 'none';

                document.getElementById('clima-icono').textContent = climaData.value.icono;
                document.getElementById('clima-descripcion').textContent = climaData.value.descripcion;
                document.getElementById('clima-temp-max').textContent = climaData.value.tempMax;
                document.getElementById('clima-temp-min').textContent = climaData.value.tempMin;

                // Mostrar probabilidad de precipitación si está disponible
                if (climaData.value.precipitacion > 0) {
                    document.getElementById('clima-precipitacion').textContent = climaData.value.precipitacion;
                    document.getElementById('clima-precipitacion-container').style.display = 'block';
                } else {
                    document.getElementById('clima-precipitacion-container').style.display = 'none';
                }
            }
        }

        // Watch para actualizar UI cuando cambien los datos del clima
        watch([climaCargando, climaData, climaError], () => {
            actualizarUIClima();
        });

        function showPage(pageId) {
            document.querySelectorAll('.container-page').forEach(page => page.classList.remove('active'));
            document.getElementById(pageId).classList.add('active');
        }

        function generateTimeOptions() {
            const select = document.getElementById('hora-reserva');
            select.innerHTML = '<option value="" disabled selected>Selecciona una hora</option>';
            for (let i = 9; i <= 23; i++) {
                const hour = i < 10 ? '0' + i : i;
                const option = document.createElement('option');
                option.value = `${hour}:00`;
                option.textContent = `${hour}:00`;
                select.appendChild(option);
            }
        }

        function limpiarFormularioCompleto() {
            // Limpiar variables reactivas de Vue
            nombreReserva.value = '';
            canchaSeleccionadaNombre.value = '';
            canchaSeleccionadaId.value = '';
            fechaReserva.value = '';
            horaReserva.value = '';
            
            // Limpiar inputs del DOM
            const nombreInput = document.getElementById('nombre-reserva');
            const canchaInput = document.getElementById('cancha-reserva');
            const fechaInput = document.getElementById('fecha-reserva');
            const horaInput = document.getElementById('hora-reserva');
            
            if (nombreInput) nombreInput.value = '';
            if (canchaInput) {
                canchaInput.value = '';
                canchaInput.removeAttribute('data-cancha-id');
            }
            if (fechaInput) fechaInput.value = '';
            if (horaInput) horaInput.value = '';
            
            // Limpiar formulario de feedback
            const usuarioInput = document.getElementById('usuario-feedback');
            const canchaFeedbackInput = document.getElementById('cancha-feedback');
            const comentarioInput = document.getElementById('comentario-feedback');
            
            if (usuarioInput) usuarioInput.value = '';
            if (canchaFeedbackInput) canchaFeedbackInput.value = '';
            if (comentarioInput) comentarioInput.value = '';
            
            usuarioFeedback.value = '';
            canchaFeedback.value = '';
            comentarioFeedback.value = '';
            calificacionSeleccionada.value = 0;
            
            // Limpiar estrellas de calificación
            document.querySelectorAll('.star-rating').forEach(e => {
                e.classList.remove('filled');
                e.classList.remove('active');
            });
            
            // Limpiar datos del clima
            climaData.value = null;
            climaCargando.value = false;
            climaError.value = null;
            
            console.log('Formulario completamente limpiado');
        }

        function prepararReserva(canchaId, canchaNombre) {
            console.log('Preparando reserva para:', { canchaId, canchaNombre });
            
            // Actualizar valores reactivos de Vue
            canchaSeleccionadaId.value = canchaId;
            canchaSeleccionadaNombre.value = canchaNombre;
            
            // Actualizar el input en el DOM
            const inputCancha = document.getElementById('cancha-reserva');
            if (inputCancha) {
                inputCancha.value = canchaNombre;
                inputCancha.setAttribute('data-cancha-id', canchaId);
            }
            
            // Cambiar a la página de reserva
            showPage('reserva-page');
        }

        function confirmarReserva() {
            const nombreInput = document.getElementById('nombre-reserva').value;
            const canchaInput = document.getElementById('cancha-reserva').value;
            const fechaInput = document.getElementById('fecha-reserva').value;
            const horaInput = document.getElementById('hora-reserva').value;
            
            // Sincronizar valores con Vue
            nombreReserva.value = nombreInput;
            fechaReserva.value = fechaInput;
            
            // Obtener cancha ID del atributo data
            const canchaId = document.getElementById('cancha-reserva').getAttribute('data-cancha-id') || canchaSeleccionadaId.value;
            
            console.log('Validando reserva:', {
                nombre: nombreInput,
                cancha: canchaInput,
                canchaId: canchaId,
                fecha: fechaInput,
                hora: horaInput
            });
            
            if (!nombreInput || !canchaInput || !fechaInput || !horaInput) {
                alert('Por favor, completa todos los campos para la reserva.');
                return;
            }
            
            if (!canchaId) {
                alert('Por favor, selecciona una cancha primero.');
                return;
            }

            const reservaExistente = reservas.value.find(reserva => 
                reserva.canchaId === canchaId && reserva.fecha === fechaInput && reserva.hora === horaInput && reserva.estado === 'Reservada'
            );

            if (reservaExistente) {
                var errorModal = new bootstrap.Modal(document.getElementById('errorModal'));
                errorModal.show();
            } else {
                var confirmacionModal = new bootstrap.Modal(document.getElementById('confirmacionModal'));
                confirmacionModal.show();
            }
        }

        function procesarReserva() {
            const nombreInput = document.getElementById('nombre-reserva').value;
            const fechaInput = document.getElementById('fecha-reserva').value;
            const horaInput = document.getElementById('hora-reserva').value;
            const canchaId = document.getElementById('cancha-reserva').getAttribute('data-cancha-id') || canchaSeleccionadaId.value;
            
            const nuevoId = 'R' + String(reservas.value.length + 1).padStart(3, '0');
            const nuevaReserva = {
                id: nuevoId,
                usuario: nombreInput,
                canchaId: canchaId,
                fecha: fechaInput,
                hora: horaInput,
                estado: 'Reservada'
            };
            
            reservas.value.push(nuevaReserva);
            
            console.log('Reserva creada:', nuevaReserva);
            console.log('Total reservas:', reservas.value.length);
            
            // Limpiar solo nombre, fecha y hora (NO la cancha)
            document.getElementById('nombre-reserva').value = '';
            document.getElementById('fecha-reserva').value = '';
            document.getElementById('hora-reserva').value = '';
            nombreReserva.value = '';
            fechaReserva.value = '';
            
            var confirmacionModal = bootstrap.Modal.getInstance(document.getElementById('confirmacionModal'));
            confirmacionModal.hide();
            var reservaExitosaModal = new bootstrap.Modal(document.getElementById('reservaExitosaModal'));
            reservaExitosaModal.show();
        }

        function cargarReservas() {
            // reactividad: simplemente usar reservas.value
            const listado = document.getElementById('reservas-listado');
            const noReservasMsg = document.getElementById('no-reservas-msg');
            listado.innerHTML = '';

            const reservasActivas = reservas.value.filter(r => r.estado === 'Reservada');
            if (reservasActivas.length === 0) {
                noReservasMsg.style.display = 'block';
                return;
            } else {
                noReservasMsg.style.display = 'none';
            }

            reservasActivas.forEach(reserva => {
                const nombreCancha = obtenerNombreCanchaPorId(reserva.canchaId);
                const item = document.createElement('div');
                item.className = 'reserva-item';
                item.innerHTML = `
                    <div>
                        <strong class="text-warning">${nombreCancha}</strong>
                        <small class="card-text">Usuario: ${reserva.usuario} | Fecha: ${reserva.fecha} | Hora: ${reserva.hora}</small>
                    </div>
                    <button class="btn btn-danger btn-rounded btn-cancelar" data-id="${reserva.id}" data-bs-toggle="modal" data-bs-target="#cancelacionModal"><i class="fas fa-trash-alt me-2"></i>Cancelar</button>
                `;
                listado.appendChild(item);
            });
        }

        function confirmarCancelacion(id) {
            idReservaACancelar.value = id;
        }

        function procesarCancelacion() {
            const reserva = reservas.value.find(r => r.id === idReservaACancelar.value);
            if (reserva) reserva.estado = 'Cancelada';
            cargarReservas();
            var cancelacionModal = bootstrap.Modal.getInstance(document.getElementById('cancelacionModal'));
            cancelacionModal.hide();
            var cancelacionExitosaModal = new bootstrap.Modal(document.getElementById('cancelacionExitosaModal'));
            cancelacionExitosaModal.show();
        }

        function cargarCanchasEnSelect() {
            // poblar select en el DOM
            const select = document.getElementById('cancha-feedback');
            select.innerHTML = '<option value="" disabled selected>Selecciona una cancha</option>';
            canchas.value.forEach(cancha => {
                const option = document.createElement('option');
                option.value = cancha.id;
                option.textContent = cancha.nombre;
                select.appendChild(option);
            });
        }

        function inicializarSistemaCalificacion() {
            const estrellas = document.querySelectorAll('.star-rating');
            estrellas.forEach((estrella, index) => {
                estrella.addEventListener('mouseenter', function() {
                    for (let i = 0; i <= index; i++) estrellas[i].classList.add('active');
                });
                estrella.addEventListener('mouseleave', function() {
                    estrellas.forEach(e => e.classList.remove('active'));
                });
                estrella.addEventListener('click', function() {
                    calificacionSeleccionada.value = index + 1;
                    estrellas.forEach((e, i) => {
                        if (i < calificacionSeleccionada.value) e.classList.add('filled'); else e.classList.remove('filled');
                    });
                });
            });
        }

        function enviarFeedback() {
            // Obtener valores directamente del DOM
            const usuarioInput = document.getElementById('usuario-feedback').value;
            const canchaInput = document.getElementById('cancha-feedback').value;
            const comentarioInput = document.getElementById('comentario-feedback').value;
            
            console.log('Enviando feedback:', {
                usuario: usuarioInput,
                cancha: canchaInput,
                comentario: comentarioInput,
                calificacion: calificacionSeleccionada.value
            });
            
            if (!usuarioInput || !canchaInput || !comentarioInput || calificacionSeleccionada.value === 0) {
                alert('Por favor, completa todos los campos y selecciona una calificación.');
                return;
            }
            
            const nuevoId = 'F' + String(feedbacks.value.length + 1).padStart(3, '0');
            const nuevoFeedback = {
                id: nuevoId,
                usuario: usuarioInput,
                canchaId: canchaInput,
                calificacion: calificacionSeleccionada.value,
                comentario: comentarioInput,
                fecha: new Date().toISOString().split('T')[0],
                timestamp: new Date().toISOString()
            };
            feedbacks.value.push(nuevoFeedback);
            
            console.log('Feedback creado:', nuevoFeedback);
            console.log('Total feedbacks:', feedbacks.value.length);
            
            // Limpiar formulario (DOM y Vue)
            document.getElementById('usuario-feedback').value = '';
            document.getElementById('cancha-feedback').value = '';
            document.getElementById('comentario-feedback').value = '';
            usuarioFeedback.value = '';
            canchaFeedback.value = '';
            comentarioFeedback.value = '';
            calificacionSeleccionada.value = 0;
            document.querySelectorAll('.star-rating').forEach(e => { e.classList.remove('filled'); e.classList.remove('active'); });

            const form = document.getElementById('feedbackForm');
            const successMessage = document.createElement('div');
            successMessage.className = 'feedback-success';
            successMessage.innerHTML = '<i class="fas fa-check-circle me-2"></i>¡Gracias por tu opinión! Tu feedback ha sido enviado correctamente.';
            form.appendChild(successMessage);
            setTimeout(() => successMessage.remove(), 3000);
        }

        function mostrarComentarios(canchaId) {
            const cancha = canchas.value.find(c => c.id === canchaId);
            const feedbacksCancha = feedbacks.value.filter(f => f.canchaId === canchaId);
            document.getElementById('comentariosModalLabel').innerHTML = `<i class="fas fa-comments me-2"></i>Opiniones de ${cancha ? cancha.nombre : ''}`;
            const listado = document.getElementById('comentarios-listado');
            const noComentariosMsg = document.getElementById('no-comentarios-msg');
            listado.innerHTML = '';
            if (feedbacksCancha.length === 0) { noComentariosMsg.style.display = 'block'; return; } else { noComentariosMsg.style.display = 'none'; }
            const feedbacksOrdenados = [...feedbacksCancha].sort((a,b) => new Date(b.timestamp) - new Date(a.timestamp));
            feedbacksOrdenados.forEach(feedback => {
                const item = document.createElement('div');
                item.className = 'comentario-item';
                const estrellas = generarEstrellas(feedback.calificacion);
                item.innerHTML = `\
                    <div class="comentario-header">\
                        <div>\
                            <span class="comentario-usuario">${feedback.usuario}</span>\
                            <div class="rating-stars text-warning mt-1">${estrellas}</div>\
                        </div>\
                        <span class="comentario-fecha">${feedback.fecha}</span>\
                    </div>\
                    <p class="comentario-texto">${feedback.comentario}</p>\
                `;
                listado.appendChild(item);
            });
        }

        // Exponer funciones globalmente necesarias por los atributos inline y modales
        window.mostrarComentarios = mostrarComentarios;
        window.limpiarFormularioCompleto = limpiarFormularioCompleto;
        window.showPage = showPage;

        onMounted(async () => {
            console.log('Vue App montada, cargando datos...');
            
            const today = new Date().toISOString().split('T')[0];
            const fechaFiltroEl = document.getElementById('fecha-filtro');
            const fechaReservaEl = document.getElementById('fecha-reserva');
            if (fechaFiltroEl) fechaFiltroEl.min = today;
            if (fechaReservaEl) fechaReservaEl.min = today;

            // Cargar datos
            await Promise.all([cargarCanchasDesdeJSON(), cargarReservasDesdeJSON(), cargarFeedbacksDesdeJSON()]);
            
            console.log('Datos cargados:', {
                canchas: canchas.value.length,
                reservas: reservas.value.length,
                feedbacks: feedbacks.value.length
            });
            
            // Renderizar canchas inicial
            renderizarCanchas();
            
            generateTimeOptions();
            inicializarSistemaCalificacion();
            
            // Configurar event listeners para navegación
            const setupNavigation = () => {
                // Navegación principal
                document.getElementById('showListado')?.addEventListener('click', (e) => {
                    e.preventDefault();
                    limpiarFormularioCompleto();
                    showPage('listado-page');
                });
                
                document.getElementById('showListado2')?.addEventListener('click', (e) => {
                    e.preventDefault();
                    limpiarFormularioCompleto();
                    showPage('listado-page');
                });
                
                document.getElementById('showListado3')?.addEventListener('click', (e) => {
                    e.preventDefault();
                    limpiarFormularioCompleto();
                    showPage('listado-page');
                });
                
                document.getElementById('showMisReservas')?.addEventListener('click', (e) => {
                    e.preventDefault();
                    limpiarFormularioCompleto();
                    showPage('mis-reservas-page');
                    cargarReservas();
                });
                
                document.getElementById('showMisReservas2')?.addEventListener('click', (e) => {
                    e.preventDefault();
                    limpiarFormularioCompleto();
                    showPage('mis-reservas-page');
                    cargarReservas();
                });
                
                document.getElementById('showMisReservas3')?.addEventListener('click', (e) => {
                    e.preventDefault();
                    limpiarFormularioCompleto();
                    showPage('mis-reservas-page');
                    cargarReservas();
                });
                
                document.getElementById('showFeedback')?.addEventListener('click', (e) => {
                    e.preventDefault();
                    limpiarFormularioCompleto();
                    showPage('feedback-page');
                    cargarCanchasEnSelect();
                });
                
                document.getElementById('showFeedback2')?.addEventListener('click', (e) => {
                    e.preventDefault();
                    limpiarFormularioCompleto();
                    showPage('feedback-page');
                    cargarCanchasEnSelect();
                });
                
                document.getElementById('showFeedback3')?.addEventListener('click', (e) => {
                    e.preventDefault();
                    limpiarFormularioCompleto();
                    showPage('feedback-page');
                    cargarCanchasEnSelect();
                });
                
                // Filtro
                document.getElementById('deporte-filtro')?.addEventListener('change', (e) => {
                    filtroDeporte.value = e.target.value;
                });
                
                document.getElementById('fecha-filtro')?.addEventListener('change', (e) => {
                    filtroFecha.value = e.target.value;
                });
                
                document.getElementById('btnFiltrar')?.addEventListener('click', () => {
                    renderizarCanchas();
                });
                
                // Botón confirmar reserva
                document.getElementById('btnConfirmarReserva')?.addEventListener('click', confirmarReserva);
                
                // Botón procesar reserva
                document.getElementById('btnProcesarReserva')?.addEventListener('click', procesarReserva);
                
                // Botón confirmar cancelación
                document.getElementById('btnConfirmarCancelacion')?.addEventListener('click', procesarCancelacion);
                
                // Botón enviar feedback
                document.getElementById('btnEnviarFeedback')?.addEventListener('click', enviarFeedback);
                
                // Event listener para cancelar reservas
                document.getElementById('reservas-listado')?.addEventListener('click', (e) => {
                    if (e.target.classList.contains('btn-cancelar') || e.target.closest('.btn-cancelar')) {
                        const btn = e.target.classList.contains('btn-cancelar') ? e.target : e.target.closest('.btn-cancelar');
                        const id = btn.getAttribute('data-id');
                        idReservaACancelar.value = id;
                    }
                });
                
                // Event listener para cambio de fecha de reserva (obtener clima)
                document.getElementById('fecha-reserva')?.addEventListener('change', (e) => {
                    const fechaSeleccionada = e.target.value;
                    console.log('Fecha seleccionada para reserva:', fechaSeleccionada);
                    if (fechaSeleccionada) {
                        obtenerClima(fechaSeleccionada);
                    } else {
                        climaData.value = null;
                        climaCargando.value = false;
                        climaError.value = null;
                    }
                });
            };
            
            setupNavigation();
            console.log('Navegación configurada');
        });

        return {
            canchas,
            reservas,
            feedbacks,
            filtroDeporte,
            filtroFecha,
            canchasFiltradas,
            nombreReserva,
            canchaSeleccionadaNombre,
            canchaSeleccionadaId,
            fechaReserva,
            horaReserva,
            usuarioFeedback,
            canchaFeedback,
            comentarioFeedback,
            calificacionSeleccionada,
            climaData,
            climaCargando,
            climaError,
            prepararReserva,
            confirmarReserva,
            procesarReserva,
            cargarReservas,
            confirmarCancelacion,
            procesarCancelacion,
            cargarCanchasEnSelect,
            inicializarSistemaCalificacion,
            enviarFeedback,
            limpiarFormularioCompleto,
            obtenerClima
        };
    }
}).mount('#app');

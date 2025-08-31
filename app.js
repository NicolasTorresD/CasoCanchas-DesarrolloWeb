let canchas = [];
let reservas = [];
let idReservaACancelar = null;

// Función para obtener el nombre de cancha por ID
function obtenerNombreCanchaPorId(canchaId) {
    const cancha = canchas.find(c => c.id === canchaId);
    return cancha ? cancha.nombre : canchaId;
}

// Función para obtener el ID de cancha por nombre
function obtenerIdCanchaPorNombre(nombreCancha) {
    const cancha = canchas.find(c => c.nombre === nombreCancha);
    return cancha ? cancha.id : nombreCancha;
}

function showPage(pageId) {
    document.querySelectorAll('.container-page').forEach(page => {
        page.classList.remove('active');
    });
    document.getElementById(pageId).classList.add('active');
}

async function cargarCanchasDesdeJSON() {
    try {
        const response = await fetch('canchas.json');
        
        if (!response.ok) {
            throw new Error(`Error HTTP: ${response.status}`);
        }
        
        canchas = await response.json();
        renderizarCanchas(); 

    } catch (error) {
        console.error("Error al cargar el archivo JSON:", error);
        document.getElementById('canchas-listado').innerHTML = '<p class="text-center text-light mt-4">Error al cargar las canchas. Asegúrate de que el archivo `canchas.json` esté en la misma carpeta y de estar ejecutando un servidor local.</p>';
    }
}

async function cargarReservasDesdeJSON() {
    try {
        const response = await fetch('reservas.json');
        if (!response.ok) {
            throw new Error(`Error HTTP: ${response.status}`);
        }
        reservas = await response.json();
        console.log('Reservas cargadas:', reservas.length);
    } catch (error) {
        console.error("Error al cargar reservas:", error);
        // Inicializar con array vacío si hay error
        reservas = [];
    }
}

function renderizarCanchas(canchasFiltradas = canchas) {
    const listado = document.getElementById('canchas-listado');
    listado.innerHTML = '';
    if (canchasFiltradas.length === 0) {
        listado.innerHTML = '<p class="text-center text-light mt-4">No hay canchas disponibles con los filtros seleccionados.</p>';
        return;
    }
    canchasFiltradas.forEach(cancha => {
        const card = document.createElement('div');
        card.className = 'col-md-4 mb-4';
        card.setAttribute('data-deporte', cancha.deporte);
        card.innerHTML = `
            <div class="card h-100">
                <img src="${cancha.imagen}" class="card-img-top" alt="${cancha.nombre}">
                <div class="card-body">
                    <h5 class="card-title fw-bold">${cancha.nombre}</h5>
                    <p class="card-text text-muted">Deporte: ${cancha.deporte.charAt(0).toUpperCase() + cancha.deporte.slice(1)}</p>
                    <button class="btn w-100 btn-rounded reservar-btn" style="background-color: ${cancha.color}; border-color: ${cancha.color};" data-cancha-id="${cancha.id}" data-cancha-nombre="${cancha.nombre}">Reservar</button>
                </div>
            </div>
        `;
        listado.appendChild(card);
    });
    document.querySelectorAll('.reservar-btn').forEach(button => {
        button.addEventListener('click', function() {
            const canchaId = this.getAttribute('data-cancha-id');
            const canchaNombre = this.getAttribute('data-cancha-nombre');
            document.getElementById('cancha-reserva').value = canchaNombre;
            document.getElementById('cancha-reserva').setAttribute('data-cancha-id', canchaId);
            showPage('reserva-page');
        });
    });
}

document.getElementById('btnFiltrar').addEventListener('click', function() {
    const deporteSeleccionado = document.getElementById('deporte-filtro').value;
    const fechaSeleccionada = document.getElementById('fecha-filtro').value;
    
    let canchasFiltradas = canchas;

    if (deporteSeleccionado !== 'todos') {
        canchasFiltradas = canchasFiltradas.filter(cancha => cancha.deporte === deporteSeleccionado);
    }

    if (fechaSeleccionada) {
        // Filtrar canchas que ya tienen reservas en la fecha seleccionada
        canchasFiltradas = canchasFiltradas.filter(cancha => {
            const reservasEnFecha = reservas.filter(reserva => 
                reserva.canchaId === cancha.id && 
                reserva.fecha === fechaSeleccionada && 
                reserva.estado === 'Reservada'
            );
            return reservasEnFecha.length === 0;
        });
    }

    renderizarCanchas(canchasFiltradas);
});

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

document.getElementById('showListado').addEventListener('click', function() { showPage('listado-page'); });
document.getElementById('showListado2').addEventListener('click', function() { showPage('listado-page'); });
document.getElementById('showMisReservas').addEventListener('click', function() { showPage('mis-reservas-page'); cargarReservas(); });
document.getElementById('showMisReservas2').addEventListener('click', function() { showPage('mis-reservas-page'); cargarReservas(); });

document.getElementById('btnConfirmarReserva').addEventListener('click', function() {
    const nombre = document.getElementById('nombre-reserva').value;
    const canchaNombre = document.getElementById('cancha-reserva').value;
    const canchaId = document.getElementById('cancha-reserva').getAttribute('data-cancha-id');
    const fecha = document.getElementById('fecha-reserva').value;
    const hora = document.getElementById('hora-reserva').value;

    if (!nombre || !canchaNombre || !fecha || !hora) {
        alert('Por favor, completa todos los campos para la reserva.');
        return;
    }

    // Verificar si ya existe una reserva activa para esta cancha, fecha y hora
    const reservaExistente = reservas.find(reserva => 
        reserva.canchaId === canchaId && 
        reserva.fecha === fecha && 
        reserva.hora === hora && 
        reserva.estado === 'Reservada'
    );

    if (reservaExistente) {
        var errorModal = new bootstrap.Modal(document.getElementById('errorModal'));
        errorModal.show();
    } else {
        var confirmacionModal = new bootstrap.Modal(document.getElementById('confirmacionModal'));
        confirmacionModal.show();
    }
});

document.getElementById('btnProcesarReserva').addEventListener('click', function() {
    const nombre = document.getElementById('nombre-reserva').value;
    const canchaNombre = document.getElementById('cancha-reserva').value;
    const canchaId = document.getElementById('cancha-reserva').getAttribute('data-cancha-id');
    const fecha = document.getElementById('fecha-reserva').value;
    const hora = document.getElementById('hora-reserva').value;
    const canchaInfo = canchas.find(c => c.id === canchaId);
    const deporte = canchaInfo ? canchaInfo.deporte : 'desconocido';

    // Generar nuevo ID para la reserva
    const nuevoId = 'R' + String(reservas.length + 1).padStart(3, '0');
    const nuevaReserva = { 
        id: nuevoId, 
        usuario: nombre, 
        canchaId: canchaId, 
        fecha: fecha, 
        hora: hora, 
        estado: 'Reservada' 
    };
    reservas.push(nuevaReserva);

    // Limpiar formulario
    document.getElementById('nombre-reserva').value = '';
    document.getElementById('cancha-reserva').value = '';
    document.getElementById('fecha-reserva').value = '';
    document.getElementById('hora-reserva').value = '';

    var confirmacionModal = bootstrap.Modal.getInstance(document.getElementById('confirmacionModal'));
    confirmacionModal.hide();
    
    var reservaExitosaModal = new bootstrap.Modal(document.getElementById('reservaExitosaModal'));
    reservaExitosaModal.show();

    setTimeout(() => {
        var feedbackModal = new bootstrap.Modal(document.getElementById('feedbackModal'));
        feedbackModal.show();
    }, 1500);
});

function cargarReservas() {
    const listado = document.getElementById('reservas-listado');
    const noReservasMsg = document.getElementById('no-reservas-msg');
    listado.innerHTML = '';
    
    // Filtrar solo reservas activas
    const reservasActivas = reservas.filter(reserva => reserva.estado === 'Reservada');
    
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
                <p class="mb-0 text-muted">Fecha: ${reserva.fecha} | Hora: ${reserva.hora}</p>
                <small class="text-secondary">${reserva.usuario}</small>
            </div>
            <button class="btn btn-danger btn-rounded btn-cancelar" data-id="${reserva.id}" data-bs-toggle="modal" data-bs-target="#cancelacionModal"><i class="fas fa-trash-alt me-2"></i>Cancelar</button>
        `;
        listado.appendChild(item);
    });
}

document.getElementById('reservas-listado').addEventListener('click', function(e) {
    if (e.target.classList.contains('btn-cancelar')) {
        idReservaACancelar = e.target.getAttribute('data-id');
    }
});

document.getElementById('btnConfirmarCancelacion').addEventListener('click', function() {
    // Cambiar el estado de la reserva a 'Cancelada' en lugar de eliminarla
    const reserva = reservas.find(r => r.id === idReservaACancelar);
    if (reserva) {
        reserva.estado = 'Cancelada';
    }
    cargarReservas();
    var cancelacionModal = bootstrap.Modal.getInstance(document.getElementById('cancelacionModal'));
    cancelacionModal.hide();
    var cancelacionExitosaModal = new bootstrap.Modal(document.getElementById('cancelacionExitosaModal'));
    cancelacionExitosaModal.show();
});

document.addEventListener('DOMContentLoaded', () => {
    // Configurar fecha mínima como hoy
    const today = new Date().toISOString().split('T')[0];
    const fechaFiltro = document.getElementById('fecha-filtro');
    const fechaReserva = document.getElementById('fecha-reserva');
    
    if (fechaFiltro) fechaFiltro.min = today;
    if (fechaReserva) fechaReserva.min = today;
    
    // Cargar datos y inicializar la aplicación
    Promise.all([
        cargarCanchasDesdeJSON(),
        cargarReservasDesdeJSON()
    ]).then(() => {
        console.log('Datos cargados correctamente');
        console.log('Canchas:', canchas.length);
        console.log('Reservas:', reservas.length);
    }).catch(error => {
        console.error('Error al cargar los datos:', error);
    });
    
    generateTimeOptions();
    
    // Valores por defecto para testing (opcional)
    const usernameField = document.getElementById('username');
    const passwordField = document.getElementById('password');
    if (usernameField) usernameField.value = 'user';
    if (passwordField) passwordField.value = 'password';
});
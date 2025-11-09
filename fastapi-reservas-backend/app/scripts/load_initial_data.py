"""
Script para cargar datos iniciales desde los archivos JSON
Ejecutar con: python -m app.scripts.load_initial_data
"""
import json
import sys
from pathlib import Path
from datetime import datetime

# Agregar el directorio raíz al path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from app.database import SessionLocal, engine
from app.models import Base, Usuario, Deporte, Cancha, Reserva, Feedback
import bcrypt

def hash_password(password: str) -> str:
    """Hash password usando bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def load_deportes(db):
    """Cargar deportes iniciales"""
    deportes_data = [
        {"nombre": "futbol", "descripcion": "Fútbol 5 y 7", "activo": True},
        {"nombre": "tenis", "descripcion": "Tenis individual y dobles", "activo": True},
        {"nombre": "padel", "descripcion": "Pádel", "activo": True},
    ]
    
    for data in deportes_data:
        # Verificar si ya existe
        existing = db.query(Deporte).filter(Deporte.nombre == data["nombre"]).first()
        if not existing:
            deporte = Deporte(**data)
            db.add(deporte)
            print(f"✅ Deporte agregado: {data['nombre']}")
        else:
            print(f"⏭️  Deporte ya existe: {data['nombre']}")
    
    db.commit()

def load_canchas(db):
    """Cargar canchas desde canchas.json"""
    json_path = Path(__file__).resolve().parents[3] / "canchas.json"
    
    if not json_path.exists():
        print(f"❌ Archivo no encontrado: {json_path}")
        return
    
    with open(json_path, 'r', encoding='utf-8') as f:
        canchas_data = json.load(f)
    
    # Mapear deportes (solo futbol, tenis y padel)
    deporte_map = {
        "futbol": db.query(Deporte).filter(Deporte.nombre == "futbol").first(),
        "tenis": db.query(Deporte).filter(Deporte.nombre == "tenis").first(),
        "padel": db.query(Deporte).filter(Deporte.nombre == "padel").first(),
    }
    
    for data in canchas_data:
        # Verificar si ya existe
        existing = db.query(Cancha).filter(Cancha.codigo == data["id"]).first()
        if not existing:
            deporte = deporte_map.get(data["deporte"])
            if deporte:
                cancha = Cancha(
                    id_deporte=deporte.id_deporte,
                    nombre=data["nombre"],
                    codigo=data["id"],
                    imagen_url=data.get("imagen"),
                    color=data.get("color", "#000000"),
                    precio_hora=data.get("precio", 0),
                    estado="Disponible"
                )
                db.add(cancha)
                print(f"✅ Cancha agregada: {data['id']} - {data['nombre']}")
            else:
                print(f"⚠️  Deporte no encontrado para cancha: {data['id']}")
        else:
            print(f"⏭️  Cancha ya existe: {data['id']}")
    
    db.commit()

def load_usuarios(db):
    """Cargar usuarios de ejemplo"""
    usuarios_data = [
        {"nombre": "Carlos Díaz", "email": "carlos.diaz@example.com", "telefono": "555-0001"},
        {"nombre": "María López", "email": "maria.lopez@example.com", "telefono": "555-0002"},
        {"nombre": "José Pérez", "email": "jose.perez@example.com", "telefono": "555-0003"},
        {"nombre": "Ana Fernández", "email": "ana.fernandez@example.com", "telefono": "555-0004"},
        {"nombre": "Luis González", "email": "luis.gonzalez@example.com", "telefono": "555-0005"},
    ]
    
    for data in usuarios_data:
        # Verificar si ya existe
        existing = db.query(Usuario).filter(Usuario.email == data["email"]).first()
        if not existing:
            # Password por defecto: "password123"
            usuario = Usuario(
                nombre=data["nombre"],
                email=data["email"],
                telefono=data.get("telefono"),
                password_hash=hash_password("password123"),
                activo=True
            )
            db.add(usuario)
            print(f"✅ Usuario agregado: {data['email']}")
        else:
            print(f"⏭️  Usuario ya existe: {data['email']}")
    
    db.commit()

def load_reservas(db):
    """Cargar reservas desde reservas.json"""
    json_path = Path(__file__).resolve().parents[3] / "reservas.json"
    
    if not json_path.exists():
        print(f"❌ Archivo no encontrado: {json_path}")
        return
    
    with open(json_path, 'r', encoding='utf-8') as f:
        reservas_data = json.load(f)
    
    for data in reservas_data:
        # Verificar si ya existe (por ID original)
        # Como no tenemos el campo 'codigo' en Reserva, verificamos por cancha+fecha+hora
        cancha = db.query(Cancha).filter(Cancha.codigo == data["canchaId"]).first()
        if not cancha:
            print(f"⚠️  Cancha no encontrada: {data['canchaId']}")
            continue
        
        # Buscar usuario por nombre
        usuario = db.query(Usuario).filter(Usuario.nombre == data["usuario"]).first()
        if not usuario:
            print(f"⚠️  Usuario no encontrado: {data['usuario']}")
            continue
        
        # Parsear fecha y hora
        fecha = datetime.strptime(data["fecha"], "%Y-%m-%d").date()
        hora = datetime.strptime(data["hora"], "%H:%M").time()
        
        # Verificar si ya existe una reserva igual
        existing = db.query(Reserva).filter(
            Reserva.id_cancha == cancha.id_cancha,
            Reserva.id_usuario == usuario.id_usuario,
            Reserva.fecha == fecha,
            Reserva.hora == hora
        ).first()
        
        if not existing:
            reserva = Reserva(
                id_usuario=usuario.id_usuario,
                id_cancha=cancha.id_cancha,
                fecha=fecha,
                hora=hora,
                duracion=60,  # Duración por defecto 60 minutos
                estado=data["estado"],
                precio_total=cancha.precio_hora
            )
            db.add(reserva)
            print(f"✅ Reserva agregada: {data['id']} - {data['usuario']} en {data['canchaId']}")
        else:
            print(f"⏭️  Reserva ya existe: {data['id']}")
    
    db.commit()

def load_feedbacks(db):
    """Cargar feedbacks desde feedbacks.json"""
    json_path = Path(__file__).resolve().parents[3] / "feedbacks.json"
    
    if not json_path.exists():
        print(f"❌ Archivo no encontrado: {json_path}")
        return
    
    with open(json_path, 'r', encoding='utf-8') as f:
        feedbacks_data = json.load(f)
    
    for data in feedbacks_data:
        # Buscar usuario por nombre
        usuario = db.query(Usuario).filter(Usuario.nombre == data["usuario"]).first()
        if not usuario:
            print(f"⚠️  Usuario no encontrado para feedback: {data['usuario']}")
            continue
        
        # Buscar cancha
        cancha = db.query(Cancha).filter(Cancha.codigo == data["canchaId"]).first()
        if not cancha:
            print(f"⚠️  Cancha no encontrada para feedback: {data['canchaId']}")
            continue
        
        # Buscar reserva correspondiente
        fecha = datetime.strptime(data["fecha"], "%Y-%m-%d").date()
        reserva = db.query(Reserva).filter(
            Reserva.id_usuario == usuario.id_usuario,
            Reserva.id_cancha == cancha.id_cancha,
            Reserva.fecha == fecha
        ).first()
        
        if not reserva:
            print(f"⚠️  Reserva no encontrada para feedback: {data['id']}")
            continue
        
        # Verificar si ya existe el feedback
        existing = db.query(Feedback).filter(Feedback.id_reserva == reserva.id_reserva).first()
        
        if not existing:
            feedback = Feedback(
                id_reserva=reserva.id_reserva,
                id_usuario=usuario.id_usuario,
                id_cancha=cancha.id_cancha,
                calificacion=data["calificacion"],
                comentario=data.get("comentario"),
                fecha=datetime.strptime(data["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
            )
            db.add(feedback)
            print(f"✅ Feedback agregado: {data['id']} - {data['usuario']}")
        else:
            print(f"⏭️  Feedback ya existe para reserva: {reserva.id_reserva}")
    
    db.commit()

def main():
    """Función principal"""
    print("🚀 Iniciando carga de datos iniciales...\n")
    
    # Crear sesión
    db = SessionLocal()
    
    try:
        # Cargar datos en orden (respetando foreign keys)
        print("📊 Cargando deportes...")
        load_deportes(db)
        
        print("\n🏟️  Cargando canchas...")
        load_canchas(db)
        
        print("\n👥 Cargando usuarios...")
        load_usuarios(db)
        
        print("\n📅 Cargando reservas...")
        load_reservas(db)
        
        print("\n💬 Cargando feedbacks...")
        load_feedbacks(db)
        
        print("\n✅ ¡Datos iniciales cargados exitosamente!")
        print("\n📝 Nota: Todos los usuarios tienen password: 'password123'")
        
    except Exception as e:
        print(f"\n❌ Error al cargar datos: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    main()

"""
Script para inspeccionar el contenido de la base de datos
Ejecutar: python -m app.scripts.inspect_db
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from app.database import SessionLocal
from app.models.deporte import Deporte
from app.models.cancha import Cancha
from app.models.usuario import Usuario
from app.models.reserva import Reserva
from app.models.feedback import Feedback
from tabulate import tabulate

def show_deportes(db):
    """Mostrar tabla de deportes"""
    print("\n" + "="*80)
    print("⚽ TABLA: DEPORTES")
    print("="*80)
    
    deportes = db.query(Deporte).all()
    if deportes:
        data = [[d.id_deporte, d.nombre, d.descripcion, d.activo] 
                for d in deportes]
        headers = ["ID", "Nombre", "Descripción", "Activo"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
        print(f"\nTotal: {len(deportes)} deportes")
    else:
        print("❌ No hay deportes en la base de datos")

def show_canchas(db):
    """Mostrar tabla de canchas"""
    print("\n" + "="*80)
    print("🏟️  TABLA: CANCHAS")
    print("="*80)
    
    canchas = db.query(Cancha).all()
    if canchas:
        data = [[c.id_cancha, c.codigo, c.nombre, c.deporte.nombre, 
                 f"${c.precio_hora}", c.estado] 
                for c in canchas]
        headers = ["ID", "Código", "Nombre", "Deporte", "Precio/Hora", "Estado"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
        print(f"\nTotal: {len(canchas)} canchas")
    else:
        print("❌ No hay canchas en la base de datos")

def show_usuarios(db):
    """Mostrar tabla de usuarios"""
    print("\n" + "="*80)
    print("👥 TABLA: USUARIOS")
    print("="*80)
    
    usuarios = db.query(Usuario).all()
    if usuarios:
        data = [[u.id_usuario, u.nombre, u.email, u.telefono, u.activo] 
                for u in usuarios]
        headers = ["ID", "Nombre", "Email", "Teléfono", "Activo"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
        print(f"\nTotal: {len(usuarios)} usuarios")
    else:
        print("❌ No hay usuarios en la base de datos")

def show_reservas(db):
    """Mostrar tabla de reservas"""
    print("\n" + "="*80)
    print("📅 TABLA: RESERVAS")
    print("="*80)
    
    reservas = db.query(Reserva).all()
    if reservas:
        data = [[r.id_reserva, r.usuario.nombre, r.cancha.codigo, 
                 r.fecha, r.hora, f"{r.duracion} min", 
                 f"${r.precio_total}", r.estado] 
                for r in reservas]
        headers = ["ID", "Usuario", "Cancha", "Fecha", "Hora", "Duración", "Precio", "Estado"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
        print(f"\nTotal: {len(reservas)} reservas")
    else:
        print("❌ No hay reservas en la base de datos")

def show_feedbacks(db):
    """Mostrar tabla de feedbacks"""
    print("\n" + "="*80)
    print("💬 TABLA: FEEDBACKS")
    print("="*80)
    
    feedbacks = db.query(Feedback).all()
    if feedbacks:
        data = [[f.id_feedback, f.usuario.nombre, f.cancha.codigo, 
                 f"⭐"*f.calificacion, 
                 f.comentario[:40] + "..." if f.comentario and len(f.comentario) > 40 else f.comentario,
                 f.fecha.strftime("%Y-%m-%d")] 
                for f in feedbacks]
        headers = ["ID", "Usuario", "Cancha", "Calificación", "Comentario", "Fecha"]
        print(tabulate(data, headers=headers, tablefmt="grid"))
        print(f"\nTotal: {len(feedbacks)} feedbacks")
    else:
        print("❌ No hay feedbacks en la base de datos")

def show_statistics(db):
    """Mostrar estadísticas generales"""
    print("\n" + "="*80)
    print("📊 ESTADÍSTICAS GENERALES")
    print("="*80)
    
    stats = [
        ["Deportes", db.query(Deporte).count()],
        ["Canchas", db.query(Cancha).count()],
        ["Usuarios", db.query(Usuario).count()],
        ["Reservas", db.query(Reserva).count()],
        ["Feedbacks", db.query(Feedback).count()],
    ]
    
    print(tabulate(stats, headers=["Tabla", "Total Registros"], tablefmt="grid"))
    
    # Estadísticas por deporte
    print("\n📈 Canchas por deporte:")
    for deporte in db.query(Deporte).all():
        count = db.query(Cancha).filter(Cancha.id_deporte == deporte.id_deporte).count()
        print(f"   • {deporte.nombre.capitalize()}: {count} canchas")
    
    # Reservas por estado
    print("\n📋 Reservas por estado:")
    estados = db.query(Reserva.estado).distinct().all()
    for (estado,) in estados:
        count = db.query(Reserva).filter(Reserva.estado == estado).count()
        print(f"   • {estado}: {count} reservas")

def main():
    """Función principal"""
    print("🔍 INSPECCIÓN DE BASE DE DATOS")
    
    db = SessionLocal()
    
    try:
        # Mostrar todas las tablas
        show_statistics(db)
        show_deportes(db)
        show_canchas(db)
        show_usuarios(db)
        show_reservas(db)
        show_feedbacks(db)
        
        print("\n" + "="*80)
        print("✅ Inspección completada")
        print("="*80)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    main()

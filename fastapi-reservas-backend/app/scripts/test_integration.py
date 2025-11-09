"""
Script para probar la integración de la base de datos con la API
Ejecutar: python -m app.scripts.test_integration
"""
import sys
from pathlib import Path

# Add the parent directory to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from app.database import SessionLocal, engine, Base
from app.models.deporte import Deporte
from app.models.cancha import Cancha
from app.models.usuario import Usuario
from app.models.reserva import Reserva
from app.models.feedback import Feedback

def test_database_connection():
    """Verifica la conexión a la base de datos"""
    print("🔌 Probando conexión a la base de datos...")
    try:
        db = SessionLocal()
        # Probar una consulta simple
        deportes = db.query(Deporte).all()
        print(f"✅ Conexión exitosa. {len(deportes)} deportes encontrados.")
        db.close()
        return True
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False

def test_deportes():
    """Verifica que los deportes se cargaron correctamente"""
    print("\n⚽ Verificando deportes...")
    db = SessionLocal()
    try:
        deportes = db.query(Deporte).all()
        print(f"   Total deportes: {len(deportes)}")
        for deporte in deportes:
            print(f"   - {deporte.nombre} (ID: {deporte.id_deporte})")
        db.close()
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        db.close()
        return False

def test_canchas():
    """Verifica que las canchas se cargaron correctamente"""
    print("\n🏟️  Verificando canchas...")
    db = SessionLocal()
    try:
        canchas = db.query(Cancha).all()
        print(f"   Total canchas: {len(canchas)}")
        
        # Contar por deporte
        for deporte in db.query(Deporte).all():
            count = db.query(Cancha).filter(Cancha.id_deporte == deporte.id_deporte).count()
            print(f"   - {deporte.nombre}: {count} canchas")
        
        db.close()
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        db.close()
        return False

def test_usuarios():
    """Verifica que los usuarios se cargaron correctamente"""
    print("\n👥 Verificando usuarios...")
    db = SessionLocal()
    try:
        usuarios = db.query(Usuario).all()
        print(f"   Total usuarios: {len(usuarios)}")
        for usuario in usuarios[:3]:  # Mostrar solo los primeros 3
            print(f"   - {usuario.nombre} ({usuario.email})")
        db.close()
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        db.close()
        return False

def test_relationships():
    """Verifica las relaciones entre modelos"""
    print("\n🔗 Verificando relaciones...")
    db = SessionLocal()
    try:
        # Probar relación cancha -> deporte
        cancha = db.query(Cancha).first()
        if cancha:
            print(f"   Cancha '{cancha.nombre}' -> Deporte '{cancha.deporte.nombre}'")
        
        # Verificar si hay reservas
        reservas_count = db.query(Reserva).count()
        print(f"   Total reservas: {reservas_count}")
        
        # Verificar si hay feedbacks
        feedbacks_count = db.query(Feedback).count()
        print(f"   Total feedbacks: {feedbacks_count}")
        
        db.close()
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        db.close()
        return False

def main():
    """Ejecuta todas las pruebas"""
    print("=" * 60)
    print("🧪 PRUEBAS DE INTEGRACIÓN DE BASE DE DATOS")
    print("=" * 60)
    
    tests = [
        test_database_connection,
        test_deportes,
        test_canchas,
        test_usuarios,
        test_relationships
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 60)
    print(f"📊 RESUMEN: {sum(results)}/{len(results)} pruebas exitosas")
    print("=" * 60)
    
    if all(results):
        print("✅ Todas las pruebas pasaron correctamente!")
        print("\n🚀 La base de datos está lista para ser integrada con la API.")
        print("   Puedes iniciar el servidor con: uvicorn app.main:app --reload")
    else:
        print("⚠️  Algunas pruebas fallaron. Revisa los errores arriba.")

if __name__ == "__main__":
    main()

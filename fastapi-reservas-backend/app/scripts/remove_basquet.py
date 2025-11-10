"""
Script para eliminar el deporte 'basquet' de la base de datos
Ejecutar: python -m app.scripts.remove_basquet
"""
import sys
from pathlib import Path

# Add the parent directory to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from app.database import SessionLocal
from app.models.deporte import Deporte

def remove_basquet():
    """Elimina el deporte basquet de la base de datos"""
    db = SessionLocal()
    
    try:
        # Buscar el deporte basquet
        basquet = db.query(Deporte).filter(Deporte.nombre == "basquet").first()
        
        if basquet:
            print(f"🗑️  Eliminando deporte: {basquet.nombre} (ID: {basquet.id_deporte})")
            db.delete(basquet)
            db.commit()
            print("✅ Deporte 'basquet' eliminado correctamente")
        else:
            print("ℹ️  El deporte 'basquet' no existe en la base de datos")
        
        # Verificar deportes restantes
        print("\n📋 Deportes disponibles después de la eliminación:")
        deportes = db.query(Deporte).all()
        for deporte in deportes:
            print(f"   - {deporte.nombre} (ID: {deporte.id_deporte})")
        
        db.close()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()
        db.close()

if __name__ == "__main__":
    print("=" * 60)
    print("🧹 ELIMINANDO DEPORTE 'BASQUET'")
    print("=" * 60)
    remove_basquet()
    print("=" * 60)

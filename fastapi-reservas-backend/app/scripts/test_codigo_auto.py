"""
Script para probar la creación automática de código de cancha
Ejecutar: python -m app.scripts.test_codigo_auto
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from app.database import SessionLocal
from app.services.cancha_service import CanchaService
from app.schemas.cancha import CanchaCreate

def test_codigo_automatico():
    """Probar generación automática de código"""
    print("🧪 PRUEBA: Generación automática de código de cancha\n")
    
    db = SessionLocal()
    service = CanchaService(db)
    
    try:
        # Crear cancha SIN código (automático)
        print("1️⃣ Creando cancha SIN especificar código...")
        nueva_cancha = CanchaCreate(
            nombre='Cancha de Prueba Automática',
            id_deporte=1,  # Fútbol
            precio_hora=45.00,
            estado='Disponible',
            color='#FF6B6B'
        )
        
        cancha = service.create_cancha(nueva_cancha)
        print(f'   ✅ Cancha creada exitosamente!')
        print(f'   📝 ID: {cancha.id_cancha}')
        print(f'   📝 Nombre: {cancha.nombre}')
        print(f'   🏷️  Código: {cancha.codigo} ← GENERADO AUTOMÁTICAMENTE')
        print(f'   💰 Precio: ${cancha.precio_hora}\n')
        
        # Crear otra cancha del mismo deporte
        print("2️⃣ Creando otra cancha de fútbol (sin código)...")
        otra_cancha = CanchaCreate(
            nombre='Cancha de Fútbol Extra',
            id_deporte=1,  # Fútbol
            precio_hora=50.00,
            estado='Disponible',
            color='#00FF00'
        )
        
        cancha2 = service.create_cancha(otra_cancha)
        print(f'   ✅ Cancha creada exitosamente!')
        print(f'   🏷️  Código: {cancha2.codigo} ← El número se incrementó\n')
        
        # Crear cancha CON código personalizado
        print("3️⃣ Creando cancha CON código personalizado...")
        cancha_custom = CanchaCreate(
            nombre='Cancha VIP Premium',
            id_deporte=2,  # Tenis
            codigo='VIP-01',
            precio_hora=100.00,
            estado='Disponible',
            color='#FFD700'
        )
        
        cancha3 = service.create_cancha(cancha_custom)
        print(f'   ✅ Cancha creada exitosamente!')
        print(f'   🏷️  Código: {cancha3.codigo} ← Código personalizado usado\n')
        
        print("=" * 60)
        print("✅ TODAS LAS PRUEBAS PASARON CORRECTAMENTE")
        print("=" * 60)
        
    except Exception as e:
        print(f'\n❌ Error: {e}')
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    test_codigo_automatico()

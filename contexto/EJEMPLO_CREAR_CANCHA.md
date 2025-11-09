# 📝 Ejemplo: Crear Nueva Cancha

## ✅ **MEJORA IMPLEMENTADA: Código Automático**

Ahora el campo `codigo` se genera **automáticamente** si no lo proporcionas.

---

## 🎯 **Opciones para crear una cancha:**

### **Opción 1: Código Automático (RECOMENDADO)**

```json
POST /api/v1/canchas/
{
  "nombre": "Cancha de Fútbol 6",
  "id_deporte": 1,
  "precio_hora": 40.00,
  "color": "#00FF00",
  "estado": "Disponible"
}
```

**Resultado:** Código generado automáticamente → `CAN-16`

---

### **Opción 2: Código Manual**

```json
POST /api/v1/canchas/
{
  "nombre": "Cancha VIP Premium",
  "id_deporte": 1,
  "codigo": "VIP-01",
  "precio_hora": 100.00,
  "color": "#FFD700",
  "estado": "Disponible"
}
```

**Resultado:** Usa el código que proporcionaste → `VIP-01`

---

## 🏷️ **Formato de Códigos Automáticos:**

Mantiene el estándar actual: **CAN-01**, **CAN-02**, **CAN-03**, etc.

| Última Cancha | Siguiente Código |
|---------------|------------------|
| CAN-15        | **CAN-16**       |
| CAN-16        | **CAN-17**       |
| CAN-17        | **CAN-18**       |

**Nota:** El número se incrementa automáticamente según el total de canchas existentes.

---

## 🧪 **Probar con Swagger:**

1. Abre: http://127.0.0.1:8000/docs
2. Ve a **POST /api/v1/canchas/**
3. Click en "Try it out"
4. Usa este JSON (sin campo `codigo`):

```json
{
  "nombre": "Cancha de Prueba",
  "id_deporte": 1,
  "precio_hora": 35.00,
  "estado": "Disponible",
  "color": "#FF5733"
}
```

5. Click en "Execute"
6. Verás que se generó automáticamente: `FUT-06`

---

## 🧪 **Probar con curl:**

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/canchas/" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Cancha Nueva",
    "id_deporte": 2,
    "precio_hora": 25.00,
    "estado": "Disponible",
    "color": "#0066CC"
  }'
```

---

## 📊 **IDs de Deportes actuales:**

| ID | Deporte | Prefijo Código |
|----|---------|----------------|
| 1  | futbol  | FUT-           |
| 2  | tenis   | TEN-           |
| 5  | padel   | PAD-           |

---

## ✨ **Ventajas del código automático:**

✅ No tienes que pensar en el código  
✅ Se evitan códigos duplicados  
✅ Formato consistente (FUT-01, FUT-02, etc.)  
✅ Aún puedes usar códigos personalizados si quieres  
✅ El sistema verifica que no exista duplicado  

---

## 🔍 **Ver todas las canchas y sus códigos:**

```bash
python -m app.scripts.inspect_db
```

O visita: http://127.0.0.1:8000/api/v1/canchas/

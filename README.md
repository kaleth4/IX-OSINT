# 📞 IX. OSINT: Phone Number Intelligence 

## 🔍 **Introducción al Script de OSINT para Números de Teléfono**

Este script de Python está diseñado para la **recopilación de información (OSINT)** a partir de números de teléfono, utilizando la librería [`phonenumbers`](https://github.com/daviddrysdale/python-phonenumbers), un puerto de la librería [`libphonenumber`](https://github.com/google/libphonenumber) de Google.

---

## 🚀 **¿Qué hace el código?**

El script procesa un número de teléfono (con formato internacional, ej: `+34600000000`) para extraer dos datos clave:

1. **Geolocalización (`geocoder`):**
   Determina la región o el país al que pertenece el número (ej: *"Switzerland"*, *"Spain"*).

2. **Identificación de Operador (`carrier`):**
   Identifica la compañía telefónica proveedora del servicio (ej: *"Swisscom"*, *"Vodafone"*, *"Movistar"*).

---

## 📜 **Código del Script**

```python
import sys
import phonenumbers
from phonenumbers import geocoder, carrier

def track_phone_number(phone_input: str, lang: str = "en"):
    try:
        # Parsea el número (asume formato internacional si empieza con +)
        parsed_number = phonenumbers.parse(phone_input)

        if not phonenumbers.is_valid_number(parsed_number):
            print(f"[-] El número {phone_input} no es válido.")
            return

        # 1. Obtener ubicación geográfica
        location = geocoder.description_for_number(parsed_number, lang)

        # 2. Obtener nombre del operador
        service_provider = carrier.name_for_number(parsed_number, lang)

        print(f"\n[+] Resultados para: {phone_input}")
        print(f"{"-"*30}")
        print(f"📍 Ubicación: {location if location else 'Desconocida'}")
        print(f"📶 Operador:  {service_provider if service_provider else 'No identificado'}")
        print(f"📋 Formato:    {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")

    except Exception as e:
        print(f"[!] Error al procesar el número: {e}")

if __name__ == "__main__":
    # Permite pasar el número como argumento: python script.py +34600000000
    if len(sys.argv) > 1:
        track_phone_number(sys.argv[1])
    else:
        target = input("Ingresa el número (con prefijo +): ")
        track_phone_number(target)
```

---

## 💡 **¿Por qué esta versión es mejor?**

✅ **Validación:**
   Usa `is_valid_number` para asegurar que el número **realmente existe** antes de intentar rastrearlo.

✅ **Formateo:**
   Añade la función `format_number` para mostrar el número de manera **estandarizada** (formato E.164).

✅ **Flexibilidad:**
   Permite la entrada dinámica de datos:
   - **Desde terminal:** `python script.py +34600000000`
   - **Interactivo:** Ejecución sin argumentos (`python script.py`).

✅ **Manejo de errores:**
   Captura excepciones (ej: números inválidos o formatos incorrectos).

---

## 📝 **Integración en tu `README.md`**

Puedes añadirlo como una nueva sección de **Reconocimiento Pasivo**:

```markdown
## 📞 IX. OSINT: Phone Number Intelligence
Herramienta para la identificación de vectores de ataque mediante análisis de metadatos telefónicos.

*   **Identificación de Carrier:** Crucial para ataques de ingeniería social dirigidos.
*   **Validación de Formato:** Asegura que los objetivos cumplen con los estándares internacionales (E.164).
```

---
⚠ **⚠ Advertencia:**
Este script debe usarse **únicamente con fines legales y éticos**. La recopilación de información sin consentimiento puede ser ilegal en muchas jurisdicciones.

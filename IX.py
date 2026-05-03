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

import phonenumbers
from phonenumbers import carrier, geocoder, timezone
phone_number = "+56999401140"
parsed_number = phonenumbers.parse(phone_number, "CL")
is_valid = phonenumbers.is_valid_number(parsed_number)
number_type = phonenumbers.number_type(parsed_number)
region_info = geocoder.description_for_number(parsed_number, "en")
carrier_info = carrier.name_for_number(parsed_number, "en")
timezone_info = timezone.time_zones_for_number(parsed_number)


print(f"Número válido: {is_valid}")
print(f"Tipo de número: {number_type}")
print(f"Región: {region_info}")
print(f"Proveedor: {carrier_info}")
print(f"Zona horaria: {timezone_info}")
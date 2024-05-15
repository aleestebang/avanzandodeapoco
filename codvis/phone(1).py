import phonenumbers

# Ejemplo de número de teléfono
numero_telefono = "+56999401140"

# Parsear el número de teléfono
numero_parseado = phonenumbers.parse(numero_telefono, None)

# Validar si el número de teléfono es válido
if phonenumbers.is_valid_number(numero_parseado):
    print("Número de teléfono válido")
else:
    print("Número de teléfono inválido")

# Obtener información del número de teléfono
region = phonenumbers.region_code_for_number(numero_parseado)
tipo_numero = phonenumbers.number_type(numero_parseado)
formato_internacional = phonenumbers.format_number(numero_parseado, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
formato_nacional = phonenumbers.format_number(numero_parseado, phonenumbers.PhoneNumberFormat.NATIONAL)

print("Región:", region)
print("Tipo de número:", tipo_numero)
print("Formato internacional:", formato_internacional)
print("Formato nacional:", formato_nacional)

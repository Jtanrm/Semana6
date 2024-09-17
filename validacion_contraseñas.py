# Función para validar la contraseña
def validar_contraseña(contraseña):
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_caracter_especial = False
    caracteres_especiales = "!@#$%^&*"

    # Verificar longitud mínima
    if len(contraseña) < 8:
        return False

    # Iterar sobre cada caracter en la contraseña
    for caracter in contraseña:
        # Verificar si hay mayúsculas
        if caracter.isupper():
            tiene_mayuscula = True
        # Verificar si hay minúsculas
        elif caracter.islower():
            tiene_minuscula = True
        # Verificar si hay números
        elif caracter.isdigit():
            tiene_numero = True
        # Verificar si hay caracteres especiales
        elif caracter in caracteres_especiales:
            tiene_caracter_especial = True

    # Retornar True si cumple todos los criterios
    if tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_caracter_especial:
        return True
    else:
        return False

# Solicitar contraseña al usuario
contraseña = input("Introduce tu contraseña: ")

# Llamar a la función de validación
es_valida = validar_contraseña(contraseña)

# Mostrar resultado
if es_valida:
    print("La contraseña es válida.")
else:
    print("La contraseña no cumple con los requisitos.")

# Comprobación del código:
# Puedes probarlo ingresando contraseñas como 'Abc123!' para asegurar que funcione correctamente.

# Formateador de nombres

# primer_nombre = input("First Name: ")
# segundo_nombre = input("Second Name: ")
# primer_apellido = input("Last Name: ")
# segundo_apellido = input("Last Name2: ")

# primer_nombre = primer_nombre.capitalize()
# segundo_nombre = segundo_nombre.capitalize()
# primer_apellido = primer_apellido.capitalize()
# segundo_apellido = segundo_apellido.capitalize()

# nombre_completo = f"{primer_nombre} {segundo_nombre} {primer_apellido} {segundo_apellido}"

# print(nombre_completo)

##############################################################
# pro code

primer_nombre = input("¿Cual es tu primer nombre? ").strip().capitalize()
segundo_nombre = input("¿Cual es tu segundo nombre? ").strip().capitalize()
primer_apellido = input("¿Cual es tu primer apellido? ").strip().capitalize()
segundo_apellido = input("¿Cual es tu segundo nombre? ").strip().capitalize()

NOMBRE_COMPLETO = f"{primer_nombre} {segundo_nombre} {primer_apellido} {segundo_apellido}".replace(
    "  ", " ")

print(NOMBRE_COMPLETO)

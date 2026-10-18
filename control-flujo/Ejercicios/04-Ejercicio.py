# Formateador de Nombres

# Este programa solicita al usuario, su nombre completo y lo formatea eliminado espacios adicionales y capitalizando las palabras
# Se asegura de que el usuario ingrese un nombre y un apellido valido antes de proceder

print("Ingresa tu nombre, para salir del programa ingresa salir y preciona enter")

# nombre = input("Ingresa tu primer nombre: ").strip().capitalize()
nombre = ""
# if nombre == "Exit":
#     print("Has salido de la aplicacion...")
#     exit()

while not nombre:
    print("No ingresaste tu primer nombre. Puedes salir de la aplicacion escribiendo Exit")
    nombre = input("¿Cual es tu nombre: ").strip().capitalize()
    if nombre == "Exit":
        print("Has salido de la aplicacion")
        exit()

segundo_nombre = input(
    "¿Cual es tu segundo nombre?(Opcional): ").strip().capitalize()

if segundo_nombre == "Exit":
    exit()

primer_apellido = input("¿Cual es tu primer apellido: ").strip().capitalize()

while not primer_apellido:
    print("No ingresaste tu primer apellido. Puedes salir de la aplicacion escribiendo Exit")
    primer_apellido = input(
        "¿Cual es tu primer apellido?: ").strip().capitalize()

    if primer_apellido == "Exit":
        print("Has salido de la aplicacion")
        exit()

segundo_apellido = input(
    "¿Cual es tu segundo apellido?(Opcional): ").strip().capitalize()

if segundo_nombre == "Exit":
    exit()

# Ahora debemos concatenar el nombre y apellido ingresado.

nombre_completo = nombre

if segundo_nombre:
    nombre_completo += f" {segundo_nombre}"

nombre_completo += f" {primer_apellido}"

if segundo_apellido:
    nombre_completo += f" {segundo_apellido}"

print(f"El nombre completo es: {nombre_completo}")

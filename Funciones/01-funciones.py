# def hola(nombre):  # Parametros
#     print("Hola Mundo")
#     print(f"Bienvenido {nombre}")


# hola(input("Ingresa tu nombre: "))  # Argumentos...

# Podemos asignar valores por defecto, si es que le pasamos un valor como abajo al segundo
def hola(nombre, apellido="Valor x defecto"):
    # parametro este tomara el que tu le pases como argumento. que serian parametros opcionales.
    print("Hola Mundo")
    print(f"Bienvenido {nombre} {apellido}")


# hola(input("Ingresa tu nombre: "), "Del VALLE")  # Argumentos...
# Tambien podemos poner los valores al reves y ordenandolos con argumentos nombrados. ejemplo

# Ejemplo aca estan al reves, podriamos ismplmente cambiar los string o nombrarlos. ejemplo
# hola("Del Valle", "Francisco") # out: Del Valle Francisco

# out: Bienvenido Francisco, Del Valle
hola(apellido="Del Valle", nombre="Francisco")

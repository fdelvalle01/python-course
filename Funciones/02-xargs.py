# def suma(a, b):
#     print(a + b)

# suma(2, 5)


def suma(*numeros):  # Xargs => el * al inicio le dice que sera iterable. tomara todos los argumentos que le pasemos en la llamada de la funcion
    resultado = 0
    for numero in numeros:
        resultado += numero
       # print(resultado)
    # El print debe estar identado, porque si no imprimira muchas veces dentro del for.
    print(resultado)


suma(2, 5)
suma(2, 5, 7)
suma(2, 5, 7, 45, 32)

buscar = 5

for numero in range(5): # Esto es iterable.
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break
else: #este seria un for else si no se encuentra algo dentro del
    # primer for y no lo encuentra entonces imprimimos un mensaje
    print("No se encontro el numero buscado :(")

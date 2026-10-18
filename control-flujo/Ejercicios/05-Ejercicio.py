
# Caja registradora que acumula el precio de los productos ingresados por el usuario.

# Variables

total = 0.0

while True:
    precio = input("Ingresa los precios: ")
    if precio.lower() == "fin":
        break
    total += int(precio)

print(f"El total a pagar es: {total:.2f}")

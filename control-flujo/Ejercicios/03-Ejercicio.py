
# Este programa convierte una cantidad de dinero de una divisa a otras.

# Divisas soportadas: USD, EUR, MXN
# Si ingresas ejemplo 100 USD, debes calcular, EUC y MXN.

# Debemis ingresar la cantidad y la divisa.
print("""Bienvenidos a la calculadora de divisas
Para Salir escibe Salir
Las operaciones son USD, EUR, MXN""")

# Tasas de conversion
# 1 USD = 0.95 EUR
# 1 USD = 20.28 MXN
# 1 EUR = 21.36 MXN

resultado_usd = 0
resultado_mxn = 0
resultado_eur = 0
cantidad = ""

while True:
    if not cantidad:
        cantidad = input("Ingrese Cantidad: ")
        if cantidad.lower() == "salir":
            break
        cantidad = int(cantidad)
    op = input("Ingresa divisa: ")
    if op.lower() == "salir":
        break

    if op.lower() == "usd":
        resultado_eur = cantidad * 0.95
        resultado_mxn = cantidad * 20.28
        print(f"{resultado_eur} EUR, {resultado_mxn} MXN")
    if op.lower() == "eur":
        resultado_usd = cantidad / 0.95
        resultado_mxn = cantidad * 21.36
        print(f"{resultado_usd} USD, {resultado_mxn} MXN")
    if op.lower() == "mxn":
        resultado_usd = cantidad / 20.28
        resultado_eur = cantidad / 21.36
        print(f"{resultado_usd} USD, {resultado_eur} EUR")
    else:
        print("Operacion no valida")
        break

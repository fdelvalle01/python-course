
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


tasa_USD_a_EUR = 0.95
tasa_USD_a_MXN = 20.28
tasa_EUR_a_MXN = 21.36


cantidad = ""

while True:
    if not cantidad:
        cantidad = input("Ingrese Cantidad: ")
        if cantidad.lower() == "salir":
            break
        cantidad = float(cantidad)
    op = input("Ingresa divisa: ")
    if op.lower() == "salir":
        break

    if op.lower() == "usd":
        resultado_eur = cantidad * tasa_USD_a_EUR
        resultado_mxn = cantidad * tasa_USD_a_MXN
        print(f"{resultado_eur:.2f} EUR, {resultado_mxn:.2f} MXN")
    if op.lower() == "eur":
        resultado_usd = cantidad / tasa_USD_a_EUR
        resultado_mxn = cantidad * tasa_USD_a_MXN
        print(f"{resultado_usd:.2f} USD, {resultado_mxn:.2f} MXN")
    if op.lower() == "mxn":
        resultado_usd = cantidad / tasa_USD_a_MXN
        resultado_eur = cantidad / tasa_EUR_a_MXN
        print(f"{resultado_usd:.2f} USD, {resultado_eur:.2f} EUR")
    else:
        print("Operacion no valida")
        break


# :.2f esto sirve para mostrar exactamente el numero con 2 decimables dentro de un f-String en python

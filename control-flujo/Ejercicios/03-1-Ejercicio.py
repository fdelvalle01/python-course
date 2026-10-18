print("Bienvenido al conversor de divisas")

cantidad = float(input("Introduce la cantidad a convertir: "))
divisa_origen = input(
    "Introduce la divisa de origen (USD, EUR, MXN): ").upper()

divisa_disponible = ["USD", "EUR", "MXN"]

if divisa_origen not in divisa_disponible:
    print("Divisa de origen no valida.")
    exit()


tasa_USD_a_EUR = 0.95
tasa_USD_a_MXN = 20.28
tasa_EUR_a_MXN = 21.36


if divisa_origen == "USD":
    cantidad_euros = cantidad * tasa_USD_a_EUR
    cantidad_pesos = cantidad * tasa_USD_a_MXN
    print(
        f"Por tu(s): {cantidad:.2f} dolar(es) obtendras. {cantidad_euros:.2f} euros o {cantidad_pesos:.2f} pesos mexicandos.")
elif divisa_origen == "EUR":
    cantidad_dolares = cantidad / tasa_USD_a_EUR
    cantidad_pesos = cantidad * tasa_USD_a_MXN
    print(f"Por tu(s): {cantidad:.2f} dolar(es) obtendras. {cantidad_dolares:.2f} dolares o {cantidad_pesos:.2f} pesos mexicandos.")
else:
    cantidad_dolares = cantidad / tasa_USD_a_EUR
    cantidad_euros = cantidad / tasa_USD_a_MXN
    print(
        f"Por tu(s): {cantidad:.2f} dolar(es) obtendras. {cantidad_dolares:.2f} dolares o {cantidad_euros:.2f} euros.")

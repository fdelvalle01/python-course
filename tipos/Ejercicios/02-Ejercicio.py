#Esteprograma calcula cuanto costaria un producto en diferentes monedas extranjeras a partir 
#de una cantidad ingresada en moneda local. 

#1 Solicitar al usuario que ingrese una cantidad en su moneda local. ejemplo CLP 
cantidad = int(input("Ingresa la moneda local: "))

moneda_usd = cantidad * 0.050
moneda_eur = cantidad * 0.047
moneda_gbp = cantidad * 0.039
moneda_jpy = cantidad * 7.71

print(f"Cantidad equivalente en USD: {moneda_usd}, EUR: {moneda_eur}, GBP: {moneda_gbp}, JPY: {moneda_jpy}")
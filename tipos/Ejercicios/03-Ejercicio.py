# Calculadora de Cambio. 
# Solicitar al usuario dos datos: 

# 1 Cantidad de dinero entregada por el cliente 

cantidad_cliente = float(input("Cantidad de dinero entregada x cliente: "))

costo_producto = float(input("Costo del producto: "))

# Calcular el cambio restando el costo del producto al dinero entregado. 

total_devolver = cantidad_cliente - costo_producto

print(f"Total a devolver: {total_devolver}")
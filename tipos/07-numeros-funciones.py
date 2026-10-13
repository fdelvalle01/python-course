print(round(1.3)) # out: 1 -> Devuelve el numero que se encuentra mas cercano. 
# 1.3 se encuentra mas cercano de 1 o de 2 ?? obviamente de 1. 

print(round(1.7)) # out: 2


print(round(1.5)) # out: 2


print(abs(-77)) # out: 77 entrega el valor absoluto del valor que le entregamos al a funcion


# Tambien python tiene un modulo que nos permite trabajar con muchos numeros de manera nativa 
# ejemplo math

import math

# Ejemplo pensemos que math => math.py codigo python nativo para matematicas 

print(math.ceil(1.1)) #Ceil tomara el numero mas cercano y lo subira arriba ejemplo 2

print(math.floor(1.9999)) # tomara el numero y lo llevara hacia el numero entero mas cercano hacia abajo

print(math.isnan(22)) # Preguntaria si el valor que le pasamos no es un numero
#print(math.isnan("22")) # Esto generara error. 

print(math.pow(10, 3 )) # elevar un valor a 3 ejemplo 

print(math.sqrt(9)) # obtener la raiz cuadrada de nueve. 3
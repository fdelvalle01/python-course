##Para una calculadra como podriamos obtener datos del usuario ? 

n1 = input("Ingresa el primer numero: ")
n2 = input("Ingresa el segundo numero: ")

print(n1+ n2)

# hon.exe c:/Users/Francisco/Desktop/Learning/python-course/tipos/calculadora.py
# Ingresa el primer numero: 3
# Ingresa el segundo numero: 2
# 32 => Esto esta mal ya que son string, en python debemos transformar los valores de String a int

#ejemplo

n1 = int(n1)
n2 = int(n2)
print(n1 + n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2 
devi = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2}
el resultado de la suma es {suma}
el resultado de la resta es {resta}
el resultado de la multi es {multi}
el resultado de la devi es {devi}
"""
#Si no se le pone f al inicio. sera solo todo string. se debe poner f siempre para imprimir 
#variable 

print(mensaje)
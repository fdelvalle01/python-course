numero = 1
# Queremos duplicar el numero hasta que este sea < a 100 

while numero < 100:
    print(numero)
    numero *= 2



# Con esto podemos simular el ingreso de comandos. ejemplo comando salir 
# utilizando while, osea hasta que el valor sea igual a algo. 
# lower() se utiliza convierte todo a minusculas. 
comandos = ""
while comandos.lower() != "salir":
    comandos = input("$ ")
    print(comandos)

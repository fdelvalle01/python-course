# and, or, not
# GAS = False
# ENCENDIDO = True
# EDAD = 18

# if not GAS and (ENCENDIDO or EDAD > 17): 
#     print("Puedes avanzar")

# Operador de corto-circuito.
# Las operaciones en generar se ejecutan de izquierda a derecha. a excepcion de si tienes un () 
# Matematicamente se ejecutarian lo que esta dentro de los parentecis.
GAS = False
ENCENDIDO = True
EDAD = 18

if GAS or ENCENDIDO or EDAD > 17:
    print("Puedes avanzar")

# Uso de if
EDAD = 60

# El if siempre es identado. si no genera error. los 4 espacioes son importates 
# para que sea considerado dentro del if. ademas despues de el if se deben
# agregar los ':'

if EDAD > 65:
    print("Puede ver la pelicula con super descuento. ")

elif EDAD > 54:
    print("Puedes ver la pelicula con descuento")

elif EDAD > 17:
    print("Puedes ver la pelicula")

else:
    print("No puedes entrar")

# EL ORDEN EN EL QUE SE COLOCAN LOS IF Y LAS CONDICIONES SON IMPORTANTES.

print("Listo")

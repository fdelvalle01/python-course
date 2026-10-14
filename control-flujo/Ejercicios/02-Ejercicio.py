# Verificacion de Tweets 

# Este programa solicita al usuario que ingrese un tweet y verifica si cumple con el limite de 20 caracteres. 

tweet = input("Ingrese el tweet ")

if tweet != "":
    if len(tweet) <= 20:
        print("Su tweet ha sido publicado.")
    elif len(tweet) > 20:
        print("Ha sobrepasado el limite de su publicacion.")
else:
    print("No se puede publciar un twwt vacio")
    
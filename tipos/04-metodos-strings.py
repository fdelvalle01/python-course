animal = "   chanCHito feliz    "

# ¿Que son los metodos?
# Los metodos son funciones que se encuentran dentro de un objeto.

# Estos son metodos ejemplo upper() upper esta tomando los valores de la variable animal
print(animal.upper())  # out: CHANCHITO FELIZ

# y los transforma en mayusculas.
# caso contrario de upper es lower, convierte todo a minusculas.
print(animal.lower())  # out: chanchito feliz

# Otro metodo es el capitalize() que nos permite tomar un String y si esta todo en minusculas
# Asigna la primera letra en mayusculas, utilizando capital letter por ejemplo
print(animal.capitalize())  # out: Chanchito feliz

# Tambien podemos encadenar los metodos, como por ejemplo
print(animal.strip().capitalize())  # out: Chanchito feliz

# Otro metodo muy similar a capitalize es title, pero la diferencia es que convierte en mayusculas
# los primeros caracteres pero al texto completo, como un titulo. :)
print(animal.title())  # out: Chanchito Feliz

# Hay metodos como por ejemplo Strip, este es el que remueve todo los espacios que estan en la izquierda
# y derecha. ejemplo
print(animal.strip())  # out: Chanchito Feliz

# thon.exe "c:/Users/fdel_/OneDrive/Escritorio/Aprendiendo Python - IA/python-course/tipos/04-metodos-strings.py"
#    CHANCHITO FELIZ
#    chanchito feliz
#    chanchito feliz
#    Chanchito Feliz
# chanchito feliz
# PS C:\Users\fdel_\OneDrive\Escritorio\Aprendiendo Python - IA>

# Tambien existen metodos strip pero para sacar los espacios de un lado, ya sea izquierda o derecha
# ejemplo

print(animal.lstrip())  # Saca los espacios de la izquierda "left"

print(animal.rstrip())  # Saca los espacios de la derecha "right"


# Otro metodo util es el find() find buscara una cadena de caracteres que nosotros le indiquemos.
# Este devuelve el indice.

# out: 7 si no lo encuentra entregara un -1 => no lo encontre. si es positivo entonces si lo encontro.
print(animal.find("CH"))

# Metodo replace,
print(animal.replace("nCH", "j"))
# out: chajito feliz => Si no la encuentra no hara nada, si la encuentra lo remplazada


# ni en un caracter dentro de un String
print("nCH" in animal)  # out: true =>

# Cual es la diferecnia de find ??
# Find devuelve el indice de donde se encuentra la cadena de caracteres y el in devuelve el boolean
# es decir si se encuentra o no, true o false.

# Aca buscamos si esta cadena de caracteres NO se encuentra en el String.
print("nCH" not in animal)  # out: False

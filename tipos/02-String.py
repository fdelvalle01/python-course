nombre_curso = "Ultimate Python"

descripcion_curso = """
Ultimate Python, 
Este curso contempla todos los detalles
que necesitas para encontrar un trabajo.
"""

print(nombre_curso, descripcion_curso)


# len nos permite obtener la longitud que tiene un string.

# Los argumentos son los valores que nosotros le pasamos a una funcion
print(len(nombre_curso))
# nombre_curso es el argumento de la funcion len. y con print lo podemos imprimir

# PS C:\Users\fdel_\OneDrive\Escritorio\Aprendiendo Python - IA> & C:\Users\fdel_\AppData\Local\Programs\Python\Python313\python.exe "c:/Users/fdel_/OneDrive/Escritorio/Aprendiendo Python - IA/python-course/tipos/02-String.py"
# Ultimate Python
# Ultimate Python,
# Este curso contempla todos los detalles
# que necesitas para encontrar un trabajo.

# 15
# PS C:\Users\fdel_\OneDrive\Escritorio\Aprendiendo Python - IA>

# De esta forma con los [] podemos acceder a un caracter de un string ejemplo el resultado es U
print(nombre_curso[0])

# PS C:\Users\fdel_\OneDrive\Escritorio\Aprendiendo Python - IA> & C:\Users\fdel_\AppData\Local\Programs\Python\Python313\python.exe "c:/Users/fdel_/OneDrive/Escritorio/Aprendiendo Python - IA/python-course/tipos/02-String.py"
# U
# PS C:\Users\fdel_\OneDrive\Escritorio\Aprendiendo Python - IA>


# Tambien existen formas de poder recortar un string con el siguiente ejemplo

# eJEMPLO ACA Tomara desde la posicion 0 hasta la 8 y solo mostrara eso
print(nombre_curso[0:8])
# Ultimate


# Hay casos en donde lo podemos dejar asi y lo que significa es que partira de la posicion
print(nombre_curso[9:])
# 9 y imprimira todo hasta el final. siempre y cuando no le pasemos la segunda variable despues de :

# Formato de String
# Normalmente podemos concatenar 2 variables String de esta forma.
nombre = "Francisco"
apellido = "Del Valle"
nombre_completo = nombre + " " + apellido

print(nombre_completo)  # out: Francisco Del Valle

# Pero existe una mejor manera y mas rapida de poder escribir el codigo y concatenar
# para eso usamos la funcion f"{}" la cual nos permitira llamar a las variabels declaradas y ademas
# Escribir texto ejemplo

nombre_completo2 = f"Mi nombre: {nombre} {apellido}"
print(nombre_completo2)  # out:  Mi nombre: Francisco Del Valle

# Tambien podemos generar operaciones o utilizar expreciones que nosotros queramos...
nombre_completo3 = f"Mi nombre: {nombre[0]} {2 + 5}"
print(nombre_completo3)  # out:  Mi nombre: F 7

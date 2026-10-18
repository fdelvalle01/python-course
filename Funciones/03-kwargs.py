# keyword arguments.
# los ** son para poder trabajar los kwargs. a diferencia de los xargs con un solo *
def get_product(**datos):
    print(datos)  # Para poder acceder a los valores se usa el []
    print(datos["id"], datos["name"], datos["desc"])


# out: {'id': 'id'} => Esto es un diccionario o un objeto..
# Parametros y argumentos
get_product(id="23", name="iPhone", desc="Esto es un iPhone")

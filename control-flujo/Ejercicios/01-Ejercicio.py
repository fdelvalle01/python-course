
print("""Bienvenidos a la calculadora
Para Salir escibe Salir
Las operaciones son suma, multi, div y resta""")

# operation_type = ""
# result = 0

# while operation_type.lower() != "salir":
#     operation_type = input("Ingresa operacion: ")
#     number1 = int(input("Ingresa numero: "))
#     number2 = int(input("Ingresa numero: "))

#     if operation_type == "suma":
#         result = number1 + number2
#     elif operation_type == "multi":
#         result = number1 * number2
#     elif operation_type == "div":
#         result = number1 / number2
#     elif operation_type == "resta":
#         result = number1 - number2
#     else:
#         print("Operacion no valida.")
#     print(f"El resultado es {result} ")


resultado = ""

while True: 
    if not resultado: 
        resultado = input("Ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresa operacion: ")
    if op.lower() == "salir":
        break
    #Ahora debemos preguntarle el siguiente numero al usuario

    n2 = input("Ingresa el siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2  = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operacion no valida")
        break

    print(f"El resultado es: {resultado}")


grado_celsius = float(input("Ingresa grados Celsius: ")) #Esto es String, se debe transformar a number o float

grado_fahrenheit = (grado_celsius * 9/5) + 32
grado_kelvin = grado_celsius + 273.15

print(f"Temperatura grados Celsis: {grado_celsius}")
print(f"""Temperatura grados Fahrenheit: {grado_fahrenheit}""")
print(f"""Temperatura grados Kelvin: {grado_kelvin}""")
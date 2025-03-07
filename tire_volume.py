import math
import datetime
import os

# Definir el nombre del archivo
filename = "volumes.txt"

# Verificar si el archivo existe para escribir los encabezados solo una vez
file_exists = os.path.isfile(filename)

# Solicitar datos al usuario
width = float(input("Enter the tire width (mm): "))
ratio = float(input("Enter the tire aspect ratio: "))
diameter = float(input("Enter the wheel diameter (inches): "))

# Calcular el volumen del neumático en litros
volume_liters = (math.pi * width**2 * ratio * (width * ratio + 2540 * diameter)) / 10000000000

# Obtener la fecha actual sin la hora
current_date = datetime.date.today()

# Abrir el archivo en modo de adición
with open(filename, "a") as file:
    # Si el archivo no existe, escribir los encabezados
    if not file_exists:
        file.write("Date,Tire Width (mm),Aspect Ratio,Wheel Diameter (in),Tire Volume (L)\n")
    
    # Escribir los datos en la tabla
    file.write(f"{current_date},{width},{ratio},{diameter},{volume_liters:.2f}\n")

print(f"The tire volume is: {volume_liters:.2f} liters. The data has been saved in volumes.txt.")



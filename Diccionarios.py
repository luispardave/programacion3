#Diccionarios 

# Materia: Programacion III
# Nombre: Luis Angel Pardave Garcia
# Proyecto: DDiccionarios
# Descripcion: Practica de diccionarios

"""agenda = [
{
        "Nombre" : "Luis",
        "Telefono" : 123456789,
        "Correo" : "luis@udg.mx",
        "Direccion" : "Av. Universidad 123",
},
{
        "Nombre" : "Carlos",
        "Telefono" : 123456789,
        "Correo" : "carlos@udg.mx",
        "Direccion" : "Av. Universidad 123",
}
]

diccionario = {
        "Nombre" : "Luis",
        "Telefono" : 123456789,
        "Correo" : "luis@udg.mx",
        "Direccion" : "Av. Universidad 123",
}

print(agenda[1]["Correo"])

for clave, valor in diccionario.items():
    #print(clave, valor, "\n")
        pass

for clave in diccionario.keys():
    print(clave)
    pass

print("\n")
pass

for valor in diccionario.values():
    print(valor)
    pass"""

alumno = {
     "Nombre": "Carlos",
     "Edad": 20,
     "Carrera": "Licenciatura en Inteligencia Artificial y Ciencia de Datos",
     "Promedio": 8.7,
}

alumno["Telefono"] = "123456789"

#Mostrar nombre del alumno
print(alumno["Nombre"])
print("-------------------------")
print("\n")

#Mostrar el promedio
print(alumno["Promedio"])
print("-------------------------")
print("\n")

#Mostrar la suma de edad + promedio
print(alumno["Edad"] + alumno["Promedio"])
print("-------------------------")
print("\n")

#Usa for y hacer un print solo de los valores
for key, value in alumno.items():
    print("-------------------------")
    print(value)


for key in alumno.keys():
    print("-------------------------")
    print(key)
    
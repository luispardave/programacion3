
calificaciones = [80, 90, 70, 100]

def promedio(lista):
    return sum(lista) / len(lista)

resultado = promedio(calificaciones)
print(f"El promedio de las calificaciones es: {resultado}")
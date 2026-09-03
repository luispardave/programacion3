#Sistema de calificiones

calificaciones = [ 80, 90, 75, 100, 65]

def mostrar_calificaciones(lista):
    for elemento in lista:
        print(elemento)
        
def calcular_promedio(lista):
    return sum(lista) / len(lista)

def obtener_mayor(lista):
    return max(lista)

def obtener_menor(lista):
    return min(lista)

def buscar_calificacion(lista, calificacion):
    for elemento in lista:
        if elemento == calificacion:
            return elemento
    return "Calificación no encontrada"

mostrar_calificaciones(calificaciones)
print(f"Promedio: {calcular_promedio(calificaciones)}")
print(f"Mayor calificación: {obtener_mayor(calificaciones)}")
print(f"Menor calificación: {obtener_menor(calificaciones)}")
print(buscar_calificacion(calificaciones, 50))


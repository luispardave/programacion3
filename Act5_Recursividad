#Recursividad Actividad 5

personas = ["Ana", "Carlos", "Pedro"]

def buscar (persona, posicion):
    if posicion >= len(personas):
        return "No se encontró a la persona"

    if persona == personas[posicion]:
        return "Localizado en la posición: " + str(posicion)

    return buscar(persona, posicion + 1)

print(buscar("Pedro", 0))
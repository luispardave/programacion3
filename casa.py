casa ={
    "Entrada": ["Sala"],
    "Sala": ["Entrada", "Cocina", "Baño"],
    "Cocina": ["Sala", "Cuarto"],
    "Baño": ["Sala"],
    "Cuarto": ["Cocina"]
}

visitadas = []

def visitar(habitacion):
    
    # Si ya lo visitamos esta habitacion, terminamos
    if habitacion in visitadas:
        return

    # Visitamos la habitacion
    print("Visitando:", habitacion)
    visitadas.append(habitacion)

    # Visitamos sus vecinos
    for vecino in casa[habitacion]:
        visitar(vecino)

visitar("Cuarto")
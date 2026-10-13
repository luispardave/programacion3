class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.vecinos = []

    def __repr__(self):
        return f"{self.valor}"


A = Nodo("A")
B = Nodo("B")
C = Nodo("C")
D = Nodo("D")

visitados = []

def conectar(origen, destino, peso):
    origen.vecinos.append((destino, peso))

def recorrer(nodo, visitados, distancia_acumulada=0):
    if nodo in visitados:
        return

    visitados.append(nodo)
    print(f"{nodo.valor} - Distancia acumulada: {distancia_acumulada}")

    for vecino, peso in nodo.vecinos:
        recorrer(vecino, visitados, distancia_acumulada + peso)

#Camino derecho
conectar(A, B, 8)
conectar(B, D, 2)
conectar(D, C, 7)

#Camino izquierdo




recorrer(A, visitados)

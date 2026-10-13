
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

def recorrer(nodo, visitados):
    if nodo in visitados:
        return

    visitados.append(nodo)
    print(nodo.valor)

    for vecino in nodo.vecinos:
        recorrer(vecino, visitados)

A.vecinos.append(B)
A.vecinos.append(C)
B.vecinos.append(D)
C.vecinos.append(D)
D.vecinos.append(C)

recorrer(A, visitados)
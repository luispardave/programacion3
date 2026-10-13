
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = {}

class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, nombre):
        self.nodos[nombre] = Nodo(nombre)

    def agregar_conexion(self, origen, destino, peso):
        self.nodos[origen].vecinos[destino] = peso
        self.nodos[destino].vecinos[origen] = peso  

    def dijkstra(self, inicio, destino):
        distancias = {}
        anteriores = {}
        visitados = set()

        for nombre in self.nodos:
            distancias[nombre] = float('inf')
            anteriores[nombre] = None

        distancias[inicio] = 0

        while len(visitados) < len(self.nodos):
            nodo_actual = None
            menor_distancia = float('inf')

            for nombre in self.nodos:

                if nombre not in visitados:

                    if distancias[nombre] < menor_distancia:
                        menor_distancia = distancias[nombre]
                        nodo_actual = nombre

            if nodo_actual is None:
                break

            if nodo_actual == destino:
                break

            visitados.add(nodo_actual)

            nodo = self.nodos[nodo_actual]

            for vecino, peso in nodo.vecinos.items():

                nueva_distancia = (
                    distancias[nodo_actual] + peso
                )

                if nueva_distancia < distancias[vecino]:

                    distancias[vecino] = nueva_distancia
                    anteriores[vecino] = nodo_actual

        camino = []
        actual = destino

        while actual is not None:
            camino.append(actual)
            actual = anteriores[actual]

        camino.reverse()
        return distancias[destino], camino

g = Grafo()
g.agregar_nodo("A")
g.agregar_nodo("B")
g.agregar_nodo("C")
g.agregar_nodo("D")
g.agregar_nodo("E")
g.agregar_nodo("F")
g.agregar_conexion("A", "B", 35)
g.agregar_conexion("B", "D", 5)
g.agregar_conexion("D", "F", 7)
g.agregar_conexion("A", "C", 1)
g.agregar_conexion("C", "E", 6)
g.agregar_conexion("E", "F", 9)
distancia, camino = g.dijkstra("A", "B")
print(f"Distancia mínima de A a B: {distancia}")
print(f"Camino: {' -> '.join(camino)}")

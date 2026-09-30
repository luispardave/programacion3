#Conectando POO con Estructuras de Datos

class Nodos:
    def __init__(self,valor):
        self.valor=valor
        self.izq = None # Apunta a otro OBJETO Nodo
        self.der = None # Apunta a otro OBJETO Nodo

def recorrer(nodo):
    if nodo is None:
        return

    print(nodo.valor)

    recorrer(nodo.izq)
    recorrer(nodo.der)

#Construccion del Arbol

raiz = Nodos(10)
raiz.izq = Nodos(5)
raiz.der = Nodos(15)
raiz.izq.izq = Nodos(20)

recorrer(raiz)

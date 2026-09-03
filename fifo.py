from collections import deque

# FIFO: el primero en entrar es el primero en salir
cola = deque()

cola.append("A")  # entra A
cola.append("B")  # entra B
cola.append("C")  # entra C

print("Cola:", list(cola))

while cola:
    elemento = cola.popleft()  # sale el más antiguo
    print("Atendido:", elemento)

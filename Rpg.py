
class Personaje :

    def __init__(self, nombre, vida, fuerza):
        self.nombre = nombre
        self.__vida = vida
        self.fuerza = fuerza

#Recibe "enemigo" como un OBJETO completo
    def atacar(self, enemigo):
        print(f"\n{self.nombre} ataca a {enemigo.nombre}")
        #enemigo.vida -= self.fuerza
        enemigo.SetVida(enemigo.GetVida() - self.fuerza)
        print(f"{enemigo.nombre} ahora tiene {enemigo.GetVida()} de vida \n")

    def esta_vivo(self):
        if self.GetVida() > 0:
            print(f"{self.nombre} está vivo con {self.GetVida()} de vida")
            return True
        else:
            print(f"{self.nombre} ha muerto")
            return False

    def GetVida(self):
        return self.__vida

    def SetVida(self, vida):
        self.__vida = vida

caballero = Personaje("Sir Arthur", 100, 20)
orco = Personaje("Grommash", 120, 15)

while True:
    caballero.atacar(orco)
    if not orco.esta_vivo():
        break

    orco.atacar(caballero)
    if not caballero.esta_vivo():
        break

print(f"\nGanador: {caballero.nombre if caballero.GetVida() > 0 else orco.nombre}")


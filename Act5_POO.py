#Clase padre
class Animal:
    # Constructor de la clase padre
    def __init__(self, color):
        self.color = color
        
    #Atributo de la clase padre
    def cagar(self):
        print(f"Este {self.nombre} tuvo que hacer del baño")

#Creacion de clase
class Perro(Animal):
    #El construcuor de la clase
    def __init__(self, nombre_recibido, edad_recibida, color):
        super().__init__(color)
        self.nombre = nombre_recibido
        self.edad = edad_recibida

    # Getter de la clase
    def getNombre(self):
        return self.nombre
    
    # Setter de la clase
    def setNombre(self, nombre_recibido):
        self.nombre = nombre_recibido
        
    # Getter de la clase
    def getEdad(self):
        return self.edad

    # Setter de la clase
    def setEdad(self, edad_recibida):
        self.edad = edad_recibida 
    
    # Metodo de la clase
    def ladrar(self):
        print(f"Guau Guau! Soy {self.nombre} , tengo {self.edad} años y mi color es {self.color}.")
    

#Intanciar(crear) un objeto de la clase Perro
perro1 = Perro("Firulais", 3, "blanco")
perro2 = Perro("Toby", 5, "negro")

perro1.ladrar()
perro1.cagar()
perro2.ladrar()
perro2.cagar()

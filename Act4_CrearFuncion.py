#Actividad 4: Crear tu funcion

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
nombre2 = input("Ingrese su segundo nombre: ")
edad2 = input("Ingrese su edad: ")
nombre3 = input("Ingrese su tercer nombre: ")
edad3 = input("Ingrese su edad: ")

def presentar(nombre, edad):
    print(f"Hola mucho gusto {nombre}, tienes {edad} años.")

presentar(nombre, edad)
presentar(nombre2, edad2)
presentar(nombre3, edad3)
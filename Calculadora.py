#Sentencia Return

a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    else:
        return a / b
    

resultado = sumar(a,b)
print(f"El resultado de la suma es: {resultado}")

resultado = restar(a,b)
print(f"El resultado de la resta es: {resultado}")

resultado = multiplicar(a,b)
print(f"El resultado de la multiplicación es: {resultado}")

resultado = dividir(a,b)
print(f"El resultado de la división es: {resultado}")
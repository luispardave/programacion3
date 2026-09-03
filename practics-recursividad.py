
# funcion contador
def contador(numero):
    if numero == 0:
        return 
    print(numero)
    numero -= 1
    return contador(numero)
contador(10)

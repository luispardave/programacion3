lista = ['a', 1, 'd', 'Colores', False, 3.9, 14, True, False, 88, 4.2]

nueva_lista = []
nueva_lista2 = []

for elemento in lista:
    print(elemento)
    if type(elemento) == int:
        nueva_lista.append(elemento + 10)
    elif type(elemento) == float:
        nueva_lista.append(elemento + 2.5)
    elif type(elemento) == bool:
        nueva_lista.append(not elemento)
    else:
        nueva_lista.append(elemento)

print(nueva_lista)


for indice in range(len(lista)):
    
    if type(lista[indice]) == int:
        nueva_lista2.append(lista[indice] + 10)
    elif type(lista[indice]) == float:
        nueva_lista2.append(lista[indice] + 2.5)
    elif type(lista[indice]) == bool:
        nueva_lista2.append(not lista[indice])
    else:
        nueva_lista2.append(lista[indice])
print(nueva_lista2)
       











# Output esperado [a, 11, d, "Colores", True, 6.4, 24, False, True, 98, 6.7]

    











# Output esperado [a, 11, d, "Colores", True, 6.4, 24, False, True, 98, 6.7]
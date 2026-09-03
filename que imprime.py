
frutas = ["manzana", "banana", "naranja", "uva"]
print(frutas)

print(frutas[0]) 
print(frutas[1]) 
print(frutas[2])  
print(frutas[-1])

frutas[1] = "fresas"
print (frutas)

print(frutas[0]) 
print(frutas[1]) 
print(frutas[2])  
print(frutas[-1])  

#pop (indice)

lista_nombres = ["Diego", "Karol", "Daniel", "Paola", "Kevin"]
print(lista_nombres)
for i in range(len(lista_nombres)):
    if lista_nombres[i] == "Karol":
        print("Ya tenemos el indice, de Karol", i)
        lista_nombres.pop(i)
        print("Se elimino a Karol de la lista")
        print(lista_nombres)
        break


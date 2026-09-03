
print("Recursividad para contar letras en una palabra")
print("Ingrese una palabra y una letra para contar cuántas veces aparece la letra en la palabra.")

palabra = input("Ingrese una palabra: ")
letra = input("Ingrese una letra: ")

def contar_letras(palabra, letra):
    if len(palabra) == 0:
        return 0
    else:
        if palabra[0] == letra:
            return 1 + contar_letras(palabra[1:], letra)
        else:
            return contar_letras(palabra[1:], letra)

print(f"La letra '{letra}' aparece {contar_letras(palabra, letra)} veces en la palabra '{palabra}'.")
print(f"----------------------------------------------------\n")


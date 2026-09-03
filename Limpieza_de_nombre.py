#Limpieza de nombre

texto = "  juAn peRez  "
print(f"Nombre original: '{texto}'")
print(f"Nombre limpio: '{texto.strip()}'")
print(f"Nombre en mayúsculas: '{texto.strip().upper()}'")
print(f"Nombre en minúsculas: '{texto.strip().lower()}'")
print(f"Nombre con la primera letra en mayúscula: '{texto.strip().capitalize()}'")
print(f"Texto en formato lista: '{texto.strip().split(" ")}'")
print(f"Primer nombre: '{texto.strip().split(" ")[0].capitalize()}'")
print(f"Segundo nombre: '{texto.strip().split(" ")[1].capitalize()}'")

texto_2 = str(input("Ingrese otro nombre: "))
print(f"Nombre original: '{texto_2}'")
print(f"Nombre limpio: '{texto_2.strip()}'")
print(f"Nombre en mayúsculas: '{texto_2.strip().upper()}'")
print(f"Nombre en minúsculas: '{texto_2.strip().lower()}'")
print(f"Nombre con la primera letra en mayúscula: '{texto_2.strip().capitalize()}'")
print(f"Texto en formato lista: '{texto_2.strip().split(" ")}'")
print(f"Primer nombre: '{texto_2.strip().split(" ")[0].capitalize()}'")
print(f"Segundo nombre: '{texto_2.strip().split(" ")[1].capitalize()}'")    

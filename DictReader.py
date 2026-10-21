"""
Titulo: DictReader
Nombre Completo: Luis Angel Pardave Garcia
Fecha de creación: 13 de Octubre de 2026 
Descripcion: pruebas de lectura de csv

"""


import csv

try:
    #Abrir archivo de nodos para grafo Djikstra
    with open('Nodos.csv', mode='r', encoding='utf-8') as file:
        try:
            reader = csv.DictReader(file)
            for row in reader:
                nodos = row['name']
                print(f"Evento registrado: {nodos}")
        except Exception as e:
            print(f"Error al leer el archivo CSV: {e}")

except Exception as error_general:
    print(f"Error general: {error_general}")



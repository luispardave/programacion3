"""
Titulo: Manejo de Excepciones
Nombre Completo: Luis Angel Pardave Garcia
Fecha de creación: 20/10/2026
Descripcion: Se crea un formulario para el manejo de excepciones en python
"""


# Excepcion personalizada
class EdadInvalidaError(Exception):
    """Se lanza cuando la edad ingresada esta fuera de rango."""
    pass


# 1. ZeroDivisionError y ValueError
def division():
    try:
        num = int(input("Ingrese un número: "))
        res = 100 / num
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except ValueError:
        print("Error: Debe ingresar un número válido.")
    else:
        print(f"Exito: el resultado es {res}")
    finally:
        print("Finalizando verificacion del bloque.")


# 2. IndexError
def indice_lista():
    frutas = ["manzana", "pera", "uva"]
    try:
        pos = int(input(f"Lista: {frutas}\nIngrese una posición (0-2): "))
        print(f"Exito: la fruta es {frutas[pos]}")
    except IndexError:
        print("Error: La posición está fuera del rango de la lista.")
    except ValueError:
        print("Error: Debe ingresar un número entero.")
    finally:
        print("Finalizando verificacion del bloque.")


# 3. KeyError
def buscar_diccionario():
    notas = {"ana": 18, "luis": 15, "maria": 20}
    try:
        nombre = input(f"Alumnos: {list(notas.keys())}\nIngrese un nombre: ").lower()
        print(f"Exito: la nota de {nombre} es {notas[nombre]}")
    except KeyError:
        print("Error: El alumno no existe en el diccionario.")
    finally:
        print("Finalizando verificacion del bloque.")


# 4. TypeError
def sumar_tipos():
    try:
        valor = input("Ingrese un valor para sumar a 10 (se suma como texto): ")
        res = 10 + valor  # int + str provoca TypeError
        print(f"Exito: el resultado es {res}")
    except TypeError:
        print("Error: No se pueden sumar tipos de datos diferentes (int + str).")
    finally:
        print("Finalizando verificacion del bloque.")


# 5. FileNotFoundError
def abrir_archivo():
    try:
        ruta = input("Ingrese el nombre del archivo a abrir: ")
        with open(ruta, "r", encoding="utf-8") as archivo:
            print("Exito: primeras líneas del archivo:")
            for _ in range(3):
                print(archivo.readline().rstrip())
    except FileNotFoundError:
        print("Error: El archivo no existe.")
    except PermissionError:
        print("Error: No tiene permisos para abrir el archivo.")
    finally:
        print("Finalizando verificacion del bloque.")


# 6. AttributeError
def llamar_metodo():
    try:
        metodo = input("Ingrese un método de texto (ej: upper, lower, title): ")
        texto = "hola mundo"
        res = getattr(texto, metodo)()
        print(f"Exito: el resultado es {res}")
    except AttributeError:
        print("Error: El objeto str no tiene ese método.")
    except TypeError:
        print("Error: Ese atributo no se puede llamar sin argumentos.")
    finally:
        print("Finalizando verificacion del bloque.")


# 7. NameError
def variable_inexistente():
    try:
        nombre = input("Ingrese el nombre de una variable (existe: 'saludo'): ")
        saludo = "Hola"
        print(f"Exito: el valor es {eval(nombre, {}, {'saludo': saludo})}")
    except NameError:
        print("Error: La variable no está definida.")
    except SyntaxError:
        print("Error: El nombre ingresado no es válido.")
    finally:
        print("Finalizando verificacion del bloque.")


# 8. Excepcion personalizada con raise
def validar_edad():
    try:
        edad = int(input("Ingrese su edad: "))
        if edad < 0 or edad > 120:
            raise EdadInvalidaError("La edad debe estar entre 0 y 120.")
        print(f"Exito: edad registrada {edad}")
    except ValueError:
        print("Error: Debe ingresar un número entero.")
    except EdadInvalidaError as e:
        print(f"Error: {e}")
    finally:
        print("Finalizando verificacion del bloque.")


# Menu principal
def menu():
    opciones = {
        "1": ("ZeroDivisionError / ValueError", division),
        "2": ("IndexError", indice_lista),
        "3": ("KeyError", buscar_diccionario),
        "4": ("TypeError", sumar_tipos),
        "5": ("FileNotFoundError", abrir_archivo),
        "6": ("AttributeError", llamar_metodo),
        "7": ("NameError", variable_inexistente),
        "8": ("Excepcion personalizada", validar_edad),
    }

    while True:
        print("\n===== FORMULARIO DE EXCEPCIONES =====")
        for clave, (nombre, _) in opciones.items():
            print(f"{clave}. {nombre}")
        print("0. Salir")

        try:
            opcion = input("Seleccione una opción: ")
            if opcion == "0":
                print("Saliendo del programa...")
                break
            opciones[opcion][1]()
        except KeyError:
            print("Error: Opción no válida.")
        except KeyboardInterrupt:
            print("\nPrograma interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"Error inesperado: {type(e).__name__} - {e}")


if __name__ == "__main__":
    menu()

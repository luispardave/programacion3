"""
Titulo: Manejo de Excepciones
Nombre Completo: Luis Angel Pardave Garcia
Fecha de creación: 20/10/2026
Descripcion: Se crea un formulario para el manejo de excepciones en python
             (ValueError, TypeError, KeyError, IndexError, FileNotFoundError).
             Cada dato se vuelve a solicitar mientras la entrada sea inválida.
"""

INVITADOS = {"ana": "Ana", "luis": "Luis", "maria": "Maria", "juan": "Juan", "pedro": "Pedro"}
BOTANAS = ["Doritos", "Ruffles", "Cheetos", "Sabritas", "Takis"]
EDAD_MINIMA = 18
LINEAS_A_MOSTRAR = 3


def pedir_invitado() -> str:
    """Solicita el nombre hasta que exista en la lista de invitados (KeyError)."""
    while True:
        try:
            nombre = input(f"Invitados: {list(INVITADOS.values())}\nSelecciona tu nombre: ").strip().lower()
            invitado = INVITADOS[nombre]
        except KeyError:
            print("Error: No existes en la lista de invitados. Intenta de nuevo.")
        else:
            print(f"Éxito: eres {invitado}. Gracias por confirmar tu asistencia.")
            return invitado
        finally:
            print(f"Verificacion completada.\n")


class MenorDeEdadError(Exception):
    """Se lanza cuando la edad ingresada es menor a EDAD_MINIMA."""


def pedir_edad() -> int:
    """Solicita la edad hasta que sea un entero mayor o igual a EDAD_MINIMA (ValueError y MenorDeEdadError)."""
    while True:
        try:
            edad = int(input("Ingresa tu edad: "))
            if edad <= 0:
                raise ValueError("La edad debe ser mayor a 0.")
            if edad < EDAD_MINIMA:
                raise MenorDeEdadError(f"Tienes {edad} años; se requieren al menos {EDAD_MINIMA}.")
        except ValueError:
            print("Error: Debe ingresar un número entero mayor a 0. Intenta de nuevo.")
        except MenorDeEdadError as error:
            print(f"Lo siento, eres menor de edad. {error} Intenta de nuevo.")
        else:
            print(f"Excelente, eres mayor de edad ({edad} años).")
            return edad
        finally:
            print("Fin de la verificación de la edad.\n")


def pedir_aportacion(total_comida: int = 0) -> int:
    """Solicita la aportación hasta que sea un entero no negativo (TypeError y ValueError)."""
    while True:
        valor = input("Ingresa cuánto aportarás a la comida: ").strip()
        try:
            try:
                # Se provoca a propósito un TypeError: input() siempre devuelve str (int + str).
                total_comida = total_comida + valor
            except TypeError:
                print("Aviso: No se pueden sumar tipos de datos diferentes (int + str). Convirtiendo a número...")
            aportacion = int(valor)
            if aportacion < 0:
                raise ValueError("La aportación no puede ser negativa.")
        except ValueError:
            print("Error: La aportación debe ser un número entero positivo. Intenta de nuevo.")
        else:
            total_comida += aportacion
            print(f"Éxito: tu aportación es de {aportacion}. Total de la comida: {total_comida}.")
            return total_comida
        finally:
            print("Fin de la verificación de la aportación.\n")


def pedir_botana() -> str:
    """Solicita una posición válida de la lista de botanas (ValueError e IndexError)."""
    ultima_posicion = len(BOTANAS) - 1
    while True:
        try:
            pos = int(input(f"Lista: {BOTANAS}\nSelecciona la botana (0-{ultima_posicion}): "))
            if pos < 0:
                raise IndexError("No se permiten posiciones negativas.")
            botana = BOTANAS[pos]
        except ValueError:
            print("Error: Debe ingresar un número entero. Intenta de nuevo.")
        except IndexError:
            print("Error: La posición está fuera del rango de la lista. Intenta de nuevo.")
        else:
            print(f"Éxito: la botana es {botana}")
            return botana
        finally:
            print("Fin de la verificación de la botana.\n")


def leer_archivo() -> None:
    """Solicita un archivo existente y muestra sus primeras líneas (FileNotFoundError)."""
    while True:
        ruta = input("Ingrese el nombre del archivo a abrir (deje vacío para omitir): ").strip()
        if not ruta:
            print("Lectura de archivo omitida.")
            return
        try:
            with open(ruta, "r", encoding="utf-8-sig") as archivo:
                print("Éxito: primeras líneas del archivo:")
                for _ in range(LINEAS_A_MOSTRAR):
                    print(archivo.readline().rstrip())
        except FileNotFoundError:
            print("Error: El archivo no existe. Intenta de nuevo.")
        else:
            return
        finally:
            print("Fin de la verificación del archivo.\n")


def llenar_formulario() -> None:
    """Ejecuta cada paso del formulario en orden."""
    pedir_invitado()
    pedir_edad()
    pedir_aportacion()
    pedir_botana()
    leer_archivo()


if __name__ == "__main__":
    llenar_formulario()

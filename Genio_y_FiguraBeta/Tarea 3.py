
def reloj_arena(simbolo, n, tipo):
    for i in range(n):
        espacios = min(i, n - 1 - i)
        ancho = n - 2 * espacios

        if tipo == 1 or ancho == 1:
            print(" " * espacios + simbolo * ancho)
        else:
            print(" " * espacios + simbolo +
                  " " * (ancho - 2) + simbolo)


def rombo(simbolo, n, tipo):
    mitad = n // 2

    for i in range(n):
        espacios = abs(mitad - i)
        ancho = n - 2 * espacios

        if tipo == 1 or ancho == 1:
            print(" " * espacios + simbolo * ancho)
        else:
            print(" " * espacios + simbolo +
                  " " * (ancho - 2) + simbolo)


def mono(simbolo, n, tipo):
    mitad = n // 2

    for i in range(n):
        espacios = abs(mitad - i)
        ancho = n - 2 * espacios

        if tipo == 1:
            print(" " * espacios + simbolo * ancho)
        elif i == mitad:
            print(simbolo * n)
        else:
            print(" " * espacios + simbolo +
                  " " * (ancho - 2) + simbolo)


def copa(simbolo, n, tipo):
    mitad = n // 2

    # Parte superior de la copa
    for i in range(mitad + 1):
        espacios = mitad - i
        ancho = 2 * i + 1

        if tipo == 1:
            print(" " * espacios + simbolo * ancho)
        elif ancho == 1:
            print(" " * espacios + simbolo)
        else:
            print(" " * espacios + simbolo +
                  " " * (ancho - 2) + simbolo)

    # Tallo
    print(" " * mitad + simbolo)
    print(" " * mitad + simbolo)

    # Base
    if tipo == 1:
        print(simbolo * n)
    else:
        print(simbolo + " " * (n - 2) + simbolo)


def pedir_datos():
    simbolo = "*"

    while True:
        try:
            n = int(input("Ingrese la dimension (impar, de 5 a 21): "))
            if 5 <= n <= 21 and n % 2 != 0:
                break
            print("Error: debe ser un numero impar entre 5 y 21.")
        except ValueError:
            print("Error: ingrese un numero entero.")

    while True:
        print("\nTipo de figura:")
        print("1. Rellena")
        print("2. Hueca")

        try:
            tipo = int(input("Seleccione el tipo: "))
            if tipo in (1, 2):
                break
            print("Error: elija 1 o 2.")
        except ValueError:
            print("Error: ingrese 1 o 2.")

    return simbolo, n, tipo


def main():
    while True:
        print("\n========== MENU ==========")
        print("1. Reloj de arena")
        print("2. Rombo")
        print("3. Mono")
        print("4. Copa")
        print("5. Todas las figuras")
        print("6. Salir")

        try:
            opcion = int(input("Seleccione que desea imprimir: "))
        except ValueError:
            print("Error: ingrese un numero del 1 al 6.")
            continue

        if opcion == 6:
            print("Programa terminado.")
            break

        if opcion not in range(1, 6):
            print("Error: seleccione una opcion del 1 al 6.")
            continue

        simbolo, n, tipo = pedir_datos()

        figuras = {
            1: ("RELOJ DE ARENA", reloj_arena),
            2: ("ROMBO", rombo),
            3: ("MONO", mono),
            4: ("COPA", copa)
        }

        if opcion == 5:
            seleccionadas = figuras.values()
            print("\n===== TODAS LAS FIGURAS =====")
        else:
            seleccionadas = [figuras[opcion]]

        for nombre, funcion in seleccionadas:
            print("\n===== " + nombre + " =====\n")
            funcion(simbolo, n, tipo)

        input("\nPresione ENTER para continuar...")


main()

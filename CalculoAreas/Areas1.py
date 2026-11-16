
import math

opcion = -1

while opcion != 0:
    print("\n0. Salir del programa")
    print("1. Área de un triángulo")
    print("2. Área de un círculo")
    print("3. Área de un rectángulo")

    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        area = (base * altura) / 2
        print("El área del triángulo es:", area)

    elif opcion == 2:
        radio = float(input("Ingrese el radio: "))
        area = math.pi * radio ** 2
        print("El área del círculo es:", area)

    elif opcion == 3:
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        area = base * altura
        print("El área del rectángulo es:", area)

    elif opcion == 0:
        print("Programa terminado.")

    else:
        print("Opción no válida.")
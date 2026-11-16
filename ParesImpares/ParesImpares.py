
def es_par(n):
    """
    Determina si un número es par o impar.

    Parámetros:
        n (int): Número entero que se desea evaluar.

    Retorno:
        bool: True si el número es par,
              False si es impar.

    Excepciones:
        TypeError: Si el argumento no es un entero.
    """

    if not isinstance(n, int):
        raise TypeError("El argumento n debe ser entero")

    if n % 2 == 0:
        return True
    else:
        return False


# Programa principal
numero = int(input("Ingresa un número entero: "))

if es_par(numero):
    print("El número es par")
else:
    print("El número es impar")

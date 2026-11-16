import math


def es_primo(numero):
    """
    Descripción breve: Determina si un número entero es primo.

    Descripción detallada (Opcional):
    Comprueba si el número tiene divisores diferentes de 1 y de sí mismo,
    probando únicamente hasta la raíz cuadrada del número.

    Parámetros:
        numero (int): Número entero mayor que 1.

    Valor de retorno:
        bool: True si el número es primo, False si no lo es.

    Excepciones:
        ValueError: Si el número es menor o igual a 1.
        TypeError: Si el valor recibido no es un número entero.

    Ejemplos (opcional):
        es_primo(7) -> True
        es_primo(10) -> False
        es_primo(1) -> ValueError
        es_primo(3.5) -> TypeError
    """
    if not isinstance(numero, int):
        raise TypeError("El número debe ser un entero.")

    if numero <= 1:
        raise ValueError("El número debe ser mayor que 1.")

    limite = int(math.sqrt(numero)) + 1

    for divisor in range(2, limite):
        if numero % divisor == 0:
            return False

    return True


try:
    numero = int(input("Ingrese un número entero mayor que 1: "))
    print("¿El número es primo?", es_primo(numero))

except ValueError as e:
    print("Error:", e)
except TypeError as e:
    print("Error:", e)
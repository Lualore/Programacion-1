def area_triangulo(base, altura):
    """
    Descripción breve: Calcula el área de un triángulo.

    Parámetros:
        base (float): Base del triángulo.
        altura (float): Altura del triángulo.

    Valor de retorno:
        float: Área del triángulo.

    Excepciones:
        ValueError: Si la base o la altura son menores o iguales a cero.
    """
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser mayores que cero.")

    area = (base * altura) / 2
    return area


try:
    base = float(input("Ingrese la base del triángulo: "))

    if base <= 0:
        raise ValueError("La base debe ser mayor que cero.")

    altura = float(input("Ingrese la altura del triángulo: "))

    if altura <= 0:
        raise ValueError("La altura debe ser mayor que cero.")

    print("El área del triángulo es:", area_triangulo(base, altura))

except ValueError as e:
    print("Error:", e)
def es_numero_valido(cadena):
    """
    Descripción breve: Verifica si una cadena representa un número positivo.

    Descripción detallada (Opcional):
    Acepta solo dígitos y a lo más un punto decimal. Rechaza cadenas vacías,
    letras, símbolos y signos negativos.

    Parámetros:
        cadena (str): Texto ingresado por el usuario.

    Valor de retorno:
        bool: True si la cadena tiene formato de número, False si no.

    Ejemplos (opcional):
        es_numero_valido("5") -> True
        es_numero_valido("3.5") -> True
        es_numero_valido("abc") -> False
        es_numero_valido("1.2.3") -> False
        es_numero_valido("") -> False
    """
    cadena = cadena.strip()

    # Quita el primer punto (si existe) y revisa que todo lo demás sean dígitos
    return cadena.replace(".", "", 1).isdecimal()


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

    return (base * altura) / 2


try:
    texto_base = input("Ingrese la base del triángulo: ")
    if not es_numero_valido(texto_base):
        raise ValueError("La base debe ser un número positivo (solo dígitos).")
    base = float(texto_base)

    texto_altura = input("Ingrese la altura del triángulo: ")
    if not es_numero_valido(texto_altura):
        raise ValueError("La altura debe ser un número positivo (solo dígitos y un punto decimal).")
    altura = float(texto_altura)

    print("El área del triángulo es:", area_triangulo(base, altura))

except ValueError as e:
    print("Error:", e)
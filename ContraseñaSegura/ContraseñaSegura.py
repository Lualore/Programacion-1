import string


def tiene_longitud_minima(cadena, minimo=5):
    """
    Verifica que la cadena tenga una longitud mínima.

    Descripción detallada:
        Compara len(cadena) contra el mínimo requerido. La validación
        de tipos se hace una sola vez en es_contrasena_segura().

    Parámetros:
        cadena (str): texto a evaluar.
        minimo (int): longitud mínima requerida (por defecto 5).

    Valor de retorno:
        bool: True si len(cadena) >= minimo, False en caso contrario.

    Excepciones:
        Ninguna (los argumentos ya fueron validados por quien la llama).

    Ejemplos:
        >>> tiene_longitud_minima("Hola#1")
        True
        >>> tiene_longitud_minima("Ho#1")
        False
    """
    return len(cadena) >= minimo


def tiene_mayuscula(cadena):
    """
    Verifica que la cadena contenga al menos una letra mayúscula.

    Parámetros:
        cadena (str): texto a evaluar.

    Valor de retorno:
        bool: True si hay al menos una mayúscula, False en caso contrario.

    Excepciones:
        Ninguna (los argumentos ya fueron validados por quien la llama).

    Ejemplos:
        >>> tiene_mayuscula("hOla")
        True
        >>> tiene_mayuscula("hola")
        False
    """
    return any(c.isupper() for c in cadena)


def tiene_minuscula(cadena):
    """
    Verifica que la cadena contenga al menos una letra minúscula.

    Parámetros:
        cadena (str): texto a evaluar.

    Valor de retorno:
        bool: True si hay al menos una minúscula, False en caso contrario.

    Excepciones:
        Ninguna (los argumentos ya fueron validados por quien la llama).

    Ejemplos:
        >>> tiene_minuscula("HOLa")
        True
        >>> tiene_minuscula("HOLA")
        False
    """
    return any(c.islower() for c in cadena)


def tiene_digito(cadena):
    """
    Verifica que la cadena contenga al menos un dígito numérico.

    Parámetros:
        cadena (str): texto a evaluar.

    Valor de retorno:
        bool: True si hay al menos un dígito, False en caso contrario.

    Excepciones:
        Ninguna (los argumentos ya fueron validados por quien la llama).

    Ejemplos:
        >>> tiene_digito("Hola1")
        True
        >>> tiene_digito("Hola")
        False
    """
    return any(c.isdigit() for c in cadena)


def tiene_caracter_especial(cadena):
    """
    Verifica que la cadena contenga al menos un carácter especial.

    Descripción detallada:
        Se considera especial cualquier carácter incluido en
        string.punctuation (!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~).

    Parámetros:
        cadena (str): texto a evaluar.

    Valor de retorno:
        bool: True si hay al menos un carácter especial, False en caso contrario.

    Excepciones:
        Ninguna (los argumentos ya fueron validados por quien la llama).

    Ejemplos:
        >>> tiene_caracter_especial("Hola#")
        True
        >>> tiene_caracter_especial("Hola1")
        False
    """
    return any(c in string.punctuation for c in cadena)


def es_contrasena_segura(cadena, minimo=5):
    """
    Determina si una cadena es una contraseña segura.

    Descripción detallada:
        Una contraseña es segura si tiene la longitud mínima y contiene
        al menos una mayúscula, una minúscula, un dígito y un carácter
        especial. Primero valida los argumentos y lanza excepciones si
        son incorrectos; después evalúa los criterios.

    Parámetros:
        cadena (str): contraseña a evaluar.
        minimo (int): longitud mínima requerida (por defecto 5, debe ser >= 1).

    Valor de retorno:
        bool: True si cumple todos los criterios, False en caso contrario.

    Excepciones:
        TypeError: si 'cadena' no es str o 'minimo' no es int.
        ValueError: si 'minimo' es menor que 1.

    Ejemplos:
        >>> es_contrasena_segura("Hola#1")
        True
        >>> es_contrasena_segura(12345)
        Traceback (most recent call last):
            ...
        TypeError: La contraseña debe ser una cadena (str).
    """
    if not isinstance(cadena, str):
        raise TypeError("La contraseña debe ser una cadena (str).")
    if not isinstance(minimo, int):
        raise TypeError("La longitud mínima debe ser un entero (int).")
    if minimo < 5:
        raise ValueError("La longitud mínima debe ser al menos 5.")
    if cadena == "":
        raise ValueError("La contraseña no puede estar vacía.")

    return (
        tiene_longitud_minima(cadena, minimo)
        and tiene_mayuscula(cadena)
        and tiene_minuscula(cadena)
        and tiene_digito(cadena)
        and tiene_caracter_especial(cadena)
    )


# Programa principal
if __name__ == "__main__":
    contrasena = input("Ingresa una contraseña: ")

    try:
        resultado = es_contrasena_segura(contrasena)
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
    else:
        if resultado:
            print("True -> La contraseña es segura.")
        else:
            print("False -> La contraseña NO es segura.")
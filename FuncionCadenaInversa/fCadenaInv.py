def invertir_cadena(cadena):
    """
    Descripción breve: Invierte el orden de los caracteres de una cadena.

    Descripción detallada (Opcional):
    Devuelve una nueva cadena con los caracteres colocados
    en orden inverso.

    Parámetros:
        cadena (str): Cadena de caracteres que se desea invertir.

    Valor de retorno:
        str: Cadena original escrita en orden inverso.

    Excepciones:
        TypeError: Si el valor recibido no es una cadena.

    Ejemplos (opcional):
        invertir_cadena("Hola") -> "aloH"
        invertir_cadena(123) -> Error
    """
    if not isinstance(cadena, str):
        raise TypeError("El valor debe ser una cadena.")

    cadena_invertida = cadena[::-1]
    return cadena_invertida

cadena = input("Ingrese una cadena de caracteres: ")

print("La cadena invertida es:", invertir_cadena(cadena))
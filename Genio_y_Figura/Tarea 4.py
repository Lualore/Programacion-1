# Nombre:¡Genio y figura...!
# Descripcion: Imprime figuras de asteriscos (reloj de arena, rombo, moño y
# copa) de tamaño impar entre 5 y 21, rellenas o huecas. Tiene un menu para
# elegir una figura o todas.
# Autores: Luis Alexandro Lopez Reyes y Luis Fernando Gálvez Huez
# Fecha: 31/10/2026


def validar_dimension(n):
    """
    Revisa que la dimension sea impar y este entre 5 y 21.

    Parametros:
        n (int): la dimension de la figura.

    Valor de retorno:
        None: no regresa nada, solo manda error si n no sirve.

    Excepciones:
        ValueError: si n esta fuera de 5 a 21 o si es par.

    Ejemplos:
        validar_dimension(7) no pasa nada porque esta bien.
        validar_dimension(8) manda ValueError: La dimension debe ser impar.
    """
    if n < 5 or n > 21:
        raise ValueError("La dimension debe estar entre 5 y 21.")
    if n % 2 == 0:
        raise ValueError("La dimension debe ser impar.")


def validar_tipo(tipo):
    """
    Revisa que el tipo sea 1 (rellena) o 2 (hueca).

    Parametros:
        tipo (int): el tipo de figura.

    Valor de retorno:
        None: no regresa nada, solo manda error si tipo no sirve.

    Excepciones:
        ValueError: si tipo no es 1 ni 2.

    Ejemplos:
        validar_tipo(2) no pasa nada.
        validar_tipo(3) manda ValueError: El tipo debe ser 1 o 2.
    """
    if tipo != 1 and tipo != 2:
        raise ValueError("El tipo debe ser 1 o 2.")


def fila(simbolo, espacios, ancho, tipo):
    """
    Arma una fila de una figura.

    Descripcion detallada:
        Sirve para el reloj de arena, el rombo y la copa. Primero van
        los espacios de la izquierda y despues los simbolos. Si la figura
        es hueca solo se ponen los dos de las orillas, pero si el ancho
        es 1 se pone uno solo (si no salian dos juntos).

    Parametros:
        simbolo (str): el caracter con el que se dibuja.
        espacios (int): cuantos espacios van a la izquierda.
        ancho (int): cuantos simbolos de ancho tiene la fila.
        tipo (int): 1 rellena, 2 hueca.

    Valor de retorno:
        str: la fila ya armada para imprimirla.

    Excepciones:
        Ninguna.

    Ejemplos:
        fila("*", 1, 5, 2) regresa " *   *"
        fila("*", 2, 1, 2) regresa "  *"
    """
    if tipo == 1 or ancho == 1:
        return " " * espacios + simbolo * ancho
    return " " * espacios + simbolo + " " * (ancho - 2) + simbolo


def reloj_arena(simbolo, n, tipo):
    """
    Imprime un reloj de arena relleno o hueco.

    Descripcion detallada:
        La primera y la ultima fila se imprimen aparte porque siempre
        van completas (si no el reloj hueco quedaba abierto). Entre
        ellas, un ciclo baja hasta el centro y otro sube de regreso.

    Parametros:
        simbolo (str): el caracter con el que se dibuja.
        n (int): el ancho y el alto de la figura (impar de 5 a 21).
        tipo (int): 1 rellena, 2 hueca.

    Valor de retorno:
        None: solo imprime la figura.

    Excepciones:
        ValueError: si n o tipo no son validos.

    Ejemplos:
        reloj_arena("*", 5, 1) imprime:
        *****
         ***
          *
         ***
        *****

        reloj_arena("*", 4, 1) manda ValueError: La dimension debe ser impar.
    """
    validar_dimension(n)
    validar_tipo(tipo)
    mitad = n // 2

    print(simbolo * n)  # primera fila

    # Hasta el centro
    for i in range(1, mitad + 1):
        print(fila(simbolo, i, n - 2 * i, tipo))

    # Del centro hacia abajo (al reves, sin repetir el centro)
    for i in range(mitad - 1, 0, -1):
        print(fila(simbolo, i, n - 2 * i, tipo))

    print(simbolo * n)  # ultima fila


def rombo(simbolo, n, tipo):
    """
    Imprime un rombo relleno o hueco.

    Parametros:
        simbolo (str): el caracter con el que se dibuja.
        n (int): el ancho y el alto de la figura (impar de 5 a 21).
        tipo (int): 1 rellena, 2 hueca.

    Valor de retorno:
        None: solo imprime la figura.

    Excepciones:
        ValueError: si n o tipo no son validos.

    Ejemplos:
        rombo("*", 5, 2) imprime:
          *
         * *
        *   *
         * *
          *

        rombo("*", 25, 2) manda ValueError: La dimension debe estar entre 5 y 21.
    """
    validar_dimension(n)
    validar_tipo(tipo)
    mitad = n // 2

    # De la punta de arriba hasta el centro
    for i in range(mitad + 1):
        print(fila(simbolo, mitad - i, 1 + 2 * i, tipo))

    # Del centro hacia la punta de abajo
    for i in range(mitad - 1, -1, -1):
        print(fila(simbolo, mitad - i, 1 + 2 * i, tipo))


def mono(simbolo, n, tipo):
    """
    Imprime un moño relleno o hueco.

    Descripcion detallada:
        Aqui no use fila() porque con espacios y ancho salia un reloj de
        arena. Mejor armo cada fila columna por columna, y en cada una
        decido si va un simbolo o un espacio. A la funcion le puse mono
        sin ñ para evitar problemas.

    Parametros:
        simbolo (str): el caracter con el que se dibuja.
        n (int): el ancho y el alto de la figura (impar de 5 a 21).
        tipo (int): 1 rellena, 2 hueca.

    Valor de retorno:
        None: solo imprime la figura.

    Excepciones:
        ValueError: si n o tipo no son validos.

    Ejemplos:
        mono("*", 5, 2) imprime:
        *   *
        ** **
        * * *
        ** **
        *   *

        mono("*", 7, 3) manda ValueError: El tipo debe ser 1 o 2.
    """
    validar_dimension(n)
    validar_tipo(tipo)

    for i in range(n):
        # nivel es 0 en la primera y ultima fila y va subiendo hasta el centro
        nivel = min(i, n - 1 - i)

        linea = ""
        for columna in range(n):
            if tipo == 1:
                # Relleno: se llenan las orillas hasta llegar al nivel
                poner = columna <= nivel or columna >= n - 1 - nivel
            else:
                # Hueco: solo las orillas y las diagonales
                poner = (columna == 0 or columna == n - 1
                         or columna == nivel or columna == n - 1 - nivel)

            if poner:
                linea = linea + simbolo
            else:
                linea = linea + " "

        print(linea)


def copa(simbolo, n, tipo):
    """
    Imprime una copa rellena o hueca.

    Descripcion detallada:
        Tiene tres partes: el vaso (que se va haciendo angosto hasta un
        solo simbolo), el tallo y la base. El tallo crece con n y como
        minimo tiene 2 filas. La tapa y la base siempre van completas.
        Ojo: esta figura no mide n de alto como las demas.

    Parametros:
        simbolo (str): el caracter con el que se dibuja.
        n (int): el ancho de la copa (impar de 5 a 21).
        tipo (int): 1 rellena, 2 hueca.

    Valor de retorno:
        None: solo imprime la figura.

    Excepciones:
        ValueError: si n o tipo no son validos.

    Ejemplos:
        copa("*", 7, 2) imprime:
        *******
         *   *
          * *
           *
           *
           *
        *******

        copa("*", 7, 5) manda ValueError: El tipo debe ser 1 o 2.
    """
    validar_dimension(n)
    validar_tipo(tipo)
    mitad = n // 2

    print(simbolo * n)  # la tapa

    # El resto del vaso
    for i in range(1, mitad + 1):
        print(fila(simbolo, i, n - 2 * i, tipo))

    # El tallo (minimo 2 filas)
    alto_tallo = max(2, n // 3)
    for i in range(alto_tallo):
        print(" " * mitad + simbolo)

    print(simbolo * n)  # la base


def pedir_dimension():
    """
    Le pide al usuario la dimension de la figura.

    Descripcion detallada:
        Vuelve a preguntar hasta que el usuario escriba algo valido.
        Primero revisa que haya escrito un numero y despues que ese
        numero sirva con validar_dimension.

    Parametros:
        Ninguno.

    Valor de retorno:
        int: la dimension ya validada.

    Excepciones:
        Ninguna, los errores se atrapan aqui mismo y se vuelve a preguntar.

    Ejemplos:
        Si el usuario escribe 7, regresa 7.
        Si escribe "abc" muestra "Error: ingrese un numero entero." y
        vuelve a preguntar.
    """
    while True:
        try:
            n = int(input("Ingrese la dimension (impar, de 5 a 21): "))
        except ValueError:
            print("Error: ingrese un numero entero.")
            continue

        try:
            validar_dimension(n)
            return n
        except ValueError as error:
            print("Error:", error)


def pedir_tipo():
    """
    Le pide al usuario si quiere la figura rellena o hueca.

    Parametros:
        Ninguno.

    Valor de retorno:
        int: 1 si es rellena o 2 si es hueca.

    Excepciones:
        Ninguna, los errores se atrapan aqui mismo y se vuelve a preguntar.

    Ejemplos:
        Si el usuario escribe 2, regresa 2.
        Si escribe 5 muestra "Error: El tipo debe ser 1 o 2." y vuelve
        a preguntar.
    """
    while True:
        print("\nTipo de figura:")
        print("1. Rellena")
        print("2. Hueca")

        try:
            tipo = int(input("Seleccione el tipo: "))
        except ValueError:
            print("Error: ingrese 1 o 2.")
            continue

        try:
            validar_tipo(tipo)
            return tipo
        except ValueError as error:
            print("Error:", error)


def imprimir_figura(numero, n, tipo):
    """
    Imprime la figura que corresponde a un numero del menu.

    Descripcion detallada:
        Es la unica parte donde hay varios if seguidos, para no
        repetirlos en main. Cada return evita seguir revisando los demas.

    Parametros:
        numero (int): 1 reloj de arena, 2 rombo, 3 moño, 4 copa.
        n (int): la dimension de la figura.
        tipo (int): 1 rellena, 2 hueca.

    Valor de retorno:
        None: solo imprime el titulo y la figura.

    Excepciones:
        ValueError: si n o tipo no son validos (lo manda la figura).

    Ejemplos:
        imprimir_figura(2, 5, 1) imprime el titulo ROMBO y un rombo
        relleno de 5.
        imprimir_figura(1, 6, 1) manda ValueError: La dimension debe ser impar.
    """
    if numero == 1:
        print("\n===== RELOJ DE ARENA =====\n")
        reloj_arena("*", n, tipo)
        return
    if numero == 2:
        print("\n===== ROMBO =====\n")
        rombo("*", n, tipo)
        return
    if numero == 3:
        print("\n===== MOÑO =====\n")
        mono("*", n, tipo)
        return
    print("\n===== COPA =====\n")
    copa("*", n, tipo)


def main():
    """
    Muestra el menu y imprime lo que el usuario elija.

    Descripcion detallada:
        La opcion 5 (todas) se resuelve con un ciclo que va de la figura
        1 a la 4. Si se elige una sola, el ciclo va de ese numero a ese
        mismo numero, asi solo da una vuelta.

    Parametros:
        Ninguno.

    Valor de retorno:
        None: termina cuando el usuario elige salir.

    Excepciones:
        Ninguna, si la opcion no es valida se muestra un error y se
        vuelve a mostrar el menu.

    Ejemplos:
        Si el usuario escribe 6 imprime "Programa terminado." y se cierra.
        Si escribe 9 imprime "Error: elija una opcion del 1 al 6." y
        vuelve al menu.
    """
    while True:
        print("\n========== MENU ==========")
        print("1. Reloj de arena")
        print("2. Rombo")
        print("3. Moño")
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

        if opcion < 1 or opcion > 5:
            print("Error: elija una opcion del 1 al 6.")
            continue

        n = pedir_dimension()
        tipo = pedir_tipo()

        # Con la opcion 5 se recorren las 4 figuras, con las demas solo una
        primera = opcion
        ultima = opcion
        if opcion == 5:
            primera = 1
            ultima = 4

        for numero in range(primera, ultima + 1):
            imprimir_figura(numero, n, tipo)

        input("\nPresione ENTER para continuar...")


main()

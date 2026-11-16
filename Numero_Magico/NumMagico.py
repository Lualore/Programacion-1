
import random
import os

# Nombre: Número mágico 3
# Autor: Luis Alexandro López Reyes
# Fecha: 17/09/2026

cont = 0
respuesta = ""

print("Este algoritmo simulará el número mágico.")
print("Tendrás que adivinar un número escogido al azar,")
print("el cual será revelado al final. Tienes 4 intentos.")

while respuesta != "n":

    # Limpiar pantalla
    os.system("cls" if os.name == "nt" else "clear")

    print("¿Quieres jugar? S/N")
    respuesta = input().lower()

    if respuesta == "s":

        # Reiniciar valores para cada partida
        cont += 1
        LimI = 0
        LimS = 100
        intentos = 5

        # Elegir número mágico
        NumM = random.randint(0, 100)

        print("Inserte el número mágico:")
        adiv = int(input())

        # Validar el primer número
        while adiv < LimI or adiv > LimS:
            print("Límite, no se permiten números menores que",LimI,"o mayores que",LimS)
            adiv = int(input())

        # Juego
        while intentos > 0:

            # ¿Acertó?
            if adiv == NumM:
                print("¡Felicidades! Has adivinado el número mágico #", NumM)
                break

            # Gastar un intento
            intentos -= 1

            # El número mágico es mayor
            if NumM > adiv:
                print(
                    "Fallo, el número mágico es mayor, intentos restantes:",intentos)
                LimI = adiv

                # Si todavía quedan intentos, pedir otro número
                if intentos > 0:
                    print("Inserte el número mágico:")
                    adiv = int(input())

                    while adiv < LimI or adiv > LimS:
                        print("Límite, no se permiten números menores que",LimI,"o mayores que",LimS)
                        adiv = int(input())

            # El número mágico es menor
            elif NumM < adiv:
                print("Fallo, el número mágico es menor, intentos restantes:", intentos)
                LimS = adiv

                # Si todavía quedan intentos, pedir otro número
                if intentos > 0:
                    print("Inserte el número mágico:")
                    adiv = int(input())

                    while adiv < LimI or adiv > LimS:
                        print( "Límite, no se permiten números menores que",LimI,"o mayores que", LimS)
                        adiv = int(input())

        # Se acabaron los intentos
        if adiv != NumM:
            print("Te has quedado sin intentos.")
            print("El número mágico era:", NumM)

print("Fin del juego, has jugado:", cont, "partidas")
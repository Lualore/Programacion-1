import random

# 4-tupla de palos de la baraja inglesa
palos = ('♥', '♦', '♣', '♠')

# 13-tupla de denominaciones de la baraja inglesa
denominaciones = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

# Lista de 52 cartas: cada una es una 2-tupla (denominación, palo)
baraja = [(d, p) for p in palos for d in denominaciones]

# Imprimir la baraja completa
print("Baraja completa:")
print(baraja)

# Barajar
random.shuffle(baraja)

# Imprimir la baraja de nuevo
print("\nBaraja barajada:")
print(baraja)
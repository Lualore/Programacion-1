# Quitar los números repetidos de una lista

n = int(input("¿Cuántos números vas a capturar? "))

numeros = []
for i in range(n):
    numero = int(input(f"Número {i + 1}: "))
    numeros.append(numero)

# Segunda lista: solo agrego el número si todavía no está en ella
sin_repetidos = []
for numero in numeros:
    if numero not in sin_repetidos:
        sin_repetidos.append(numero)

print("\nLista original:", numeros)
print("Lista sin repeticiones:", sin_repetidos)
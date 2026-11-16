import numpy as np

def pedir_n():
    while True:
        try:
            n = int(input("Ingresa n (10 a 30): "))
            if 10 <= n <= 30:
                return n
        except ValueError:
            pass
        print("Valor inválido, intenta de nuevo.")
        
def graficar(arr):
    # Recorre los niveles de arriba (15) hacia abajo (1)
    for nivel in range(15, 0, -1):
        for valor in arr:
            if valor >= nivel:
                print("█  ", end="")
            else:
                print("   ", end="")
        print()  # salto de línea al terminar la fila

    # Números debajo de cada barra
    for valor in arr:
        print(f"{valor:<3}", end="")
    print()
# def graficar(arr):
#     niveles = np.arange(15, 0, -1)[:, None]   # columna: 15, 14, ..., 1
#     matriz = arr[None, :] >= niveles          # True donde la barra alcanza ese nivel
#     for fila in matriz:
#         print("".join("█  " if x else "   " for x in fila))
#     print("".join(f"{v:<3}" for v in arr))

def burbuja(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

n = pedir_n()
arreglo = np.random.randint(1, 16, size=n)    # el límite superior es exclusivo

print("\nArreglo original:", arreglo)
graficar(arreglo)

ordenado = arreglo.copy()
burbuja(ordenado)

print("\nArreglo ordenado:", ordenado)
graficar(ordenado)
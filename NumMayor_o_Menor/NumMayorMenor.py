
while True:
    try:
        n = int(input("¿Cuántos números vas a ingresar? "))
        if n > 0:
            break
        else:
            print("Error, debes ingresar una cantidad mayor que cero.")
    except ValueError:
        print("Error, debes ingresar un número entero.")

while True:
    try:
        numero = float(input("Ingresa el número 1: "))
        break
    except ValueError:
        print("Error, no están permitidas las letras.")

minimo = numero
maximo = numero

for i in range(2, n + 1):
    while True:
        try:
            numero = float(input("Ingresa el número " + str(i) + ": "))
            break
        except ValueError:
            print("Error, no están permitidas las letras.")

    if numero < minimo:
        minimo = numero

    if numero > maximo:
        maximo = numero

print("El número mínimo es:", minimo)
print("El número máximo es:", maximo)

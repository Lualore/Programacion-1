
cadena = input("Ingrese una cadena: ")

for letra in cadena:
    if letra.lower() in "aeiou":
        print("La primera vocal es:", letra)
        break
else:
    print("No se encontraron vocales")
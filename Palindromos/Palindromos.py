cadena = input("Ingresa una cadena: ")

palindromo = True

for i in range(len(cadena)):
    if cadena[i] != cadena[len(cadena) - 1 - i]:
        palindromo = False

if palindromo:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
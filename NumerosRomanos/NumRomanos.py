
numero = int(input("Introduce un número entero (1-3999): "))

if numero < 1 or numero >= 4000:
    print("Número no válido")
else:
    romanos = ""

    valores = [1000, 900, 500, 400, 100, 90, 50, 40,
               10, 9, 5, 4, 1]

    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L",
                "XL", "X", "IX", "V", "IV", "I"]

    for i in range(len(valores)):
        while numero >= valores[i]:
            romanos = romanos + simbolos[i]
            numero = numero - valores[i]

    print("Número romano:", romanos)

# millares = num // 1000
# centenas = num % 1000 // 100
# decenas = num % 100 // 10
# unidades = num % 10
# 
# numRomano = " "
# match millares:
#     case 1:
#         numRomano = numRomano + "M"
#     case 2:
#         numRomano = numRomano + "MM"
#     case 2:
#         numRomano = numRomano + "MMM"
import math
num = int(input("Deme un número entero mayor que 1: "))
while num <=1:
    num = int(input("Dame un número entero mayor que : "))


raiz = math.sqrt(num)
divisor = 2
while divisor <= raiz:
    if num % divisor == 0:
        break
    divisor +=1

# if divisor > raiz:
#     print("Es primo")
# else:
#     print("Es compuesto")

print("Es primo" if divisor > raiz else "Es compuesto")


















# while num <=1:
#     num = int(input("Dame un número entero mayor que : "))
# 
# esPrimo = True
# raiz = math.sqrt(num)
# divisor = 2
# while divisor <= raiz and esPrimo:
#     if num % divisor == 0:
#         esPrimo = False
#     divisor +=1
# 
# if esPrimo
#     print("Es primo")
# else:
#     print("Es compuesto")
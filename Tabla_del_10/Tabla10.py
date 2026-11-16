
# Programa para mostrar la tabla de multiplicar de un número

n = int(input("Ingrese un número entero: "))
while n<1 or n>10:
    print("Error, ingrese un número entre el 1 y 10")
    n = int(input("Ingrese un número entero: "))

n1,n2,n3,n4,n5,n6,n7,n8,n9,n10=1,2,3,4,5,6,7,8,9,10
print(n*n1,n*n2,n*n3,n*n4,n*n5,n*n6,n*n7,n*n8,n*n9,n*n10)

#Fecha:15/10/26
n = int(input("Ingrese la cantidad de calificaciones: "))

suma = 0

for i in range(n):
    calificacion = float(input("Ingrese la calificación: "))

    if calificacion < 0 or calificacion > 100:
        print("Error, elige un número del 0 al 100")
    else:
        suma = suma + calificacion

promedio = suma / n

print("El promedio es:", promedio)

#i=1
#while i <= n:
#     calificacion= float(input(f"calificación {i}: "))
#     while calificacion <0 or calif >100.0:
#         calificacion= float(input(calificación {i}))
        
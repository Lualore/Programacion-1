# Ejercicio 3: calificaciones y nombres en listas separadas

n = int(input("¿Cuántos estudiantes son? "))

nombres = []
calificaciones = []
for i in range(n):
    nombres.append(input(f"Nombre del estudiante {i + 1}: "))
    calificaciones.append(float(input(f"Calificación del estudiante {i + 1}: ")))

promedio = sum(calificaciones) / n
print(f"\nPromedio grupal: {promedio:.2f}")

print("Estudiantes con calificación superior al promedio:")
for i in range(n):
    if calificaciones[i] > promedio:
        print(f"  #{i + 1} {nombres[i]}: {calificaciones[i]}")








# # Ejercicio 3: igual que el 2, pero con los nombres en otra lista
# 
# n = int(input("¿Cuántos estudiantes son? "))
# 
# nombres = []
# calificaciones = []
# for i in range(n):
#     nombre = input(f"Nombre del estudiante {i + 1}: ")
#     cal = float(input(f"Calificación de {nombre}: "))
#     nombres.append(nombre)
#     calificaciones.append(cal)
# 
# promedio = sum(calificaciones) / n
# print(f"\nPromedio grupal: {promedio:.2f}")
# 
# # Las dos listas van "en paralelo": la posición i de una corresponde a la posición i de la otra
# print("Estudiantes con calificación superior al promedio:")
# hay_alguno = False
# for i in range(n):
#     if calificaciones[i] > promedio:
#         print(f"  #{i + 1} {nombres[i]}: {calificaciones[i]}")
#         hay_alguno = True
# 
# if not hay_alguno:
#     print("  Ninguno superó el promedio.")
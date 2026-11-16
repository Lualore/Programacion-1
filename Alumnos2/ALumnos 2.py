# Ejercicio 4: lista de elementos [nombre, calificación]

n = int(input("¿Cuántos estudiantes son? "))

alumnos = []
for i in range(n):
    nombre = input(f"Nombre del estudiante {i + 1}: ")
    cal = float(input(f"Calificación del estudiante {i + 1}: "))
    alumnos.append([nombre, cal])

suma = 0
for alumno in alumnos:
    suma += alumno[1]
promedio = suma / n
print(f"\nPromedio grupal: {promedio:.2f}")

print("Estudiantes con calificación superior al promedio:")
for i in range(n):
    if alumnos[i][1] > promedio:
        print(f"  #{i + 1} {alumnos[i][0]}: {alumnos[i][1]}")





# # Ejercicio 4: igual que el 2, pero cada elemento de la lista es [nombre, calificación]
# 
# n = int(input("¿Cuántos estudiantes son? "))
# 
# alumnos = []
# for i in range(n):
#     nombre = input(f"Nombre del estudiante {i + 1}: ")
#     cal = float(input(f"Calificación de {nombre}: "))
#     alumnos.append([nombre, cal])   # lista dentro de la lista
# 
# # alumno[1] es la calificación (alumno[0] es el nombre)
# suma = 0
# for alumno in alumnos:
#     suma += alumno[1]
# promedio = suma / n
# print(f"\nPromedio grupal: {promedio:.2f}")
# 
# print("Estudiantes con calificación superior al promedio:")
# hay_alguno = False
# for i in range(n):
#     if alumnos[i][1] > promedio:
#         print(f"  #{i + 1} {alumnos[i][0]}: {alumnos[i][1]}")
#         hay_alguno = True
# 
# if not hay_alguno:
#     print("  Ninguno superó el promedio.")
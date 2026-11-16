# 2.Promedio grupal y alumnos arriba del promedio

n = int(input("¿Cuántos estudiantes son? "))

calificaciones = []
for i in range(n):
    cal = float(input(f"Calificación del estudiante {i + 1}: "))
    calificaciones.append(cal)

# Promedio = suma de todas / cantidad de alumnos
promedio = sum(calificaciones) / n
print(f"\nPromedio grupal: {promedio:.2f}")

# Recorro la lista con índice; el estudiante número es el índice + 1
print("Estudiantes con calificación superior al promedio:")
hay_alguno = False
for i in range(n):
    if calificaciones[i] > promedio:
        print(f"  Estudiante {i + 1}: {calificaciones[i]}")
        hay_alguno = True

if not hay_alguno:
    print("  Ninguno superó el promedio.")
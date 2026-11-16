
# Programa para convertir una fecha de nacimiento a una cadena de 6 caracteres

año = int(input("Ingresa el año: "))
mes = int(input("Ingresa el mes: "))
día = int(input("Ingresa el día: "))

# Validar el año
while año < 1900 or año > 2026:
    print("Error: el año debe estar entre 1900 y 2026.")
    año = int(input("Ingresa el año: "))

# Validar el mes
while mes < 1 or mes > 12:
    print("Error: el mes debe estar entre 1 y 12.")
    mes = int(input("Ingresa el mes: "))

# Determinar la cantidad de días del mes
if mes == 2:
    # Un año es bisiesto si es divisible entre 4,
    # excepto los divisibles entre 100 que no sean divisibles entre 400.
    if (año % 400 == 0) or (año % 4 == 0 and año % 100 != 0):
        días_del_mes = 29
    else:
        días_del_mes = 28

elif mes in [4, 6, 9, 11]:
    días_del_mes = 30

else:
    días_del_mes = 31

# Validar el día
while día < 1 or día > días_del_mes:
    print(f"Error: el día debe estar entre 1 y {días_del_mes}.")
    día = int(input("Ingresa el día: "))

# Obtener los dos últimos dígitos del año
año_2 = año % 100

# Crear la cadena de 6 caracteres
fecha = f"{año_2:02d}{mes:02d}{día:02d}"

print("Fecha:", fecha)
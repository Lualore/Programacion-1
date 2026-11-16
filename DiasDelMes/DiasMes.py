
año = int(input("Introduce un año mayor que 1582: "))
mes = int(input("Introduce un mes (1-12): "))

if año <= 1582 or mes < 1 or mes > 12:
    print("Datos no válidos")
else:
    if mes == 2:
        if año % 400 == 0 or (año % 4 == 0 and año % 100 != 0):
            dias = 29
        else:
            dias = 28
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias = 30
    else:
        dias = 31

    print("El mes tiene", dias, "días")
1
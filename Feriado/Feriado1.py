import sys
precio = int(input("Precio del articulo: "))
if precio>0:
    importe = int(input("Ingrese el importe de la compra: "))
    if importe >= precio:
        cambio = int(importe-precio)

        Bill500 = cambio//500
        cambio %= 500
        bill200 = cambio//200
        cambio %= 200
        bill100 = cambio//100
        cambio %= 100
        bill50 = cambio//50
        cambio %= 50
        bill20 = cambio//20
        cambio %= 20
        mon10 = cambio//10
        cambio %= 10
        mon5 = cambio//5
        cambio %= 5
        mon2 = cambio//2
        cambio %= 2
        mon1 = cambio//1
        cambio %= 1
        print(f"Tienes {Bill500} billetes de 500, {bill200} billetes de 200, {bill100} billetes de 100, {bill50} billetes de 50, {bill20} billetes de 20 pesos y {mon10} monedas de 10, {mon5} monedas de 5, {mon2} monedas de 2 y {mon1} monedas de 1 peso de feria.")

    else:
        print("Error, el importe es menor al precio del producto.", file=sys.stderr)
else:
    print("Error, el precio es incorrecto.", file=sys.stderr)
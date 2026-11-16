import math
import sys
radio = float(input("Ingrese el radio de la esfera: "))

if radio >= 0:
    volumen = (4/3) * math.pi * radio**3
    print(f"El volumen de la esfera es: {volumen}")
else:
    print("Error: el radio no puede ser negativo.", file=sys.stderr)
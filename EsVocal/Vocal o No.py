
import sys
caracter = input("Introduce un carácter: ")
if len(caracter) == 1:
    match caracter.lower():
        case "a"|"e"|"i"|"o"|"u"|"á"|"é"|"í"|"ó"|"ú":
            print("Es una vocal")
        case _:
            print("No es una vocal")
else:
    print("error:no es un caracter", file= sys.stderr)



def grupo_Asignado(nombre, género):
    if (género == "M" and nombre.lower() < 'm') or (género == "H" and nombre.lower() > 'n'):
        print("Perteneces al grupo A. ")
    else:
        print("Perteneces al grupo B. ")

if __name__ == "__main__":
    nombre = input("Introduzca su nombre: ")
    género = str(input("Introduzca su género con las letras mayúsculas (H/M): "))

    grupo_Asignado(nombre, género)
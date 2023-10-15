


def calcular_precio(edad):
    if (edad < 4):
        precio = 0
    else:
        if (edad >= 4 and edad <= 18):
            precio = 5
        else:
            precio = 10
    return precio

if __name__ == "__main__":
    edad = int(input("Introduzca su edad: "))

    calcular_precio(edad)
    
    print("El precio de su entrada equivale a " + str(calcular_precio(edad)) + " euros. ")
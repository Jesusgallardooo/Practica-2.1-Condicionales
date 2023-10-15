


def tributar_O_No(edad, ingresosMes):
    if(edad >= 16 and ingresosMes >= 1000):
        print("Usted debe tributar. ")
    else:
        print("Usted no tiene que tributar. ")

if __name__ == "__main__":
    edad = int(input("Introduzca su edad: "))
    ingresosMes = float(input("Introduzca sus ingresos mensuales: "))

    tributar_O_No(edad, ingresosMes)
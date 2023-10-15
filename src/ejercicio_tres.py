

def resultado_division(divisor, division):
    if (divisor == 0):
        print("ERROR, no puedes dividir entre 0.")
    else:
        print("El resultado de su division es: " + str(division))

if __name__ == "__main__":
    dividendo = int (input("Introduzca el numero que quiera dividir: "))
    divisor = int (input("Introduzca entre qué numero quiere dividir: "))

    division = dividendo / divisor

    resultado_division(divisor, division)
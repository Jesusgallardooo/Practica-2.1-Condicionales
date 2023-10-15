


def numero_Par_Impar(numero):
    if(numero %2  == 0):
        print("El número que has introducido es par. ")
    else:
        print("El número que has introducido es impar. ")

if __name__ == "__main__":
    
    numero = int(input("Introduzca un número entero:"))

    numero_Par_Impar(numero)

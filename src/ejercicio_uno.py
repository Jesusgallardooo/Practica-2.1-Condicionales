
def calcular_Mayoría_Edad(edad):
    if (edad <= 17):
        print(" Aún eres menor de edad. ")
    else:
        print(" Ya eres mayor de edad. ")


if __name__ == "__main__":
    
    edad = int(input("Introduzca su edad: "))

    if(edad < 0):
        print("Dato incorrecto, fin del programa. ")
    else:
        calcular_Mayoría_Edad(edad)
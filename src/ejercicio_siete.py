


def calcular_Tipo_Impositivo(rentaAnual):
    if (rentaAnual < 10000):
        print ("Le corresponde un tipo impositivo del 5% ")
        tipoImpositivo = rentaAnual * 0.05
    else:
        if (rentaAnual < 20000 ):
            print ("Le corresponde un tipo impositivo del 15% ")
            tipoImpositivo = rentaAnual * 0.15
        else:
            if (rentaAnual < 35000):
                print ("Le corresponde un tipo impositivo del 20% ")
                tipoImpositivo = rentaAnual * 0.2
            else:
                if(rentaAnual < 60000):
                    print ("Le corresponde un tipo impositivo del 30% ")
                    tipoImpositivo = rentaAnual * 0.3
                else:
                    print ("Le corresponde un tipo impositivo del 45% ")
                    tipoImpositivo = rentaAnual * 0.45
    return tipoImpositivo

if __name__ == "__main__":
    rentaAnual = float(input("Introduzca su renta anual: "))

    tipoImpositivo = calcular_Tipo_Impositivo(rentaAnual)
    
    print("Su tipo impositivo equivale a " + str(tipoImpositivo) + " euros. ")
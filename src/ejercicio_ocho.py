


def calcular_recompensa(puntuación):
    if((puntuación > 0.0 and puntuación < 0.4 ) or (puntuación > 0.4 and puntuación < 0.6)):
                print("Dato incorrecto, Fin del programa. ")
    else:
        if(puntuación == 0.0 ):
            print("Tu rendimiento en la empresa durante este año ha sido inaceptable. ")
            recompensa = puntuación * 2400
        else: 
            if(puntuación == 0.4 ):
                print("Tu rendimiento en la empresa durante este año ha sido aceptable. ")
                recompensa = puntuación * 2400
            else:
                print("Tu rendimiento en la empresa durante este año ha sido meritorio. ")
                recompensa = puntuación * 2400
        print("La cantidad de dinero que recibirá como recompensa equivale a " + str(recompensa) + " euros. ")

if __name__ == "__main__":
    
    puntuación = float(input("Introduzca su puntuación: "))

    calcular_recompensa(puntuación)


def comprobar_Contraseña(contraseñaCorrecta, intento):
    if contraseñaCorrecta == intento.lower():
        print("Acceso permitido,  contraseña correcta.")
    else:
        print("Acceso denegado, contraseña incorrecta. ")


if __name__ == "__main__":
    contraseñaCorrecta = "contraseña"
    intento = input("Introduce la contraseña: ")

    comprobar_Contraseña(contraseñaCorrecta, intento)

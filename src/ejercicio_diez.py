


if __name__ == "__main__":
    print("MENÚ \nPizzas disponibles (con base de tomate y mozzarella): \n\n\t    1 --> Vegetariana   \n\t    2 --> No vegetariana\n")
    tipo = input("Introduce el número correspondiente al tipo de pizza que quieres:")
    

    if (tipo == "1"):
        
        print("Ingredientes de las pizzas vegetarianas  \n\n\t    1 --> Tofu \n\t    2 --> Pimiento\n")
        ingrediente = input("Introduzca el ingrediente que prefiera: ")
        print("\t Pizza vegetariana con ", end="")
        if (ingrediente == "1"):
            print("Tofu")
        else: 
            print("Pimiento")

    else:
        print("Ingredientes de pizzas normales  \n\n\t    1 --> Jamón \n\t    2 --> Salmón    \n\t    3 --> Peperoni\n")
        ingrediente = input("Introduzca el ingrediente que prefiera: ")
        print("\t Pizza con ", end="")
        
        if (ingrediente == "1"):
            print("Jamón")
        elif (ingrediente == "2"):
            print("Salmón")
        else:
            print("Peperoni")
        
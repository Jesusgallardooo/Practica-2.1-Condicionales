
# test del ejercicio 8

from src.ejercicio_ocho import calcular_recompensa

def test_Calcular_Recompensa():
    assert calcular_recompensa(0.0) == "La cantidad de dinero que recibirá como recompensa equivale a 0.0 euros. "
    assert calcular_recompensa(0.3) == "Dato incorrecto, Fin del programa. "
    assert calcular_recompensa(0.4) == "La cantidad de dinero que recibirá como recompensa equivale a 960.0 euros. "
    assert calcular_recompensa(0.5) == "Dato incorrecto, Fin del programa. "
    assert calcular_recompensa(0.6) == "La cantidad de dinero que recibirá como recompensa equivale a 1440.0 euros. "
    assert calcular_recompensa(0.8) == "La cantidad de dinero que recibirá como recompensa equivale a 1920.0 euros. "
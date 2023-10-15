

#test ejercicio_uno/práctica 2.1

from src.ejercicio_uno import calcular_Mayoría_Edad

def test_calcular_Mayoría_Edad():
    assert calcular_Mayoría_Edad(12) == "Aún eres menor de edad. "
    assert calcular_Mayoría_Edad(19) == "Ya eres mayor de edad. "
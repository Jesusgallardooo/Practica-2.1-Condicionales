
#test del ejercicio 4

from src.ejercicio_cuatro import numero_Par_Impar

def test_Numero_Par_Impar():
    assert numero_Par_Impar(1727372363723527236237270) == "El número que has introducido es par. "
    assert numero_Par_Impar(1425341534162713) == "El número que has introducido es impar. "
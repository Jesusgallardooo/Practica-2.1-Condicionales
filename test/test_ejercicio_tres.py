

#test ejercicio_tres/práctica 2.1

from src.ejercicio_tres import resultado_division

def test_Resultado_Division():
    assert resultado_division(3,3) == 1.0
    assert resultado_division(15,3) == 5.0


# test del ejercicio 9

from src.ejercicio_nueve import calcular_precio

def test_calcular_precio():
    assert calcular_precio(2) == 0
    assert calcular_precio(4) == 5
    assert calcular_precio(15) == 5
    assert calcular_precio(19) == 10
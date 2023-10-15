
# test del ejercicio 7

from src.ejercicio_siete import calcular_Tipo_Impositivo

def test_Calcular_Tipo_Impositivo():
    assert calcular_Tipo_Impositivo(5000) == 250.0
    assert calcular_Tipo_Impositivo(15000) == 2250.0
    assert calcular_Tipo_Impositivo(25000) == 5000.0
    assert calcular_Tipo_Impositivo(40000) == 12000.0
    assert calcular_Tipo_Impositivo(100000) == 45000.0
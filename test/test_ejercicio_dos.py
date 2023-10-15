

# test del ejercicio 2

from src.ejercicio_dos import comprobar_Contraseña

def test_Comprobar_contraseña():
    assert comprobar_Contraseña("cOnTrAsEñA") == "Acceso permitido,  contraseña correcta."
    assert comprobar_Contraseña("holahola") == "Acceso denegado, contraseña incorrecta. "
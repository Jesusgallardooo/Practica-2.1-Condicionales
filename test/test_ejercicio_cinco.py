
# test ejercicio 5

from src.ejercicio_cinco import tributar_O_No

def test_tributar_O_No():
    assert tributar_O_No(14, 300) == "Usted no tiene que tributar. "
    assert tributar_O_No(16, 1000) == "Usted debe tributar. "
    assert tributar_O_No(18, 200) == "Usted no tiene que tributar. "
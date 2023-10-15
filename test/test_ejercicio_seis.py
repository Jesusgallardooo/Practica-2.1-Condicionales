

# test ejercicio 6

from src.ejercicio_seis import grupo_Asignado

def test_Grupo_Asignado():
    assert grupo_Asignado("jesus", "H") == "Perteneces al grupo B. "
    assert grupo_Asignado("Alba", "M") == "Perteneces al grupo A. "
    assert grupo_Asignado("Zara", "M") == "Perteneces al grupo B. "
    assert grupo_Asignado("oriol", "H") == "Perteneces al grupo A. "
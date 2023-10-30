from src.Ejercicio_3 import cuenta

def test_cuenta_sin_numeros_ni_espacios():
    assert cuenta("hola", "a") == 1

def test_cuenta_con_numeros():
    assert cuenta("hola123", "a") == "Error: La cadena no debe contener números ni espacios en blanco"

def test_cuenta_con_espacios():
    assert cuenta("hola mundo", "a") == "Error: La cadena no debe contener números ni espacios en blanco"

def test_letra_numerica():
    assert cuenta("hola", "1") == "Error: La letra no debe ser un número ni un espacio en blanco"

def test_letra_espacio():
    assert cuenta("hola", " ") == "Error: La letra no debe ser un número ni un espacio en blanco"
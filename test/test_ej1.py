from src.Ejercicio_1 import es_palabra, es_numero, obtener_frase, cadenaReves

def test_es_palabra():
    assert es_palabra("hola") == True
    assert es_palabra("123") == False
    assert es_palabra("hola123") == False
    assert es_palabra("") == False

def test_es_numero():
    assert es_numero("123") == True
    assert es_numero("hola") == False
    assert es_numero("123hola") == False
    assert es_numero("") == False

def test_obtener_frase(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "hola mundo")
    assert obtener_frase() == "hola mundo"

def test_cadena_reves():
    assert cadenaReves("hola", 3) == "a\nl\no\nh\n"
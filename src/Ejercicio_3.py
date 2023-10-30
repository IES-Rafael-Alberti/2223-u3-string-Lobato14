# Tienes este código:

"""
    palabra = 'banana'
    contador = 0
    for letra in palabra:
        if letra == 'a':
            contador = contador + 1
    print(contador)
    
"""

# Encapsúlalo en una función llamada cuenta, y hazla genérica de tal modo 
# que pueda aceptar una cadena y una letra como argumentos.

def cuenta(cadena, letra):
    if any(caracter.isdigit() or caracter.isspace() for caracter in cadena):
        return "Error: La cadena no debe contener números ni espacios en blanco"
    
    if letra.isdigit() or letra.isspace():
        return "Error: La letra no debe ser un número ni un espacio en blanco"
    
    contador = 0
    for caracter in cadena:
        if caracter == letra:
            contador += 1
    return contador

if __name__ == "__main__":
    # Entrada
    entrada_valida = False
    # Proceso
    while not entrada_valida:

        palabra = input("Introduce una palabra sin números ni espacios en blanco: ")
        letra = input("Introduce una letra sin ser un número ni espacio en blanco: ")
        
        resultado = cuenta(palabra, letra)
        # En caso de que devuelva un mensaje de error
        if isinstance(resultado, str):
            # Salida 1  
            print(resultado)
            volver_a_introducir = input("¿Quieres volver a intentarlo? (s/n): ")
            if volver_a_introducir.lower() != 's':
                entrada_valida = True
        else:
            # Salida 2
            print("Número de ocurrencias de '{}' en '{}': {}".format(letra, palabra, resultado))
            entrada_valida = True
# Escribe un bucle while que comience con el último carácter en la cadena
# y haga un recorrido hacia atrás hasta el primer carácter en la cadena, 
# imprimiendo cada letra en una línea independiente.

# Esta función verifica si la cadena es un número
def es_numero(cadena):
    return cadena.isdigit()

# Esta función verifica si la cadena contiene solo letras y es una sola palabra
def es_palabra(cadena):
    return cadena.isalpha() and len(cadena.split()) == 1

# Esta función solicita la entrada hasta que se ingrese una cadena sin números ni letras
def obtener_frase():
    frase = input("Escribe una frase: ")
    while es_palabra(frase) or es_numero(frase):
        print("Por favor, ingresa una frase sin números ni letras.")
        frase = input("Escribe una frase: ")
    return frase

def cadenaReves(cadena, indice):
    textoInvertido = ""
    while indice >= 0:
        letra = cadena[indice]
        textoInvertido = letra + "\n" + textoInvertido
        indice -= 1
    return textoInvertido

if __name__ == "__main__":
    # Entrada
    cadena = obtener_frase()
    indice = len(cadena) - 1 
    # Proceso
    textoInvertido = cadenaReves(cadena, indice)
    # Salida
    print("Frase invertida:")
    print(textoInvertido)
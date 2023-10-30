# Escribe un bucle while que comience con el último carácter en la cadena
# y haga un recorrido hacia atrás hasta el primer carácter en la cadena, 
# imprimiendo cada letra en una línea independiente.


def cadenaReves(cadena, indice):
    while indice >= 0:  
        letra = cadena[indice]  
        print(letra)  
        indice -= 1  


if __name__ == "__main__":
    # Entrada
    cadena = input("Escribe una frase: ")
    indice = len(cadena) - 1 
    # Proceso
    # Salida


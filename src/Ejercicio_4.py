# Hay un método de cadenas llamado count que es similar a find. Lee la documentación 
# de este método en: * Métodos en ingles * Métodos en castellano y escribe el 
# código necesario para invocar a este método y contar el número de veces que una 
# letra aparece en “banana”.

if __name__ == "__main__":
    # Entrada
    cadena = "banana"
    letra = "a"
    # Proceso
    ocurrencias = cadena.count(letra)
    # Salida
    print(f"El número de ocurrencias de '{letra}' en '{cadena}' es: {ocurrencias}")
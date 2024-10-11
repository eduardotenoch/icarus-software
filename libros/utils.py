import os

def ordenar_lista(numeros):
    """Ordena una lista de números de menor a mayor."""
    return sorted(numeros)

def contar_palabras(archivo):
    """Cuenta la cantidad de palabras en un archivo de texto."""
    try:
        with open(archivo, 'r') as f:
            texto = f.read()
            palabras = texto.split()
            return len(palabras)
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encontró.")
        return 0

numeros = [5, 3, 8, 1, 2]
lista_ordenada = ordenar_lista(numeros)
print("Lista ordenada:", lista_ordenada) 

nombre_archivo = 'texto.txt'
cantidad_palabras = contar_palabras(nombre_archivo)
print(f"La cantidad de palabras en el archivo es: {cantidad_palabras}")

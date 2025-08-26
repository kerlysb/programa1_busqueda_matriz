# programa1_busqueda_matriz.py

def buscar_valor(matriz, valor):
    """
    Buscar un valor en una matriz bidimensional y retornar la posición (fila, columna)
    si se encuentra, o None si no está en la matriz.
    """
    for i, fila in enumerate(matriz):
        for j, elem in enumerate(fila):
            if elem == valor:
                return (i, j)
    return None

def main():
    matriz = [
        [5, 8, 3],
        [6, 7, 2],
        [9, 1, 4]
    ]

    valor_a_buscar = 0

    resultado = buscar_valor(matriz, valor_a_buscar)

    if resultado:
        print(f"Valor {valor_a_buscar} encontrado en la posición fila {resultado[0]}, columna {resultado[1]}.")
    else:
        print(f"Valor {valor_a_buscar} NO encontrado en la matriz.")

if __name__ == "__main__":
    main()
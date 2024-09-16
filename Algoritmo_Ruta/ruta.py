""" 
    Materia: Desarrollo de Backend II
    Algoritmo de Ruta

    En base a una matriz, el algoritmo debera buscar la ruta con menos y mas costo para llegar 
    del punto i al punto f, donde se debera imprimir el costo de las dos rutas.
"""

# El codigo debera ser en Python, no se permite como entrega un algoritmo de Dijkstra

# Importar libreria Numpy para hacer la matriz
import numpy as np

# matriz[Y][X]
# Definir la matriz
matriz = np.array(
    [
        [-3, -3,  2,  -3,  3, -2, -2,  1,  2,  0,  2,  0,  1],
        [ 2,  3,  4,  -1, -1,  3,  2,  0, -3, -3,  2,  2,  1],
        [ 1, -3, -3,   2,  3,  1,  3,  3,  2,  1, -2, -2,  3],
        [ 0,  0,  3,   0,  3, -3, -2, -3,  0,  2,  2,  1,  1],
        [ 2, -1, -1,  -3,  3,  3,  0, -3, -1, -2,  2,  0,  1],
        [ 0,  3, -1,   1, -1, -2,  2, -2,  2, -1, -2, -3,  0],
        [ 0,  3,  2,   0,  1,  1,  2,  3, -1, -3,  0,  0, -2],
        [ 3,  3, -3,  -2,  3, -3, -1, -3,  3, -2,  2, -2, -1],
        [-2, -2,  1,   0, -1,  0,  3,  0,  0, -2,  2, -3, -1],
        [-3,  3,  0,  -1, -3,  1,  2, -3,  2, -3,  0,  2, -2],
        [-3, -3, -3,   3, -2,  0, -2, -3,  1,  0,  1, -1, -2],
        [-1,  0,  1,   2,  1,  0,  4,  0, -3,  3,  3, -2, -1],
        [ 1, -3,  1,   0,  1,  2,  3,  1, -2,  3,  3,  0,  3],
    ]
)


# Reemplazamos el tipo de dato con un numeros para que sean del mismo tipo en toda la Matriz

# Definir las Posiciones de i y f
# i -> matriz[1][2] <- Valor original 'i'
i = (1,2)

# f -> matriz[11][6] <- Valor original 'f'
f = (11,6)

def buscar_ruta(matriz, i, f, minimizar=True):
    """_summary_

    Args:
        matriz (_type_): _description_
        i (_type_): _description_
        f (_type_): _description_
        minimizar (bool, optional): _description_. Defaults to True.

    Returns:
        _type_: _description_
    """
    filas, columnas = matriz.shape
    visitados = set()
    rutas = [(i, 0, [])]

    mejor_costo = None
    mejor_ruta = None

    while rutas:
        (x, y), costo, ruta = rutas.pop(0)
        ruta = ruta + [(x, y)]
        if (x, y) == f:
            if mejor_costo is None or (minimizar and costo < mejor_costo) or (not minimizar and costo > mejor_costo):
                mejor_costo = costo
                mejor_ruta = ruta
            continue
        visitados.add((x, y))

        # Movimientos posibles: arriba, abajo, izquierda, derecha
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < columnas and (nx, ny) not in visitados:
                nuevo_costo = costo + matriz[nx, ny]
                rutas.append(((nx, ny), nuevo_costo, ruta))

        rutas.sort(key=lambda x: x[1], reverse=not minimizar)

    return mejor_costo, mejor_ruta


menor_costo, menor_ruta = buscar_ruta(matriz, i, f, minimizar=True)
mayor_costo, mayor_ruta = buscar_ruta(matriz, i, f, minimizar=False)


print(f"Menor costo: {menor_costo}, Ruta: {menor_ruta}")
print(f"Mayor costo: {mayor_costo}, Ruta: {mayor_ruta}")

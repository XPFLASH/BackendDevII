""" 
    Materia: Desarrollo de Backend II
    Algoritmo de Ruta

    En base a una matriz, el algoritmo debera buscar la ruta con menos y mas costo para llegar 
    del punto i al punto f, donde se debera imprimir el costo de las dos rutas.
"""

# El codigo debera ser en Python, no se permite como entrega un algoritmo de Dijkstra

# Importar libreria Numpy para hacer la matriz
import numpy as np

# Definición de la Matriz
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
# Nodo de Inicio y Final
i = (1,2)
f = (11,6)

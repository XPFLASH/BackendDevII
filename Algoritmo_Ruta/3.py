import numpy as np

# Definir la matriz con los valores y las posiciones especiales
matriz = np.array(
    [
        [-3, -3,  2, -3,  3, -2, -2,  1,  2,  0,  2,  0,  1],
        [ 2,  3,  4, -1, -1,  3,  2,  0, -3, -3,  2,  2,  1],
        [ 1, -3, -3,  2,  3,  1,  3,  3,  2,  1, -2, -2,  3],
        [ 0,  0,  3,  0,  3, -3, -2, -3,  0,  2,  2,  1,  1],
        [ 2, -1, -1, -3,  3,  3,  0, -3, -1, -2,  2,  0,  1],
        [ 0,  3, -1,  1, -1, -2,  2, -2,  2, -1, -2, -3,  0],
        [ 0,  3,  2,  0,  1,  1,  2,  3, -1, -3,  0,  0, -2],
        [ 3,  3, -3, -2,  3, -3, -1, -3,  3, -2,  2, -2, -1],
        [-2, -2,  1,  0, -1,  0,  3,  0,  0, -2,  2, -3, -1],
        [-3,  3,  0, -1, -3,  1,  2, -3,  2, -3,  0,  2, -2],
        [-3, -3, -3,  3, -2,  0, -2, -3,  1,  0,  1, -1, -2],
        [-1,  0,  1,  2,  1,  0,  4,  0, -3,  3,  3, -2, -1],
        [ 1, -3,  1,  0,  1,  2,  3,  1, -2,  3,  3,  0,  3],
    ]
)

# Encontrar posiciones de I y F
inicio = (1, 2)  # Posición original de "I"
fin = (11, 6)    # Posición original de "F"

# Función para buscar la ruta con el menor o mayor costo
def buscar_ruta(matriz, inicio, fin, minimizar=True):
    filas, columnas = matriz.shape
    visitados = set()
    rutas = [(inicio, 0, [])]  # (posición, costo acumulado, ruta tomada)

    mejor_costo = None
    mejor_ruta = None

    while rutas:
        (x, y), costo, ruta = rutas.pop(0)
        ruta = ruta + [(x, y)]
        if (x, y) == fin:
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

        rutas.sort(key=lambda x: x[1], reverse=not minimizar)  # Ordenar por costo acumulado

    return mejor_costo, mejor_ruta

# Calcular el menor y mayor costo
menor_costo, menor_ruta = buscar_ruta(matriz, inicio, fin, minimizar=True)
mayor_costo, mayor_ruta = buscar_ruta(matriz, inicio, fin, minimizar=False)

# Imprimir los resultados
print(f"Menor costo: {menor_costo}, Ruta: {menor_ruta}")
print(f"Mayor costo: {mayor_costo}, Ruta: {mayor_ruta}")

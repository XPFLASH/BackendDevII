""" 
    Materia: Desarrollo de Backend II
    Algoritmo de Ordenamiento Romano

    Encontrar los numeros romanos dentro de una palabras
"""


# Los números romanos válidos son:
# I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
# Solo se suman los números en secuencias crecientes.
# En caso de no ser válida la palabra será 0


# Valores de las palabras calculadas manualmente:
# Pixel = 9, Civil = 104, Paco = 100, Hijo = 1, Toxico = 11 Camion = 901, Clave = 150, Ximena = 11
# Damian = 500, Superar = 0, Lili = 51, Claudia = 150, Medallon = 1550, Clima = 151, Doctor = 600]

# Letras de las palabras calculadas manualmente:
# Pixel = IX, Civil = CIV, Paco = C, Hijo = I, Toxico = XI Camion = 901, Clave = CLV, Ximena = XI
# Damian = D, Superar = 0, Lili = LI, Claudia = CL, Medallon = MDL, Clima = CLI, Doctor = DC]


# Lista de Palabras
palabras = [
    "Pixel", "Civil", "Paco", "Hijo", 
    "Toxico", "Camion", "Clave", "Ximena", 
    "Damian", "Superar", "Lili", "Claudia", 
    "Medallon", "Clima", "Doctor",
]


# Diccionario de letras romanas con sus respectivos valores
numRom = {
    "I" : 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
}

def ordenamiento_romano(palabra):
    """
    En esta función se realizar el calculo para obtener el valor romano de la palabra
    donde se recorre cada letra de la palabra para compararla con alguna letra valida 
    del diccionario 'numRom' en donde dependiendo de las condiciones devuelve el valor
    correspondiente.

    Args:
        palabra (str): La palabra en la que se buscan letras romanos.

    Regresa:
        Valor (int): El valor total de los números romanos dentro de la palabra

    """
    valor = 0
    anterior = 0

    for letra in palabra.upper():
        if letra in numRom:
            actual = numRom[letra]

            if anterior > 0 and actual > anterior:
                if anterior in [1, 10, 100] and actual in [5 * anterior, 10 * anterior]:
                    valor += actual - (2 * anterior)
                else:
                    break
            else:
                valor += actual
            anterior = actual
    return valor

def imprimir_valor():
    """
    Dentro de esta función se recorre la lista de palabras para calcular el valor
    de las letras romanas, en donde para cada palabra se ejecuta la función de
    'ordenamiento_romano' para calcular su valor

    Esta función imprime solamente los resultados
    """
    for palabra in palabras:
        valor_romano = ordenamiento_romano(palabra)
        print(f"La Palabra '{palabra}' tiene el valor de {valor_romano} ")

imprimir_valor()

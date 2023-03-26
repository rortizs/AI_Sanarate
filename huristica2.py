import numpy as np


def distancia_euclidiana(ciudad1, ciudad2):
    return np.sqrt((ciudad1[0] - ciudad2[0]) ** 2 + (ciudad1[1] - ciudad2[1]) ** 2)


def distancia_total(camino, matriz_distancias):
    distancia = 0
    for i in range(len(camino) - 1):
        distancia += matriz_distancias[camino[i]][camino[i + 1]]
    distancia += matriz_distancias[camino[-1]][camino[0]]
    return distancia


def intercambiar_2opt(camino, i, k):
    nuevo_camino = camino[:i] + camino[i:k+1][::-1] + camino[k+1:]
    return nuevo_camino


def busqueda_local_2opt(ciudades):
    n_ciudades = len(ciudades)
    matriz_distancias = np.array([[distancia_euclidiana(
        ciudades[i], ciudades[j]) for j in range(n_ciudades)] for i in range(n_ciudades)])

    # Inicializar el camino
    camino = list(range(n_ciudades))

    mejora = True
    while mejora:
        mejora = False
        mejor_distancia = distancia_total(camino, matriz_distancias)
        for i in range(n_ciudades - 1):
            for k in range(i + 1, n_ciudades):
                nuevo_camino = intercambiar_2opt(camino, i, k)
                nueva_distancia = distancia_total(
                    nuevo_camino, matriz_distancias)
                if nueva_distancia < mejor_distancia:
                    camino = nuevo_camino
                    mejor_distancia = nueva_distancia
                    mejora = True

    return camino, mejor_distancia


# Coordenadas de las ciudades
ciudades = [
    (0, 0),
    (1, 5.5),
    (2, 3),
    (5, 6),
    (6, 1),
    (3, 7),
    (5, 8),
    (9, 2)
]

mejor_camino, mejor_distancia = busqueda_local_2opt(ciudades)
print("Mejor camino encontrado:", mejor_camino)
print("Distancia total del mejor camino:", mejor_distancia)

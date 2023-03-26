#Este ejemplo crea un grafo con ciudades etiquetadas con letras 'A' a 'F' y con distancias arbitrarias entre ellas. La función heuristica es una función simple que toma en cuenta la diferencia entre los caracteres de las ciudades. La función busqueda_a_estrella implementa el algoritmo A* en base a esta heurística. Finalmente, se busca una ruta desde la ciudad 'A' hasta la ciudad 'F'.

import heapq


class Grafo:
    def __init__(self):
        self.ciudades = {}
        self.distancias = {}

    def agregar_ciudad(self, ciudad):
        self.ciudades[ciudad] = []

    def agregar_conexion(self, ciudad1, ciudad2, distancia):
        self.ciudades[ciudad1].append(ciudad2)
        self.ciudades[ciudad2].append(ciudad1)
        self.distancias[(ciudad1, ciudad2)] = distancia
        self.distancias[(ciudad2, ciudad1)] = distancia


def heuristica(ciudad_actual, ciudad_objetivo):
    # Función heurística simple, podría ser cualquier otra función dependiendo del problema
    return abs(ord(ciudad_actual) - ord(ciudad_objetivo))


def busqueda_a_estrella(grafo, inicio, objetivo):
    abiertos = [(0 + heuristica(inicio, objetivo), 0, inicio, [])]
    visitados = set()

    while abiertos:
        _, costo_actual, ciudad_actual, camino = heapq.heappop(abiertos)
        if ciudad_actual == objetivo:
            return camino + [objetivo]

        if ciudad_actual not in visitados:
            visitados.add(ciudad_actual)
            for vecino in grafo.ciudades[ciudad_actual]:
                nuevo_costo = costo_actual + \
                    grafo.distancias[(ciudad_actual, vecino)]
                nuevo_camino = camino + [ciudad_actual]
                heapq.heappush(abiertos, (nuevo_costo + heuristica(vecino,
                               objetivo), nuevo_costo, vecino, nuevo_camino))

    return None


# Creación de un grafo simple
grafo = Grafo()
for ciudad in 'ABCDEF':
    grafo.agregar_ciudad(ciudad)

grafo.agregar_conexion('A', 'B', 1)
grafo.agregar_conexion('A', 'C', 2)
grafo.agregar_conexion('B', 'D', 3)
grafo.agregar_conexion('B', 'E', 4)
grafo.agregar_conexion('C', 'F', 5)
grafo.agregar_conexion('D', 'F', 6)
grafo.agregar_conexion('E', 'F', 1)

ruta = busqueda_a_estrella(grafo, 'A', 'F')
print("Ruta encontrada:", ruta)

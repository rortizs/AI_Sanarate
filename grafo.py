from queue import Queue

def bfs_search(graph, start, goal):
    # Inicializar cola y visitados
    queue = Queue()
    visited = set()

    # Añadir el nodo inicial a la cola
    queue.put(start)

    # Bucle principal
    while not queue.empty():
        # Sacar el siguiente nodo de la cola
        node = queue.get()

        # Si el nodo es la meta, devolver la solución
        if node == goal:
            return "Solución encontrada"

        # Marcar el nodo como visitado
        visited.add(node)

        # Añadir los nodos vecinos no visitados a la cola
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.put(neighbor)

    # Si no se encuentra solución, devolver mensaje de error
    return "No se encontró solución"

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
goal_node = 'F'

result = bfs_search(graph, start_node, goal_node)

print(result)

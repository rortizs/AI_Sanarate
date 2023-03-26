import networkx as nx
import matplotlib.pyplot as plt


def DFS_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        G.add_edge(start, next)
        DFS_recursive(graph, next, visited)
    return visited


# Ejemplo de uso
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

G = nx.Graph()
DFS_recursive(graph, 'A')
nx.draw(G, with_labels=True)
plt.show()

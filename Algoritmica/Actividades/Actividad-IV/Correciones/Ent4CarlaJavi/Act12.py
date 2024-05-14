"""12. Haciendo caso omiso de las ponderaciones, realiza una búsqueda en anchura en el grafo de la pregunta
anterior"""
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Considering undirected graph

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                for neighbor, _ in sorted(self.graph[node]):  # Sorting neighbors for deterministic results
                    if neighbor not in visited:
                        queue.append(neighbor)

# Construyamos el grafo
g = Graph()
edges = [(1, 2, 10), (1, 3, 15), (1, 6, 5), (2, 3, 7), (3, 4, 7), (3, 6, 10), (4, 5, 7), (5, 6, 13), (6, 4, 5)]
for edge in edges:
    g.add_edge(*edge)

# Realicemos la búsqueda en anchura desde el nodo 1
print("Recorrido BFS:")
g.bfs(1)

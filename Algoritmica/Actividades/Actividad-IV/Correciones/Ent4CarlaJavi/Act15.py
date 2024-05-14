"""15. Dado el grafo dirigido y valorado de la figura, encuentra el camino más corto desde el vértice A a todos los
demás vértices usando el algoritmo de Dijkstra. Describe el proceso paso a paso"""
import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    print(f"Inicializando las distancias desde el nodo de inicio '{start}': {distances}")

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        print(f"\nNodo actual: {current_node} con distancia: {current_distance}")

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                print(f"Encontrado un camino más corto al nodo {neighbor} a través de {current_node} con distancia {distance}")
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Definimos el grafo
graph = {
    'A': {'D': 8, 'H': 11, 'C': 6},
    'C': {'A': 6, 'D': 4, 'F': 12, 'B': 5},
    'B': {'C': 5, 'E': 3, 'D': 10},
    'D': {'B': 10, 'A': 8, 'C': 4, 'F': 6, 'H': 9},
    'E': {'B': 3, 'F': 6, 'H': 5},
    'F': {'D': 6, 'C': 12, 'E': 6},
    'H': {'D': 9, 'E': 5, 'A': 11}
}

# Ejecutamos el algoritmo de Dijkstra
distances = dijkstra(graph, 'A')

# Imprimimos las distancias desde A a todos los demás vértices
print("\nDistancias finales desde A a todos los demás vértices:")
for node, distance in distances.items():
    print(f"La distancia desde A hasta {node} es {distance}")

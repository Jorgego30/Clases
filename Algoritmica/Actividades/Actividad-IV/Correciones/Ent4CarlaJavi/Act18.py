"""18. Dado el grafo de la figura, encuentra un árbol de expansión de coste mínimo describiendo el proceso paso a
paso mediante el algoritmo de Prim"""
import heapq

def prim(graph, start):
    mst = []
    used = set([start])
    edges = [
        (cost, start, to)
        for to, cost in graph[start].items()
    ]
    heapq.heapify(edges)

    print(f"Inicializando las aristas desde el nodo de inicio '{start}': {edges}")

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in used:
            used.add(to)
            mst.append((frm, to, cost))

            print(f"\nNodo actual: {frm}, nodo vecino: {to} con peso: {cost}")

            for to_next, cost2 in graph[to].items():
                if to_next not in used:
                    heapq.heappush(edges, (cost2, to, to_next))
                    print(f"Agregando arista {to} - {to_next} con peso {cost2} a la cola")

    return mst

# Definimos el grafo
graph = {
    'Z': {'H': 2, 'J': 4, 'W': 4},
    'H': {'Z': 2, 'J': 3},
    'J': {'H': 3, 'Z': 4, 'R': 1},
    'W': {'Z': 4, 'R': 1},
    'R': {'J': 1, 'W': 1, 'K': 1, 'Y': 1},
    'K': {'R': 1, 'Y': 2, 'T': 6, 'L': 5},
    'Y': {'R': 1, 'K': 2, 'T': 5},
    'L': {'K': 5, 'T': 2},
    'T': {'L': 2, 'Y': 5, 'K': 6}
}

# Ejecutamos el algoritmo de Prim
mst = prim(graph, 'Z')

# Imprimimos el árbol de expansión mínimo
print("\nÁrbol de expansión de coste mínimo:")
for frm, to, cost in mst:
    print(f"{frm} - {to} con peso {cost}")

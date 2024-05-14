from graphviz import Digraph

def dijkstra(grafo, inicio):
    distancia = {v: float('inf') for v in grafo}
    distancia[inicio] = 0
    visitado = set()

    while len(visitado) < len(grafo):
        vertice_actual = None
        distancia_minima = float('inf')

        # Buscamos el vértice no visitado con la distancia mínima
        for v in grafo:
            if v not in visitado and distancia[v] < distancia_minima:
                vertice_actual = v
                distancia_minima = distancia[v]

        visitado.add(vertice_actual)

        # Actualizamos las distancias de los vecinos del vértice actual
        for vecino, peso in grafo[vertice_actual]:
            distancia_hasta_vecino = distancia[vertice_actual] + peso
            if distancia_hasta_vecino < distancia[vecino]:
                distancia[vecino] = distancia_hasta_vecino

    return distancia

# Definimos el grafo como un diccionario de listas de tuplas (vecino, peso)
grafo = {
    1: [(2, 10), (3, 15), (6, 5)],
    2: [(3, 7)],
    3: [(4, 7), (6, 10)],
    4: [(5, 7)],
    5: [(6, 13)],
    6: [(4, 5)]
}

# Creamos una instancia de Digraph para visualizar el grafo
grafo_visual = Digraph()

# Agregamos los nodos y las aristas al grafo visual
for vertice, conexiones in grafo.items():
    grafo_visual.node(str(vertice))
    for vecino, peso in conexiones:
        grafo_visual.edge(str(vertice), str(vecino), label=str(peso))

# Aplicamos el algoritmo de Dijkstra al grafo desde el vértice 1
resultado_dijkstra = dijkstra(grafo, 1)

# Mostramos los resultados paso a paso y agregamos las etiquetas de distancia al grafo visual
for vertice, distancia in resultado_dijkstra.items():
    print(f"Distancia mínima desde 1 hasta {vertice}: {distancia}")
    grafo_visual.node(str(vertice), label=f"{vertice}\nDistancia: {distancia}")

# Guardamos y visualizamos el grafo
grafo_visual.render('grafo_con_distancias', format='png', view=True)

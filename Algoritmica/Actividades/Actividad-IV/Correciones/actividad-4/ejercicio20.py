'''Utilizando la búsqueda en anchura, escribe un algoritmo que puede determinar la ruta más corta de cada
vértice a cada uno de los otros vértices. Esto se llama el problema de la ruta más corta de todas las parejas.'''

import networkx as nx

# Crear el grafo
grafo = nx.DiGraph()

# Agregar las aristas al grafo
grafo.add_edge('A', 'B', weight=3)
grafo.add_edge('A', 'C', weight=5)
grafo.add_edge('B', 'C', weight=1)
grafo.add_edge('B', 'D', weight=2)
grafo.add_edge('C', 'D', weight=4)

# Calcular las rutas más cortas de todas las parejas
rutas_mas_cortas = nx.floyd_warshall(grafo, weight='weight')

# Imprimir las rutas más cortas de todas las parejas
for origen in rutas_mas_cortas:
    for destino in rutas_mas_cortas[origen]:
        if origen != destino:
            distancia = rutas_mas_cortas[origen][destino]
            print("Ruta más corta entre {} y {}: {}".format(origen, destino, distancia))
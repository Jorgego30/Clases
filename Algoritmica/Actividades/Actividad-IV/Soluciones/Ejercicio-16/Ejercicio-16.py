import heapq
import networkx as nx
import matplotlib.pyplot as plt

def prim(grafo):
    arbol_expansion = []
    nodos_visitados = set()
    nodo_inicial = list(grafo.keys())[0]  # Elegir un nodo inicial arbitrario

    nodos_visitados.add(nodo_inicial)
    aristas = [(costo, nodo_inicial, vecino) for vecino, costo in grafo[nodo_inicial]]
    heapq.heapify(aristas)

    while aristas:
        costo, origen, destino = heapq.heappop(aristas)
        if destino not in nodos_visitados:
            arbol_expansion.append((origen, destino, costo))
            nodos_visitados.add(destino)
            for vecino, costo in grafo[destino]:
                if vecino not in nodos_visitados:
                    heapq.heappush(aristas, (costo, destino, vecino))
        # Dibuja el grafo actualizado en cada paso
        dibujar_grafo(grafo, arbol_expansion, nodos_visitados)

    return arbol_expansion

def dibujar_grafo(grafo, arbol_expansion, nodos_visitados):
    G = nx.Graph()

    for nodo, vecinos in grafo.items():
        for vecino, peso in vecinos:
            if (nodo, vecino, peso) in arbol_expansion or (vecino, nodo, peso) in arbol_expansion:
                G.add_edge(nodo, vecino, weight=peso)

    pos = nx.spring_layout(G)  # Posición de los nodos
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}

    plt.figure(figsize=(10, 6))
    # Dibuja los nodos
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue')
    # Dibuja las aristas
    nx.draw_networkx_edges(G, pos)
    # Dibuja las etiquetas de los nodos
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    # Dibuja las etiquetas de las aristas
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
    # Resalta los nodos visitados
    nx.draw_networkx_nodes(G, pos, nodelist=list(nodos_visitados), node_color='red', node_size=700)
    plt.title('Árbol de Expansión Mínima (Prim)')
    plt.show()

# Grafo de ejemplo
grafo = {
    'A': [('C', 6), ('H', 11)],
    'B': [('E', 3)],
    'C': [('B', 5), ('F', 12)],
    'D': [('C', 4), ('F', 6), ('B', 10)],
    'E': [('F', 6)],
    'F': [],
    'H': [('E', 5), ('D', 9)]
}

# Ejecutar el algoritmo de Prim y visualizar el paso a paso
arbol_expansion_prim = prim(grafo)

# Imprimir el árbol de expansión mínima
print("Árbol de expansión mínima (Prim):")
for arista in arbol_expansion_prim:
    print(arista)

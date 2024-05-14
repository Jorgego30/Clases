import networkx as nx
import matplotlib.pyplot as plt
import heapq

def prim_step_by_step(grafo):
    arbol_expansion = []
    nodos_visitados = set()
    nodo_inicial = list(grafo.keys())[0]  # Elegir un nodo inicial arbitrario

    nodos_visitados.add(nodo_inicial)
    aristas = [(costo, nodo_inicial, vecino) for vecino, costo in grafo[nodo_inicial]]
    heapq.heapify(aristas)

    # Crear un gráfico vacío
    G = nx.Graph()

    # Agregar nodos al gráfico
    for nodo in grafo.keys():
        G.add_node(nodo)

    # Iterar hasta que no haya aristas o todos los nodos estén visitados
    while aristas and len(nodos_visitados) < len(grafo):
        # Obtener la arista mínima
        costo, origen, destino = heapq.heappop(aristas)
        # Si el destino no ha sido visitado, agregarlo al árbol de expansión mínima
        if destino not in nodos_visitados:
            arbol_expansion.append((origen, destino))
            nodos_visitados.add(destino)
            # Agregar la arista al gráfico
            G.add_edge(origen, destino)

            # Visualizar el gráfico actual
            plt.figure(figsize=(10, 6))
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_weight='bold')
            labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
            plt.title("Árbol de expansión mínima (Prim)")
            plt.show()

            # Actualizar las aristas disponibles para el nuevo nodo visitado
            for vecino, costo in grafo[destino]:
                if vecino not in nodos_visitados:
                    heapq.heappush(aristas, (costo, destino, vecino))

    return arbol_expansion

# Grafo de ejemplo
grafo = {
    'h': [('j', 3), ('z', 2)],
    'j': [('h', 3), ('z', 4), ('r', 1)],
    'z': [('h', 2), ('j', 4), ('w', 4)],
    'w': [('z', 4), ('r', 1)],
    'r': [('j', 1), ('w', 1), ('y', 1), ('k', 1)],
    'y': [('r', 1), ('k', 2), ('t', 5)],
    'k': [('r', 1), ('y', 2), ('t', 6), ('l', 5)],
    't': [('y', 5), ('k', 6), ('l', 2)],
    'l': [('k', 5), ('t', 2)]
}

# Ejecutar el algoritmo de Prim paso a paso
arbol_expansion_prim = prim_step_by_step(grafo)

# Imprimir el árbol de expansión mínima
print("Árbol de expansión mínima (Prim):", arbol_expansion_prim)

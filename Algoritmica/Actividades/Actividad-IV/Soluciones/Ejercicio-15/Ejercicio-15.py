import networkx as nx
import matplotlib.pyplot as plt

# Representación del grafo
grafo = {
    'A': [('C', 6), ('H', 11)],
    'B': [('E', 3)],
    'C': [('B', 5), ('F', 12)],
    'D': [('C', 4), ('F', 6), ('B', 10)],
    'E': [('F', 6)],
    'F': [],
    'H': [('E', 5),('D', 9)]
}

# Inicialización de las distancias
distancias = {nodo: float('inf') for nodo in grafo}
distancias['A'] = 0

# Conjunto de nodos no visitados
nodos_no_visitados = set(grafo.keys())

# Crear el grafo dirigido
G = nx.DiGraph()

# Agregar nodos al grafo
for nodo in grafo:
    G.add_node(nodo)

# Bucle principal
for paso in range(len(grafo)):
    # Seleccionar el nodo con la distancia mínima
    nodo_actual = min(nodos_no_visitados, key=lambda nodo: distancias[nodo])

    # Eliminar el nodo actual del conjunto de nodos no visitados
    nodos_no_visitados.remove(nodo_actual)

    # Actualizar las distancias a los nodos vecinos del nodo actual
    for vecino, peso in grafo[nodo_actual]:
        distancia = distancias[nodo_actual] + peso
        if distancia < distancias[vecino]:
            distancias[vecino] = distancia
            # Agregar arista al grafo dirigido
            G.add_edge(nodo_actual, vecino, weight=peso)

    # Dibujar el grafo en cada paso
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G, seed=42)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=12, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title(f'Paso {paso + 1}: Nodo actual = {nodo_actual}')
    plt.show()

# Imprimir las distancias más cortas desde el nodo de inicio (A) a todos los demás nodos
for nodo, distancia in distancias.items():
    print(f'Distancia desde A hasta {nodo}: {distancia}')

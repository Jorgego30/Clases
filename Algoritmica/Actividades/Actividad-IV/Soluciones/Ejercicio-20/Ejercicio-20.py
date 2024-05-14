def floyd_warshall(grafo):
    # Inicializamos la matriz de distancias con infinito para todas las parejas de vértices
    V = len(grafo)
    distancias = [[float('inf')] * V for _ in range(V)]

    # Inicializamos la diagonal con distancia 0 y llenamos la matriz con las distancias conocidas
    for i in range(V):
        distancias[i][i] = 0
        for vecino, peso in grafo[i]:
            distancias[i][vecino] = peso

    # Actualizamos las distancias utilizando todos los vértices como intermedios
    for k in range(V):
        for i in range(V):
            for j in range(V):
                distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])

    return distancias

# Ejemplo de grafo representado como un diccionario de listas de tuplas (vecino, peso)
grafo = {
    0: [(1, 3), (2, 6)],
    1: [(0, 3), (2, 2)],
    2: [(0, 6), (1, 2)]
}

# Aplicamos el algoritmo de Floyd-Warshall para encontrar las distancias más cortas entre todos los pares de vértices
distancias_minimas = floyd_warshall(grafo)

# Imprimimos la matriz de distancias mínimas
print("Matriz de distancias mínimas:")
for fila in distancias_minimas:
    print(fila)

"""14. Utilizando el ejercicio 8, implementar el método decrementarClave en la clase MonticuloBinario para
que funcione el algoritmo de Dijkstra. Muestra cada paso al aplicar el algoritmo de Dijkstra al grafo
resultante del problema 11. """
# Importamos las clases del primer código
from collections import defaultdict

class MonticuloBinario:
    def __init__(self):
        self.heap = []

    def agregar(self, elemento):
        self.heap.append(elemento)
        self.avanzar(len(self.heap) - 1)

    def avanzar(self, indice):
        while indice > 0:
            padre = (indice - 1) // 2
            if self.heap[indice][0] < self.heap[padre][0]:
                self.heap[indice], self.heap[padre] = self.heap[padre], self.heap[indice]
                indice = padre
            else:
                break

    def decrementarClave(self, indice, nueva_clave):
        if nueva_clave > self.heap[indice][0]:
            raise ValueError("La nueva clave es mayor que la clave actual")
        self.heap[indice] = (nueva_clave, self.heap[indice][1])
        self.avanzar(indice)

class ColaPrioridad:
    def __init__(self):
        self.heap = MonticuloBinario()

    def agregar(self, clave, valor):
        self.heap.agregar((clave, valor))

    def avanzar(self):
        return self.heap.heap.pop(0)

class Grafo:
    def __init__(self):
        self.adj = {}

    def agregar_arista(self, u, v, peso):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append((v, peso))

def dijkstra(grafo, inicio):
    distancia = {nodo: float('inf') for nodo in grafo.adj}
    distancia[inicio] = 0
    visitados = set()
    cola = ColaPrioridad()
    cola.agregar(0, inicio)

    while cola.heap.heap:
        dist, nodo = cola.avanzar()
        if nodo in visitados:
            continue
        visitados.add(nodo)
        for vecino, peso in grafo.adj.get(nodo, []):
            nueva_distancia = dist + peso
            if nueva_distancia < distancia[vecino]:
                distancia[vecino] = nueva_distancia
                try:
                    indice = cola.heap.heap.index((distancia[vecino], vecino))
                    cola.heap.decrementarClave(indice, nueva_distancia)
                except ValueError:
                    pass
                cola.agregar(nueva_distancia, vecino)

    return distancia

# Crear el grafo del ejercicio 11
g = Grafo()
aristas = [(1, 2, 10), (1, 3, 15), (1, 6, 5), (2, 3, 7), (3, 4, 7), (3, 6, 10), (4, 5, 7), (6, 4, 5), (5, 6, 13)]
for u, v, peso in aristas:
    g.agregar_arista(u, v, peso)

# Aplicar algoritmo de Dijkstra desde el nodo 1
distancias = dijkstra(g, 1)
print("Distancias mínimas desde el nodo 1:")
for nodo, distancia in distancias.items():
    print(f"Nodo {nodo}: Distancia {distancia}")

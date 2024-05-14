"""16. Usando el algoritmo de Prim, encuentra el árbol de expansión de ponderación mínima"""
from collections import defaultdict

class Grafo:
    def __init__(self):
        self.vertices = set()
        self.aristas = defaultdict(list)

    def agregar_arista(self, u, v, peso):
        """
        Agrega una arista entre los nodos u y v con el peso dado al grafo.
        """
        self.vertices.add(u)
        self.vertices.add(v)
        self.aristas[u].append((v, peso))
        self.aristas[v].append((u, peso))

    def prim(self, inicio):
        """
        Ejecuta el algoritmo de Prim para encontrar el árbol de expansión
        de ponderación mínima comenzando desde el nodo 'inicio'.
        """
        arbol_expansion = []  # Lista para almacenar las aristas del árbol de expansión
        visitados = set()     # Conjunto para mantener los nodos visitados
        visitados.add(inicio) # Se agrega el nodo de inicio a los visitados

        # Mientras queden nodos por visitar
        while len(visitados) < len(self.vertices):
            min_peso = float('inf')
            min_arista = None

            # Iterar sobre los nodos visitados para encontrar la arista de menor peso
            for u in visitados:
                for v, peso in self.aristas[u]:
                    # Si el nodo 'v' no ha sido visitado y el peso es menor que el mínimo encontrado hasta ahora
                    if v not in visitados and peso < min_peso:
                        min_peso = peso
                        min_arista = (u, v)

            # Agregar la arista de menor peso al árbol de expansión y marcar el nodo 'v' como visitado
            arbol_expansion.append(min_arista)
            visitados.add(min_arista[1])

        return arbol_expansion

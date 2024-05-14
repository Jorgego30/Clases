"""19. Escribe el método transponer para la clase Grafo."""
class Grafo:
    def __init__(self):
        self.vertices = set()
        self.aristas = {}

    def agregar_arista(self, u, v):
        self.vertices.add(u)
        self.vertices.add(v)
        if u not in self.aristas:
            self.aristas[u] = []
        self.aristas[u].append(v)

    def transponer(self):
        grafo_transpuesto = Grafo()
        for u in self.vertices:
            if u in self.aristas:
                for v in self.aristas[u]:
                    grafo_transpuesto.agregar_arista(v, u)
        return grafo_transpuesto

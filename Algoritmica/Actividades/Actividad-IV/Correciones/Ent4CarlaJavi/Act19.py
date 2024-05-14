"""19. Escribe el método transponer para la clase Grafo."""
# Importamos la clase Grafo del primer código
from Clases19 import Grafo

# Creamos el grafo del ejemplo
g = Grafo()
g.agregar_arista(1, 2)
g.agregar_arista(1, 3)
g.agregar_arista(2, 3)
g.agregar_arista(3, 4)
g.agregar_arista(4, 1)

# Obtenemos el grafo transpuesto
grafo_transpuesto = g.transponer()

# Mostramos el grafo original y el grafo transpuesto
print("Grafo original:")
for u in g.vertices:
    if u in g.aristas:
        for v in g.aristas[u]:
            print(f"{u} -> {v}")

print("\nGrafo transpuesto:")
for u in grafo_transpuesto.vertices:
    if u in grafo_transpuesto.aristas:
        for v in grafo_transpuesto.aristas[u]:
            print(f"{u} -> {v}")

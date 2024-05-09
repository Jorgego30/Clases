
from graphviz import Digraph

# Creamos una instancia del grafo dirigido
grafo = Digraph()

# Creamos los vértices y agregamos las aristas con sus costos
aristas = [
    (1, 2, 10),
    (1, 3, 15),
    (1, 6, 5),
    (2, 3, 7),
    (3, 4, 7),
    (3, 6, 10),
    (4, 5, 7),
    (6, 4, 5),
    (5, 6, 13)
]

for de, a, costo in aristas:
    grafo.edge(str(de), str(a), label=str(costo))

# Guardamos el grafo en un archivo y lo visualizamos
grafo.render('grafo', format='png', view=True)

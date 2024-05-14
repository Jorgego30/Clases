"""16. Usando el algoritmo de Prim, encuentra el árbol de expansión de ponderación mínima"""
# Importamos la clase Grafo del primer código
from Clases16 import Grafo

# Creamos el grafo del ejemplo
g = Grafo()
g.agregar_arista(1, 2, 3)
g.agregar_arista(1, 3, 6)
g.agregar_arista(1, 4, 5)
g.agregar_arista(2, 3, 1)
g.agregar_arista(2, 4, 4)
g.agregar_arista(3, 4, 7)
g.agregar_arista(3, 5, 2)
g.agregar_arista(4, 5, 6)

# Ejecutamos el algoritmo de Prim desde el nodo 1
arbol_minimo = g.prim(1)

# Mostramos el árbol de expansión de ponderación mínima
print("Árbol de expansión de ponderación mínima:")
for arista in arbol_minimo:
    print(arista)

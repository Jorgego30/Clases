#17. ¿Cuál es el tiempo de ejecución O-grande para el algoritmo de Prim del árbol de expansión mínimo?

#Sería O(nlogn) ya que es la forma más eficiente de un algoritmo voraz

#Demostracion partiendo del 16:

from Class_Grafos import Grafo
import sys
import timeit
from priorityQueue import PriorityQueue


def prim(G,inicio):
    cp = PriorityQueue()
    for v in G:
        v.asignarDistancia(sys.maxsize)
        v.asignarPredecesor(None)
    inicio.asignarDistancia(0)
    cp.buildHeap([(v.obtenerDistancia(),v) for v in G])
    while not cp.isEmpty():
        verticeActual = cp.delMin()
        for verticeSiguiente in verticeActual.obtenerConexiones():
          nuevoCosto = verticeActual.obtenerPonderacion(verticeSiguiente)
          if verticeSiguiente in cp and nuevoCosto<verticeSiguiente.obtenerDistancia():
              verticeSiguiente.asignarPredecesor(verticeActual)
              verticeSiguiente.asignarDistancia(nuevoCosto)
              cp.decreaseKey(verticeSiguiente,nuevoCosto)




G = Grafo()
G.agregarVertice('A')
G.agregarVertice('B')
G.agregarVertice('C')
G.agregarVertice('D')
G.agregarVertice('E')
G.agregarVertice('F')
G.agregarVertice('H')

G.agregarArista("A","C",6),
G.agregarArista("A","H",11),
G.agregarArista("B","E",3),
G.agregarArista("C","B",5),
G.agregarArista("C","F",12),
G.agregarArista("D","A",8),
G.agregarArista("D","C",4),
G.agregarArista("D","B",10),
G.agregarArista("D","F",6),
G.agregarArista("E","F",6),
G.agregarArista("H","D",9),
G.agregarArista("H","E",5)



print("Sin aplicar algoritmo de prim:\n")
for v in G:
    for w in v.obtenerConexiones():
        print("( %s , %s )" % (v.obtenerId(), w.obtenerId()))
        
 


# Imprime el árbol de expansión mínima
print("Aplicando algoritmo de prim")
for v in G:
    if v.obtenerPredecesor():
        print("(%s , %s)" % (v.obtenerPredecesor().obtenerId(), v.obtenerId()))


# Ejecuta el algoritmo de Prim
for i in range(1000,21000,1000):
    tempo=timeit.timeit(lambda:prim(G, G.obtenerVertice('A')),number=i)
    print(tempo)

print("Ya que la tendencia es un poco superior a O(n), podemos aproximar que es O(nlogn)")
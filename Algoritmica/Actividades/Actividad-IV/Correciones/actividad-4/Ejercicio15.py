#Dado el grafo dirigido y valorado de la figura, encuentra el camino más corto desde el vértice A a todos los
#demás vértices usando el algoritmo de Dijkstra. Describe el proceso paso a paso.

from Class_Grafos import *
from Class_Vertices import Vertice
from priorityQueue import *

def dijkstra(unGrafo,inicio):
    cp = PriorityQueue() #Realmente se implementa con un Montículo binario
    inicio.asignarDistancia(0)
    cp.buildHeap([(v.obtenerDistancia(),v) for v in unGrafo])
    while not cp.isEmpty():
        verticeActual = cp.delMin()
        if verticeActual.obtenerDistancia() > 100:
            print("Id: ",verticeActual.obtenerId(),"distancia: Imposible")
        else:
            print("Id: ",verticeActual.obtenerId(),"distancia: ",verticeActual.obtenerDistancia())
        for verticeSiguiente in verticeActual.obtenerConexiones():
            nuevaDistancia = verticeActual.obtenerDistancia() + verticeActual.obtenerPonderacion(verticeSiguiente)
            if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarDistancia( nuevaDistancia )
                verticeSiguiente.asignarPredecesor(verticeActual)
                cp.decreaseKey(verticeSiguiente,nuevaDistancia)
    

g = Grafo()
for i in range(8):
    g.agregarVertice(i)

a = 1
b = 2
c = 3 
d = 4
e = 5
f = 6
h = 7   

g.agregarArista(a,c,6)
g.agregarArista(a,h,11)
g.agregarArista(c,b,5)
g.agregarArista(c,f,12)
g.agregarArista(b,e,3)
g.agregarArista(e,f,6)
g.agregarArista(h,e,5)
g.agregarArista(h,d,9)
g.agregarArista(d,d,10)
g.agregarArista(d,a,8)
g.agregarArista(d,f,6)

dijkstra(g,g.obtenerVertice(a))

#Como el algoritmo de dijsktra modifica el grafo si lo volvemos a ejecutar con el mismo 
# grafo dara valores incorrectos

#dijkstra(g,g.obtenerVertice(2))
#dijkstra(g,g.obtenerVertice(3))
#dijkstra(g,g.obtenerVertice(4))
#dijkstra(g,g.obtenerVertice(5))
#dijkstra(g,g.obtenerVertice(6))
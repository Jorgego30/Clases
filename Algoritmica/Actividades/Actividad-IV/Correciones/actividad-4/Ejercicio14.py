#Utilizando el ejercicio 8, implementar el método decrementarClave en la clase MonticuloBinario para
#que funcione el algoritmo de Dijkstra. Muestra cada paso al aplicar el algoritmo de Dijkstra al grafo
#resultante del problema 11

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
for i in range(1,7,1):
    g.agregarVertice(i)

g.agregarArista(1,2,10)
g.agregarArista(1,3,15)
g.agregarArista(1,6,5)
g.agregarArista(2,3,7)
g.agregarArista(3,4,7)
g.agregarArista(3,6,10)
g.agregarArista(4,5,7)
g.agregarArista(6,4,5)
g.agregarArista(5,6,13)

dijkstra(g,g.obtenerVertice(3))

#Como el algoritmo de dijsktra modifica el grafo si lo volvemos a ejecutar con el mismo 
# grafo dara valores incorrectos

#dijkstra(g,g.obtenerVertice(2))
#dijkstra(g,g.obtenerVertice(3))
#dijkstra(g,g.obtenerVertice(4))
#dijkstra(g,g.obtenerVertice(5))
#dijkstra(g,g.obtenerVertice(6))



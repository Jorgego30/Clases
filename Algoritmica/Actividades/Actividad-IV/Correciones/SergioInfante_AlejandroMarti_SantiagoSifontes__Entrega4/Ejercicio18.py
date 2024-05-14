#18. Dado el grafo de la figura, encuentra un árbol de expansión de coste mínimo describiendo el proceso paso a
#paso mediante el algoritmo de Prim

from Class_Grafos import Grafo

import sys

from priorityQueue import PriorityQueue

import networkx as nx
import matplotlib.pyplot as plt

def draw(self, name=None, arrows=True, mapon=None, edge_route=None, label_color = "black"):
        G = nx.DiGraph()
        node_c = []
        for v in self.listaVertices.values():
            G.add_node(v.id)
 
        for v in self.listaVertices.values():
            l = [x.id for x in v.conectadoA]
            d = [v.conectadoA[x] for x in v.conectadoA]
            i = v.id
            node_c.append(v.color)
            for j in d:
                #print(i, l[d.index(j)],j)
                G.add_edge(i, l[d.index(j)], dis=j)
 
        pos = nx.spring_layout(G, seed=777)
        edge_labels = dict([((u,v,),d['dis']) for u,v,d in G.edges(data=True)])
 
        if mapon:
            nx.draw_networkx_nodes(G, pos, node_color=range(self.numVertices), edgecolors="black", cmap=plt.cm.Blues)
        else:
            nx.draw_networkx_nodes(G, pos, node_color=node_c, edgecolors="black")
 
        nx.draw_networkx_edges(G, pos, arrows=arrows, arrowstyle="-|>", arrowsize=10, edge_color="#010056")
        
        if edge_route:
            nx.draw_networkx_edges(G, pos, edge_color="red", edgelist=edge_route)
        
        nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif', font_color=label_color)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        
        ax = plt.gca()
        ax.margins(0.20)
        ax.set_axis_off()
        plt.title(name)
        plt.show()

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
G.agregarVertice('H')
G.agregarVertice('J')
G.agregarVertice('K')
G.agregarVertice('L')
G.agregarVertice('R')
G.agregarVertice('T')
G.agregarVertice('W')
G.agregarVertice('Y')
G.agregarVertice('Z')


G.agregarArista("H","Z",2),
G.agregarArista("H","J",3),
G.agregarArista("J","H",3),
G.agregarArista("J","Z",4),
G.agregarArista("J","R",1),
G.agregarArista("Z","H",2),
G.agregarArista("Z","J",4),
G.agregarArista("Z","W",3),
G.agregarArista("W","Z",4),
G.agregarArista("W","R",1),
G.agregarArista("R","J",1),
G.agregarArista("R","W",1),
G.agregarArista("R","K",1),
G.agregarArista("R","Y",1),
G.agregarArista("K","R",1),
G.agregarArista("K","Y",2),
G.agregarArista("K","T",6),
G.agregarArista("K","L",5),
G.agregarArista("Y","R",1),
G.agregarArista("Y","K",2),
G.agregarArista("Y","T",5),
G.agregarArista("L","K",5),
G.agregarArista("L","T",2),
G.agregarArista("T","L",2),
G.agregarArista("T","Y",5),
G.agregarArista("T","K",6)

print("Sin aplicar algoritmo de prim:\n")
for v in G:
    for w in v.obtenerConexiones():
        print("( %s , %s )" % (v.obtenerId(), w.obtenerId()))
        
        
# Ejecuta el algoritmo de Prim
prim(G, G.obtenerVertice('H'))



# Imprime el árbol de expansión mínima
print("Aplicando algoritmo de prim")
for v in G:
    if v.obtenerPredecesor():
        print("(%s , %s)" % (v.obtenerPredecesor().obtenerId(), v.obtenerId()))
        

draw(G)

"""
1ºCrea una cola de prioridad (PriorityQueue) para almacenar los vértices que se están considerando.
2ºInicializa todas las distancias de los vértices a infinito y establece sus predecesores como None.
3ºEstablece la distancia del vértice de inicio como 0 y agrega todos los vértices al heap de la cola de prioridad.
4ºMientras la cola de prioridad no esté vacía, saca el vértice con la distancia mínima.
5ºPara cada vecino del vértice actual, si el costo para llegar a ese vecino es menor que su distancia actual, actualiza la distancia y el predecesor, y actualiza la cola de prioridad.
"""
#16. Usando el algoritmo de Prim, encuentra el árbol de expansión de ponderación mínima


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
 
        pos = nx.circular_layout(G)
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
G.agregarVertice('A')
G.agregarVertice('B')
G.agregarVertice('C')
G.agregarVertice('D')
G.agregarVertice('E')
G.agregarVertice('F')
G.agregarVertice('H')

G.agregarArista("A","C",6)
G.agregarArista("A","H",11)
G.agregarArista("B","E",3)
G.agregarArista("C","B",5)
G.agregarArista("C","F",12)
G.agregarArista("D","A",8)
G.agregarArista("D","C",4)
G.agregarArista("D","B",10)
G.agregarArista("D","F",6)
G.agregarArista("E","F",6)
G.agregarArista("H","D",9)
G.agregarArista("H","E",5)



print("Sin aplicar algoritmo de prim:\n")
for v in G:
    for w in v.obtenerConexiones():
        print("( %s , %s )" % (v.obtenerId(), w.obtenerId()))
        
# Ejecuta el algoritmo de Prim
prim(G, G.obtenerVertice('A'))
draw(G)

# Imprime el árbol de expansión mínima
print("Aplicando algoritmo de prim")
for v in G:
    if v.obtenerPredecesor():
        print("(%s , %s)" % (v.obtenerPredecesor().obtenerId(), v.obtenerId()))



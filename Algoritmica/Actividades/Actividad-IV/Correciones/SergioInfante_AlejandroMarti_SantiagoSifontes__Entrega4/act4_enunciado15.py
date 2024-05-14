"""15.  Dado el grafo dirigido y valorado de la figura, encuentra el camino más corto desde el vértice A a todos los 
demás vértices usando el algoritmo de Dijkstra. Describe el proceso paso a paso."""

from Class_Grafos import *
from ColaPrioridad import ColaPrioridad
import subprocess

def dijkstra(unGrafo,inicio):
    cp = ColaPrioridad()
    inicio.asignarDistancia(0)
    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in unGrafo])
    while not cp.estaVacia():
        verticeActual = cp.avanzar() # TUPLA (int,Vertice) (dist,vertice)
        for verticeSiguiente in verticeActual[1].obtenerConexiones():
            # VerticeSiguiente => Vertice
            # verticeActual    => Tupla (int,Vertice) (dist,vertice)
            nuevaDistancia = verticeActual[1].obtenerDistancia() + verticeActual[1].obtenerPonderacion(verticeSiguiente)
            #print("Distancias acumuladas: 1... ==>", verticeActual[1].id, "==>", verticeSiguiente.id)
            #print("Distancia actual: ", "inf" if verticeSiguiente.dist > 100 else verticeSiguiente.dist)
            #print("Nueva distancia: ", nuevaDistancia)
            # nuevaDist => int
            if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarDistancia(nuevaDistancia)
                verticeSiguiente.asignarPredecesor(verticeActual[1])
                cp.decrementarClave(verticeSiguiente,nuevaDistancia)


def DrawGraphTable(Table):
    with open("Output.csv", "w") as f:
        f.write("f;t;w\n")
        for i in Table:
            line = ';'.join(map(str, i))
            f.write(line.rstrip(';') + '\n')
    subprocess.run("python3 ScriptReprGraf.py", shell=True)



A, B, C, D, E, F, H = 1, 2, 3, 4, 5, 6, 7
diccionario_variables = {"1": "A", "2":"B","3":"C","4":"D","5":"E","6":"F","7":"H"}
G = Grafo()

G.agregarVertice(A) #Claves A-H
G.agregarVertice(B)
G.agregarVertice(C)
G.agregarVertice(D)
G.agregarVertice(E)
G.agregarVertice(F)
G.agregarVertice(H)



G.agregarArista(A, H, 11) #De A a H con costo 11
G.agregarArista(A, C, 6) #De A a C con costo 6
G.agregarArista(B, E, 3) #De B a E con costo 3
G.agregarArista(C, B, 5) #De C a B con costo 5
G.agregarArista(C, F, 12) #De C a F con costo 12
G.agregarArista(D, C, 4) #De D a C con costo 4
G.agregarArista(D, A, 8) #De D a A con costo 8
G.agregarArista(D, B, 10) #De D a B con costo 10
G.agregarArista(D, F, 6) #De D a F con costo 6
G.agregarArista(E, F, 6) #De E a F con costo 6
G.agregarArista(H, E, 5) #De H a E con costo 5
G.agregarArista(H, D, 9) #De H a D con costo 9





for j in range(1, G.numVertices + 1):
    VerticeOrigen = j
    # Pongo a infinito todas las distancias de los vertices por iteracion.
    for k in range(1, G.numVertices + 1):
        G.listaVertices[k].dist = sys.maxsize
    print()
    dijkstra(G, G.obtenerVertice(VerticeOrigen))
    for i in range(1, G.numVertices + 1):
        origen = diccionario_variables[str(VerticeOrigen)]
        destino = diccionario_variables[str(i)]
        distancia = "inf" if G.listaVertices[i].dist > 10000 else G.listaVertices[i].dist
        print(f"Distancia mínima entre vértice {origen} y {destino}: {distancia}")


Tabla = G.Graph2Table()
DrawGraphTable(Tabla)
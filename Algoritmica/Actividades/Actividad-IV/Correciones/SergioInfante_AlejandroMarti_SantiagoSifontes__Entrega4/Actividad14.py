'''
14.  Utilizando el ejercicio 8, implementar el método decrementarClave en la clase MonticuloBinario para 
que funcione el alGoritmo de Dijkstra. Muestra cada paso al aplicar el alGoritmo de Dijkstra al Grafo 
resultante del problema 11.
'''
from AlxClass_Grafos import *
from AlxColaPrioridad import ColaPrioridad
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
    with open("Output.csv","w") as f:
        f.write("f;t;w\n")
        for i in Table:
            for j in i:
                f.write(str(j))
                f.write(';') if j != i[len(i)-1] else f.write('')
            f.write('\n')
    subprocess.run("python3 ScriptReprGraf.py", shell=True)



G = Grafo()

G.agregarVertice(1)
G.agregarVertice(2)
G.agregarVertice(3)
G.agregarVertice(4)
G.agregarVertice(5)
G.agregarVertice(6)


G.agregarArista(1, 2, 10)
G.agregarArista(1, 3, 15)
G.agregarArista(1, 6, 5 )
G.agregarArista(2, 3, 7 )
G.agregarArista(3, 4, 7 )
G.agregarArista(3, 6, 10)
G.agregarArista(4, 5, 7 )
G.agregarArista(6, 4, 5 )
G.agregarArista(5, 6, 13)


for j in range(1,G.numVertices+1):
    VerticeOrigen = j
    # Pongo a infinito todas las distancias de los vertices por iteracion.
    for k in range(1,G.numVertices+1):
        G.listaVertices[k].dist = sys.maxsize
    print()
    dijkstra(G,G.obtenerVertice(VerticeOrigen))
    for i in range(1,G.numVertices+1):
        print(f"Distancia minima entre Vertice {VerticeOrigen} a",\
            G.listaVertices[i].id,": ", "inf" if G.listaVertices[i].dist>100 else G.listaVertices[i].dist )

Tabla = G.Graph2Table()
DrawGraphTable(Tabla)
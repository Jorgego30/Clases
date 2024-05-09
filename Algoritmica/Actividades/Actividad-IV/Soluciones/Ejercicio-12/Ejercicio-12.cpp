#include <iostream>
#include "Class_DFSGrafos.hpp" // Asumiendo que la clase se encuentra en un archivo llamado DFSGraph.h

int main() {
    // Creamos un grafo dirigido
    DFSGraph grafo(true); // Indicamos que el grafo es direccional

    // Agregamos vértices
    grafo.addVertex(1);
    grafo.addVertex(2);
    grafo.addVertex(3);
    grafo.addVertex(4);
    grafo.addVertex(5);

    // Agregamos aristas
    grafo.addEdge(1, 2);
    grafo.addEdge(1, 3);
    grafo.addEdge(2, 4);
    grafo.addEdge(2, 5);
    grafo.addEdge(3, 4);
    grafo.addEdge(4, 5);

    // Realizamos el recorrido en profundidad (DFS)
    std::cout << "Recorrido en profundidad (DFS):" << std::endl;
    grafo.dfs();

    return 0;
}

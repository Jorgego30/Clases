#include <iostream>
#include "Class_grafos.hpp" // Suponiendo que Graph.hpp contiene la definición de la clase Graph

using namespace std;

int main()
{
    // Crear un grafo
    Graph g;

    // Agregar algunos vértices y aristas al grafo
    g.addEdge(1, 2);
    g.addEdge(2, 3);
    g.addEdge(3, 1);

    // Mostrar el grafo original
    cout << "Grafo original:\n" << g << endl;

    // Obtener el grafo transpuesto
    Graph transposed = g.transpose();

    // Mostrar el grafo transpuesto
    cout << "Grafo transpuesto:\n" << transposed << endl;

    return 0;
}

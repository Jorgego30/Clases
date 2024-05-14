/*
12.  Haciendo caso omiso de las ponderaciones, realiza una búsqueda en anchura en el grafo de la pregunta anterior.
*/

/*
MODIFICACIONES:
    -Creado un script para representar los grafos de C++ con Python (Se necesita instalar NetworkX y Pandas
    Puedes usar el siguiente comando en una terminal: pip install networkx pandas)
    -Modificado la funcion de BEA/BFS para enseñar los colores de los vertices/nodos por pantalla.
*/

#include "AlxClass_grafos_int_full.hpp"
#include <iostream>
#include <queue>
#include <cstdlib>
#include <fstream>
using namespace std;
void CppGraph2Py(vector<vector<int>> data)
{
    ofstream file("OutputwCol.csv");

    file << "f;" << "t;" << "w;" << "col" << endl;

    for (vector<int> i : data)
    {
        for (int j : i)
        {
            file << j;
            if (j != i[i.size() - 1])
                file << ";";
        }

        file << endl;
    }

    file.close();

    system("python3 ScriptReprGrafCol.py");
}


Graph bfs(Graph g, Vertex *start)
{
    start->dist = 0;
    start->pred = NULL;
    queue<Vertex *> vertQueue;
    vertQueue.push(start);
    while (vertQueue.size() > 0)
    {
        Vertex *currentVert = vertQueue.front();
        cout << "Visitando vertice: " << *currentVert << endl;
        vertQueue.pop();
        for (unsigned int nbr = 0; nbr < currentVert->getConnections().size();
             nbr++)
        {
            cout << "Color vertice: " << g.vertList[currentVert->getConnections()[nbr]].color << endl;

            if (g.vertList[currentVert->getConnections()[nbr]].color == 'w')
            {
                cout << "Marcamos como visitados: " << g.vertList[currentVert->getConnections()[nbr]] << endl;

                g.vertList[currentVert->getConnections()[nbr]].color = 'g';

                g.vertList[currentVert->getConnections()[nbr]].dist =
                    currentVert->dist + 1;
                g.vertList[currentVert->getConnections()[nbr]].pred =
                    currentVert;
                vertQueue.push(&g.vertList[currentVert->getConnections()[nbr]]);
            }
        }
        currentVert->color = 'b';
        vector<vector<int>> Vals = g.Graph2TableCol();
        CppGraph2Py(Vals);
    }

    return g;
}



int main()
{

    Graph g;

    g.addVertex(1);
    g.addVertex(2);
    g.addVertex(3);
    g.addVertex(4);
    g.addVertex(5);
    g.addVertex(6);

    g.addEdge(1, 2, 10);
    g.addEdge(1, 3, 15);
    g.addEdge(1, 6, 5);
    g.addEdge(2, 3, 7);
    g.addEdge(3, 4, 7);
    g.addEdge(3, 6, 10);
    g.addEdge(4, 5, 7);
    g.addEdge(6, 4, 5);
    g.addEdge(5, 6, 13);

    cout << endl
         << endl;

    Graph GBFS = bfs(g, g.getVertex(1));
    cout << "Fin del recorrido\n\n\n";

    return 1;
}
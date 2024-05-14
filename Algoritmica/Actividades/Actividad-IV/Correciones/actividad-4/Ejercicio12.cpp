//Haciendo caso omiso de las ponderaciones, realiza una búsqueda en anchura en el grafo de la pregunta
//anterior.


#include <iostream>
#include <map>
#include <vector>
#include <queue>
using namespace std;
#include "Class_grafos_int_full.hpp"

Graph bfs(Graph g, Vertex *start)
{
    start->dist = 0;
    start->pred = NULL;
    queue<Vertex *> vertQueue;
    vertQueue.push(start);
    while (vertQueue.size() > 0)
    {
        Vertex *currentVert = vertQueue.front();
        vertQueue.pop();
        for (unsigned int nbr = 0; nbr < currentVert->getConnections().size(); nbr++)
        {
            if (g.vertList[currentVert->getConnections()[nbr]].color == 'w')
            {

                cout<<"vertice actual -> "<<currentVert->getConnections()[nbr]<<endl;;   //Muestra el vertice e el que esta


                g.vertList[currentVert->getConnections()[nbr]].color = 'g';

                g.vertList[currentVert->getConnections()[nbr]].dist =
                    currentVert->dist + 1;
                g.vertList[currentVert->getConnections()[nbr]].pred =
                    currentVert;
                vertQueue.push(&g.vertList[currentVert->getConnections()[nbr]]);
            }
        }
        currentVert->color = 'b';
    }

    return g;
}

int main()
{
    Graph g ;

    for(int i=1;i<7;i++)
    {
        g.addVertex(i);
    }

    g.addEdge(1,2,10);
    g.addEdge(1,3,15);
    g.addEdge(1,6,5);
    g.addEdge(2,3,7);
    g.addEdge(3,4,7);
    g.addEdge(3,6,10);
    g.addEdge(4,5,7);
    g.addEdge(6,4,5);
    g.addEdge(5,6,13);


    Graph g2(false);

    cout<<"vertice actual -> 1"<<endl;      //Vertice desde el que se muestran las conexiones
    g2=bfs(g,g.getVertex(2));               //Aqui introducimos el vertice


    
}
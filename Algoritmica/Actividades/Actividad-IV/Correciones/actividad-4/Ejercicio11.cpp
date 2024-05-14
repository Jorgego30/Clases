//Crea el grafo correspondiente a la siguiente lista de aristas


#include <iostream>
#include <map>
#include "Class_grafos.hpp"
using namespace std;



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

    cout << g << endl;

    return 0;
}
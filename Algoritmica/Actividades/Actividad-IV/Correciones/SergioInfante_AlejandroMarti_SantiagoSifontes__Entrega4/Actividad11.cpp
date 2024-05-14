/*
11.  Crea el grafo correspondiente a la siguiente lista de aristas. 
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

void CppGraph2Py(vector<vector<int>> data) {
    ofstream file("Output.csv");

    file << "f;" << "t;" << "w" << endl;
    
    for (vector<int> i : data){
    for (int j : i){
        file << j;
        if (j != i[i.size()-1])
        file << ";";
    }

    file << endl;
    }

    file.close();

    system("python3 ScriptReprGraf.py");

}


int main(){
    Graph g;

    g.addVertex(1);
    g.addVertex(2);
    g.addVertex(3);
    g.addVertex(4);
    g.addVertex(5);
    g.addVertex(6);


    g.addEdge(1, 2, 10);
    g.addEdge(1, 3, 15);
    g.addEdge(1, 6, 5 );
    g.addEdge(2, 3, 7 );
    g.addEdge(3, 4, 7 );
    g.addEdge(3, 6, 10);
    g.addEdge(4, 5, 7 );
    g.addEdge(6, 4, 5 );
    g.addEdge(5, 6, 13);

    cout << g << endl;

    cout << endl << endl;

    vector<vector<int>> Tabla = g.Graph2Table();
    CppGraph2Py(Tabla);

    

    return 1;
}
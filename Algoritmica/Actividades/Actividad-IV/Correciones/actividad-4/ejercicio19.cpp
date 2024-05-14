//Escribe el método transponer para la clase Grafo

#include<iostream>
#include<vector>
#include<map>
using namespace std;

class Vertex
{
public:
    int id;
    map<int, int> connectedTo;

    Vertex()
    {
    }

    Vertex(int key)
    {
        id = key;
    }

    void addNeighbor(int nbr, int weight = 0)
    {
        connectedTo[nbr] = weight;
    }

    vector<int> getConnections()
    {
        vector<int> keys;
        for (map<int, int>::iterator it = connectedTo.begin(); it != connectedTo.end(); ++it)
        {
            keys.push_back(it->first);
        }
        return keys;
    }

    int getId()
    {
        return id;
    }

    int getWeight(int nbr)
    {
        return connectedTo[nbr];
    }

    friend ostream &operator<<(ostream &, Vertex &);
};

ostream &operator<<(ostream &stream, Vertex &vert)
{
    vector<int> connects = vert.getConnections();
    for (unsigned int i = 0; i < connects.size(); i++)
    {
        stream << "( " << vert.id << " , " << connects[i] << " ) \n";
    }

    return stream;
}

class Graph
{
public:
    map<int, Vertex> vertList;
    int numVertices;

    Graph()
    {
        numVertices = 0;
    }

    Vertex addVertex(int key)
    {
        numVertices++;
        Vertex newVertex = Vertex(key);
        this->vertList[key] = newVertex;
        return newVertex;
    }

    Vertex *getVertex(int n)
    {
        for (map<int, Vertex>::iterator it = vertList.begin(); it != vertList.end(); ++it)
        {
            if (it->first == n)
            {
                Vertex *vpntr = &vertList[n];
                return vpntr;
            }
        }
        return NULL;
    }

    bool contains(int n)
    {
        for (map<int, Vertex>::iterator it = vertList.begin(); it != vertList.end(); ++it)
        {
            if (it->first == n)
                return true;
        }
        return false;
    }

    void addEdge(int f, int t, int cost = 0)
    {
        if (!this->contains(f))
        {
            cout << f << " was not found, adding!" << endl;
            this->addVertex(f);
        }
        if (!this->contains(t))
            cout << t << " was not found, adding!" << endl;
        vertList[f].addNeighbor(t, cost);
    }

    vector<int> getVertices()
    {
        vector<int> verts;

        for (map<int, Vertex>::iterator it = vertList.begin(); it != vertList.end(); ++it)
            verts.push_back(it->first);
        return verts;
    }

    friend ostream &operator<<(ostream &, Graph &);
};

ostream &operator<<(ostream &stream, Graph &grph)
{
    for (map<int, Vertex>::iterator it = grph.vertList.begin(); it != grph.vertList.end(); ++it)
        stream << it->second;

    return stream;
}

int main()
{
    Graph graph;
    
    /*Este código crea un grafo con 4 vértices y agrega algunas aristas entre ellos. Luego, muestra los vértices y sus conexiones en la salida*/

    // Agregar vértices
    graph.addVertex(1);
    graph.addVertex(2);
    graph.addVertex(3);
    graph.addVertex(4);

    // Agregar aristas
    graph.addEdge(1, 2, 10);
    graph.addEdge(1, 3, 5);
    graph.addEdge(2, 3, 6);
    graph.addEdge(3, 4, 8);
    graph.addEdge(4, 1, 3);

    // Obtener todos los vértices
    vector<int> vertices = graph.getVertices();

    // Mostrar los vértices
    cout << "Vertices: ";
    for (int v : vertices) {
        cout << v << " ";
    }
    cout << endl;

    // Mostrar las conexiones de cada vértice
    cout << "Conexiones: " << endl;
    cout << graph;

    return 0;
}
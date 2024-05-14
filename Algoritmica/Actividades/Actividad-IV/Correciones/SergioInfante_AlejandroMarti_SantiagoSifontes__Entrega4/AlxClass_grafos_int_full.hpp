/*
=========================================================================================================
MODIFICACIONES:
    -Añadidos los metodos transponer (Act.19) y Graph2Table (Para sacar una tabla de conexiones y pesos)
=========================================================================================================
*/

#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

class Vertex
{
public:
    int id;
    map<int, float> connectedTo;
    // Added for Breadth-First Algorithm
    char color;
    float dist;
    Vertex *pred;

    Vertex()
    {
        // w for white, g for grey, b for black
        color = 'w';
        dist = 0;
        pred = NULL;
    }

    Vertex(int key)
    {
        id = key;
        color = 'w';
        dist = 0;
        pred = NULL;
    }

    void addNeighbor(int nbr, float weight = 1)
    {
        connectedTo[nbr] = weight;
    }

    vector<int> getConnections()
    {
        vector<int> keys;
        // Use of iterator to find all keys
        for (map<int, float>::iterator it = connectedTo.begin(); it != connectedTo.end(); ++it)
            keys.push_back(it->first);
        return keys;
    }

    int getId()
    {
        return id;
    }

    float getWeight(int nbr)
    {
        return connectedTo[nbr];
    }

    friend ostream &operator<<(ostream &, Vertex &);
};

ostream &operator<<(ostream &stream, Vertex &vert)
{
    vector<int> connects = vert.getConnections();
    stream << vert.id << " -> ";
    for (unsigned int i = 0; i < connects.size(); i++)
        stream << connects[i] << endl
               << "\t";

    return stream;
}

class Graph
{
public:
    map<int, Vertex> vertList;
    int numVertices;
    bool directional;

    Graph(bool directed = true)
    {
        directional = directed;
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
        return &vertList[n];
    }

    bool contains(int n)
    {
        for (map<int, Vertex>::iterator it = vertList.begin(); it != vertList.end(); ++it)
            if (it->first == n)
                return true;
        return false;
    }

    void addEdge(int f, int t, float cost = 1)
    {
        if (!this->contains(f))
            this->addVertex(f);
        if (!this->contains(t))
            this->addVertex(t);
        vertList[f].addNeighbor(t, cost);

        if (!directional)
            vertList[t].addNeighbor(f, cost);
    }

    vector<int> getVertices()
    {
        vector<int> verts;

        for (map<int, Vertex>::iterator it = vertList.begin(); it != vertList.end(); ++it)
            verts.push_back(it->first);
        return verts;
    }

    void trasponer(Vertex *x)
    {
        // Consigo las conexiones
        map<int, float> LinksRaw = x->connectedTo;
        vector<Vertex *> Links;
        for (auto &i : LinksRaw)
            Links.push_back(&vertList[i.first]);

        // Ahora cambio las asignaciones
        int IDOrigen = x->getId();
        for (auto &j : Links)
        {
            int IDDestino = j->getId();
            float peso = x->connectedTo[IDDestino];
            j->connectedTo[IDOrigen] = peso;
            cout << "ID Origen: " << IDOrigen << "\nID Destino: " << IDDestino << "\nPeso entre vertices: " << peso << "\nReasignacion: " << *j << endl;
            // Eliminamos los Edges que transpusimos
            vertList.erase(IDOrigen);
        }
    }

    vector<vector<int>> Graph2Table()
    {
        vector<vector<int>> Table;
        vector<int> Conex;
        for (auto &i : vertList)
        {
            int Origen = i.first; // Vertice origen
            for (auto &j : i.second.getConnections())
            {
                Conex.push_back(Origen);                  // Añadirmos el vertice de origen
                Conex.push_back(j);                       // Añadimos el vertice de destino
                Conex.push_back(i.second.connectedTo[j]); // Añadimos el peso entre ellos

                // Añadimos a la tabla:
                Table.push_back(Conex);
                Conex = {};
            }
        }

        return Table;
    }

    vector<vector<int>> Graph2TableCol()
    {
        vector<vector<int>> Table;
        vector<int> Conex;
        for (auto &i : vertList)
        {
            int Origen = i.first; // Vertice origen
            for (auto &j : i.second.getConnections())
            {
                Conex.push_back(Origen);                            // Añadirmos el vertice de origen
                Conex.push_back(j);                                 // Añadimos el vertice de destino
                Conex.push_back(i.second.connectedTo[j]);           // Añadimos el peso entre ellos
                int Col = static_cast<int>(i.second.color);
                Conex.push_back(Col);  // Añadimos el color del vertice origen

                // Añadimos a la tabla:
                Table.push_back(Conex);
                Conex = {};
            }
        }
        return Table;
    }

    friend ostream &operator<<(ostream &, Graph &);
};

ostream &operator<<(ostream &stream, Graph &grph)
{
    for (map<int, Vertex>::iterator it = grph.vertList.begin(); it != grph.vertList.end(); ++it)
    {
        stream << grph.vertList[it->first];
        cout << endl;
    }

    return stream;
}
#include <iostream>
#include <map>
#include <vector>

using namespace std;

class Vertex
{
public:
    int id;
    map<int, int> connectedTo;

    // Empty constructor.
    Vertex() {}

    // Constructor that defines the key of the vertex.
    Vertex(int key) : id(key) {}

    // Adds a neighbor to this vertex with the specified ID and weight.
    void addNeighbor(int nbr, int weight = 0)
    {
        connectedTo[nbr] = weight;
    }

    // Returns a vector (e.g., list) of vertices connected to this one.
    vector<int> getConnections() const
{
    vector<int> keys;
    for (auto it = connectedTo.begin(); it != connectedTo.end(); ++it)
    {
        keys.push_back(it->first);
    }
    return keys;
}

    // Returns the ID of this vertex.
    int getId() const
    {
        return id;
    }

    // Returns the weight of the connection between this vertex and the specified neighbor.
    int getWeight(int nbr) const
    {
        return connectedTo.at(nbr);
    }

    // Output stream overload operator for printing to the screen.
    friend ostream &operator<<(ostream &stream, const Vertex &vert);
};

ostream &operator<<(ostream &stream, const Vertex &vert)
{
    vector<int> connects = vert.getConnections();
    for (unsigned int i = 0; i < connects.size(); i++)
    {
        stream << "( " << vert.id << " , " << connects[i] << " ) \n";
    }

    return stream;
}

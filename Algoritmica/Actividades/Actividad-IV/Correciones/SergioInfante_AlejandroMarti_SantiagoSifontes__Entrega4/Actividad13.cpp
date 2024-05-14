/*
13.  ¿Cuál es el tiempo de ejecución O-grande de la función construirGrafo?
MODIFICACIONES:
    -Añadimos Ctime para haacer el benchmark y corroborar el resultado.
*/

#include <fstream>
#include <iostream>
#include <map>
#include <ctime>
#include <random>
#include "AlxClass_grafos_string.hpp"
using namespace std;

string getBlank(string str, int index)
{
    string blank = str;
    blank[index] = '_';
    return blank;
}

Graph buildGraph(vector<string> words)
{
    Graph g(false);

    map<string, vector<string>> d;

    // Go through the words
    for (unsigned int i = 0; i < words.size(); i++)
    {
        // Go through each letter, making it blank
        for (unsigned int j = 0; j < words[i].length(); j++)
        {
            string bucket = getBlank(words[i], j);
            // Add the word to the map at the location of the blank
            d[bucket].push_back(words[i]);
        }
    }

    for (map<string, vector<string>>::iterator iter = d.begin(); iter != d.end(); ++iter)
    {
        for (unsigned int i = 0; i < iter->second.size(); i++)
        {
            for (unsigned int j = 0; j < iter->second.size(); j++)
            {
                if (iter->second[i] != iter->second[j])
                {
                    g.addEdge(iter->second[i], iter->second[j]);
                }
            }
        }
    }

    return g;
}

vector<string> CrearArr(long size)
{
    vector<string> out = {};

    for (long i = 0; i < size; i++)
    {
        string letters = "";
        for (int j = 0; j < 5; j++)
        {
            letters += static_cast<char>(rand() % 26 + 97);
        }
        out.push_back(static_cast<string>(letters));
    }

    return out;
}

int main()
{
    cout << "Tiempo en segundos"<<endl;
    for (long i = 1000; i < 20001; i += 1000)
    {
        vector<string> words = CrearArr(i);

        clock_t start = clock();
        Graph g = buildGraph(words);
        clock_t stop = clock();

        
        cout << double(stop - start)/CLOCKS_PER_SEC << endl;
    }

    cout << "\nComo los tiempos van incrementando exponencialmente\npodemos decir que es O(n^2)\n";

    return 0;
}
#include <iostream>
#include <map>

using namespace std;

template<typename Map>
void PrintMap(Map& m)
{
    cout << "[ ";
    for (auto &item : m) {
        cout << item.first << ":" << item.second << " ";
    }
    cout << "]\n";
}
int busca(int v[], int x)
{
    for (int i = 0; i <= 1000; i++)
        if (i == x)
            return v[i];
    return -1;
}

int main() {
    map<int, string> map1 = {{1, "Apple",},
                                {2, "Banana",},
                                {3, "Mango",},
                                {4, "Raspberry",},
                                {5, "Blackberry",},
                                {6, "Cocoa",}};

    cout << "map1 - ";
    PrintMap(map1);
    cout << endl;

    return EXIT_SUCCESS;
}
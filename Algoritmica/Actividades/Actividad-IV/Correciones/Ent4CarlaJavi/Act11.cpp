#include <iostream>
#include <queue>
#include <utility>

using namespace std;

class PriorityQueue {
private:
    priority_queue<pair<string, int>, vector<pair<string, int>>, greater<pair<string, int>>> pq;

public:
    void agregar(string clave, int prioridad) {
        pq.push(make_pair(clave, prioridad));
    }

    pair<string, int> obtener_minimo() {
        pair<string, int> minimo = pq.top();
        pq.pop();
        return minimo;
    }

    bool esta_vacia() {
        return pq.empty();
    }
};

int main() {
    // Creamos una cola de prioridad
    PriorityQueue cola_prioridad;

    // Agregamos algunas tuplas (clave, prioridad)
    cola_prioridad.agregar("A", 10);
    cola_prioridad.agregar("B", 5);
    cola_prioridad.agregar("C", 15);
    cola_prioridad.agregar("D", 3);

    // Extraemos elementos y verificamos el orden
    cout << "Extracción de elementos en orden de prioridad:" << endl;
    while (!cola_prioridad.esta_vacia()) {
        pair<string, int> elemento = cola_prioridad.obtener_minimo();
        cout << "Clave: " << elemento.first << ", Prioridad: " << elemento.second << endl;
    }

    // Agregamos más elementos
    cola_prioridad.agregar("E", 20);
    cola_prioridad.agregar("F", 7);

    // Extraemos elementos nuevamente y verificamos el orden
    cout << "\nExtracción de elementos después de agregar más elementos:" << endl;
    while (!cola_prioridad.esta_vacia()) {
        pair<string, int> elemento = cola_prioridad.obtener_minimo();
        cout << "Clave: " << elemento.first << ", Prioridad: " << elemento.second << endl;
    }

    return 0;
}

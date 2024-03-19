/*Implementar el TAD Impresión usando Colas de Prioridad*/

#include <iostream>
#include <queue>
using namespace std;

// Definición de la estructura de datos para un trabajo de impresión
struct TrabajoImpresion {
    string nombre;
    int paginas;
    int prioridad;

    TrabajoImpresion(string n, int p, int pr) {
        nombre = n;
        paginas = p;
        prioridad = pr;
    }
};

// Función auxiliar para ordenar los trabajos de impresión por prioridad
struct OrdenPorPrioridad {
    bool operator()(const TrabajoImpresion& a, const TrabajoImpresion& b) {
        return a.prioridad < b.prioridad;
    }
};

// Definición del TAD Impresión utilizando una cola de prioridad
class Impresora {
private:
    priority_queue<TrabajoImpresion, vector<TrabajoImpresion>, OrdenPorPrioridad> cola;
public:
    void agregarTrabajo(TrabajoImpresion trabajo) {
        cola.push(trabajo);
    }

    void imprimir() {
        while (!cola.empty()) {
            TrabajoImpresion trabajo = cola.top();
            cola.pop();
            cout << "Imprimiendo " << trabajo.nombre << " (" << trabajo.paginas << " páginas)..." << endl;
        }
    }
};

int main() {
    // Crear una instancia de la clase Impresora
    Impresora impresora;

    // Agregar algunos trabajos de impresión a la cola
    impresora.agregarTrabajo(TrabajoImpresion("Tesis", 100, 1));
    impresora.agregarTrabajo(TrabajoImpresion("CV", 2, 2));
    impresora.agregarTrabajo(TrabajoImpresion("Contrato", 10, 1));
    impresora.agregarTrabajo(TrabajoImpresion("Presentación", 20, 3));

    // Imprimir los trabajos en orden de prioridad
    impresora.imprimir();

    return 0;
}
/*Actividad 15:

Implementa el método tamano (__len__) para la implementación del TAD Vector Asociativo o mapa de las
tablas hash, de manera que sea 𝑶(𝟏). 
*/


#include <iostream>
#include <unordered_map>
#include "Class_VectorAsociativo.hpp"
using namespace std;



int main() {
    // Ejemplo de uso
    VectorAsociativo<string, int> mi_mapa;
    mi_mapa.insertar("uno", 1);
    mi_mapa.insertar("dos", 2);
    mi_mapa.insertar("tres", 3);

    cout << "Tamaño del mapa: " << mi_mapa.tamano() << endl; // Imprime 3

    mi_mapa.eliminar("dos");

    cout << "Tamaño del mapa después de eliminar 'dos': " << mi_mapa.tamano() << endl; // Imprime 2

    return 0;
}

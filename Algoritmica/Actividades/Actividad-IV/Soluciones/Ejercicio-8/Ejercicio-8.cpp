#include <bits/stdc++.h>
#include "Class_Monticulos.hpp"

using namespace std;

int main() {
    // Creamos una instancia de ColaPrioridad
    ColaPrioridad cola_prioridad;

    // Agregamos elementos a la cola con su respectiva prioridad
    cola_prioridad.agregar("Tarea 1", 3);
    cola_prioridad.agregar("Tarea 2", 1);
    cola_prioridad.agregar("Tarea 3", 2);

    // Avanzamos en la cola y obtenemos los elementos en orden de prioridad
    cout << "Elementos en la cola de prioridad:" << endl;
    cout << cola_prioridad.avanzar() << endl; // Avanza y devuelve "Tarea 2" (prioridad 1)
    cout << cola_prioridad.avanzar() << endl; // Avanza y devuelve "Tarea 3" (prioridad 2)
    cout << cola_prioridad.avanzar() << endl; // Avanza y devuelve "Tarea 1" (prioridad 3)

    return 0;
}

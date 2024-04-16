/*Actividad 13:
Diseña un experimento aleatorio (Benchmark ) para probar la diferencia entre una búsqueda secuencial y
una búsqueda binaria, en todas sus variantes, en una lista de 200 enteros
*/


#include <iostream>
#include <vector>
#include <ctime>
#include <algorithm>

using namespace std;

#include <iostream>
#include <vector>
#include <ctime>
#include <algorithm>

using namespace std;

// Función para generar una lista de 200 enteros aleatorios y ordenarla
vector<int> generarLista() {
    vector<int> lista;
    for (int i = 0; i < 200; ++i) {
        lista.push_back(rand() % 1000); // Genera enteros aleatorios entre 0 y 999
    }
    sort(lista.begin(), lista.end()); // Ordena la lista
    return lista;
}

// Búsqueda secuencial
int busquedaSecuencial(const vector<int>& lista, int objetivo) {
    for (int i = 0; i < lista.size(); ++i) {
        if (lista[i] == objetivo) {
            return i; // Retorna la posición si encuentra el objetivo
        }
    }
    return -1; // Retorna -1 si no encuentra el objetivo
}

// Búsqueda binaria
int busquedaBinaria(const vector<int>& lista, int objetivo) {
    int izquierda = 0;
    int derecha = lista.size() - 1;
    while (izquierda <= derecha) {
        int medio = izquierda + (derecha - izquierda) / 2;
        if (lista[medio] == objetivo) {
            return medio; // Retorna la posición si encuentra el objetivo
        } else if (lista[medio] < objetivo) {
            izquierda = medio + 1;
        } else {
            derecha = medio - 1;
        }
    }
    return -1; // Retorna -1 si no encuentra el objetivo
}

int main() {
    srand(time(nullptr)); // Inicializa la semilla del generador de números aleatorios
    vector<int> lista = generarLista(); // Genera y ordena la lista de 200 enteros

    int objetivo = lista[rand() % lista.size()]; // Elige un valor aleatorio como objetivo

    clock_t inicio, fin;
    double tiempoSecuencial, tiempoBinaria;

    // Realiza la búsqueda secuencial y mide el tiempo de ejecución
    inicio = clock();
    int posicionSecuencial = busquedaSecuencial(lista, objetivo);
    fin = clock();
    tiempoSecuencial = double(fin - inicio) / CLOCKS_PER_SEC;

    // Realiza la búsqueda binaria y mide el tiempo de ejecución
    inicio = clock();
    int posicionBinaria = busquedaBinaria(lista, objetivo);
    fin = clock();
    tiempoBinaria = double(fin - inicio) / CLOCKS_PER_SEC;

    // Imprime los resultados
    cout << "Objetivo: " << objetivo << endl;
    cout << "Posición encontrada por búsqueda secuencial: " << posicionSecuencial << endl;
    cout << "Posición encontrada por búsqueda binaria: " << posicionBinaria << endl;
    cout << "Tiempo de búsqueda secuencial: " << tiempoSecuencial << " segundos" << endl;
    cout << "Tiempo de búsqueda binaria: " << tiempoBinaria << " segundos" << endl;

    return 0;
}

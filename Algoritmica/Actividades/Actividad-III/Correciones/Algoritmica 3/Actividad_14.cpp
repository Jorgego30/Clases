/*Actividad 14:

Utiliza todas las funciones de búsqueda binaria (recursiva e iterativa). Genera una lista ordenada aleatoria de
números enteros y realiza una prueba de referencia (Benchmark) para cada función. ¿Cuáles son sus
resultados? ¿Puedes explicarlos?
*/


#include <iostream>
#include <vector>
#include <ctime>
#include <algorithm>

using namespace std;

// Función para generar una lista de 'n' enteros aleatorios y ordenarla
vector<int> generarLista(int n) {
    vector<int> lista;
    for (int i = 0; i < n; ++i) {
        lista.push_back(rand() % 1000); // Genera enteros aleatorios entre 0 y 999
    }
    sort(lista.begin(), lista.end()); // Ordena la lista
    return lista;
}

// Búsqueda binaria recursiva
int busquedaBinariaRecursiva(const vector<int>& lista, int objetivo, int izquierda, int derecha) {
    if (izquierda <= derecha) {
        int medio = izquierda + (derecha - izquierda) / 2;
        if (lista[medio] == objetivo) {
            return medio; // Retorna la posición si encuentra el objetivo
        } else if (lista[medio] < objetivo) {
            return busquedaBinariaRecursiva(lista, objetivo, medio + 1, derecha);
        } else {
            return busquedaBinariaRecursiva(lista, objetivo, izquierda, medio - 1);
        }
    }
    return -1; // Retorna -1 si no encuentra el objetivo
}

// Búsqueda binaria iterativa
int busquedaBinariaIterativa(const vector<int>& lista, int objetivo) {
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
    vector<int> lista = generarLista(200); // Genera y ordena la lista de 200 enteros

    int objetivo = lista[rand() % lista.size()]; // Elige un valor aleatorio como objetivo

    clock_t inicio, fin;
    double tiempoRecursivo, tiempoIterativo;

    // Realiza la búsqueda binaria recursiva y mide el tiempo de ejecución
    inicio = clock();
    int posicionRecursiva = busquedaBinariaRecursiva(lista, objetivo, 0, lista.size() - 1);
    fin = clock();
    tiempoRecursivo = double(fin - inicio) / CLOCKS_PER_SEC;

    // Realiza la búsqueda binaria iterativa y mide el tiempo de ejecución
    inicio = clock();
    int posicionIterativa = busquedaBinariaIterativa(lista, objetivo);
    fin = clock();
    tiempoIterativo = double(fin - inicio) / CLOCKS_PER_SEC;

    // Imprime los resultados
    cout << "Objetivo: " << objetivo << endl;
    cout << "Posición encontrada por búsqueda binaria recursiva: " << posicionRecursiva << endl;
    cout << "Posición encontrada por búsqueda binaria iterativa: " << posicionIterativa << endl;
    cout << "Tiempo de búsqueda binaria recursiva: " << tiempoRecursivo << " segundos" << endl;
    cout << "Tiempo de búsqueda binaria iterativa: " << tiempoIterativo << " segundos" << endl;

    return 0;
}

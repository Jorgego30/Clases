#include <bits/stdc++.h>
#include "Class_Monticulos.hpp"
using namespace std;



vector<int> heap_sort(vector<int> lista) {
    // Crear un objeto de MonticuloBinario
    MonticuloBinario monticulo;

    // Construir un montículo a partir de la lista
    monticulo.construirMonticulo(lista);

    // Lista para almacenar los elementos ordenados
    vector<int> elementos_ordenados;

    // Extraer el mínimo del montículo y agregarlo a la lista de elementos ordenados
    for (size_t i = 0; i < lista.size(); i++) {
        elementos_ordenados.push_back(monticulo.eliminarMin());
    }

    return elementos_ordenados;
}

int main() {
    // Ejemplo de uso
    vector<int> lista_desordenada = {9, 5, 7, 2, 3, 6, 1, 8, 4};
    cout << "Lista original: ";
    for (int num : lista_desordenada) {
        cout << num << " ";
    }
    cout << endl;

    clock_t begin = clock();
    vector<int> lista_ordenada = heap_sort(lista_desordenada);
    clock_t end = clock();

    cout << "Lista ordenada: ";
    for (int num : lista_ordenada) {
        cout << num << " ";
    }
    cout << endl;

    double segundos = double(end - begin) / CLOCKS_PER_SEC;
    cout << fixed << endl;
    cout << "Tiempo de ordenación de la lista: " << segundos << " segundos" << endl;

    return 0;
}

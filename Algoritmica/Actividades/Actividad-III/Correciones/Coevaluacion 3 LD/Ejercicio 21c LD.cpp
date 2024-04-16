/******************************************************************************
Enunciado: Realiza una prueba de referencia (Benchmark) para un ordenamiento de Shell, utilizando diferentes
conjuntos de incrementos en la misma lista (los expresados en los apuntes y dos más…).
*******************************************************************************/
#include <iostream>
#include <vector>
#include <chrono> // Para medir el tiempo

// Función para el ordenamiento de Shell
void shellSort(std::vector<int>& arr, std::vector<int>& gaps) {
    int n = arr.size();
    for (int gap : gaps) { // Iteramos sobre los diferentes conjuntos de incrementos
        for (int i = gap; i < n; i += 1) {
            int temp = arr[i];
            int j;
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap)
                arr[j] = arr[j - gap];
            arr[j] = temp;
        }
    }
}

int main() {
    // Definimos diferentes conjuntos de incrementos
    std::vector<std::vector<int>> incrementos = {{5, 3, 1}, {4, 2, 1}, {6, 3, 1}, {7, 4, 2, 1}};

    // Creamos una lista de prueba
    std::vector<int> lista = {9, 8, 7, 6, 5, 4, 3, 2, 1};

    // Realizamos la prueba de referencia para cada conjunto de incrementos
    for (auto& gaps : incrementos) {
        auto start = std::chrono::high_resolution_clock::now(); // Inicio del tiempo
        shellSort(lista, gaps); // Ordenamos la lista
        auto end = std::chrono::high_resolution_clock::now(); // Fin del tiempo

        // Calculamos e imprimimos el tiempo transcurrido
        std::chrono::duration<double> elapsed = end - start;
        std::cout << "Tiempo transcurrido con incrementos ";
        for (int gap : gaps) std::cout << gap << " ";
        std::cout << ": " << elapsed.count() << " segundos.\n";
    }

    return 0;
}

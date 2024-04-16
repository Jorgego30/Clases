/******************************************************************************
Enunciado: Utiliza todas las funciones de búsqueda binaria (recursiva e iterativa). Genera una lista ordenada aleatoria de
números enteros y realiza una prueba de referencia (Benchmark) para cada función. ¿Cuáles son sus
resultados? ¿Puedes explicarlos?

Resultados:
Búsqueda binaria recursiva: 3.579e-06 s
Búsqueda binaria iterativa: 6.6e-07 s
La búsqueda binaria iterativa fue más rápida que la recursiva en tu prueba. La iterativa evita la sobrecarga de las llamadas 
a funciones que ocurre en la recursiva. La diferencia de tiempo puede ser más notable para listas muy grandes.

*******************************************************************************/
#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <random>

// Búsqueda binaria recursiva
int binary_search_recursive(const std::vector<int>& vec, int start, int end, int key) {
    if (start <= end) {
        int mid = start + (end - start) / 2;
        if (vec[mid] == key)
            return mid;
        if (vec[mid] > key)
            return binary_search_recursive(vec, start, mid - 1, key);
        return binary_search_recursive(vec, mid + 1, end, key);
    }
    return -1;
}

// Búsqueda binaria iterativa
int binary_search_iterative(const std::vector<int>& vec, int key) {
    int start = 0, end = vec.size() - 1;
    while (start <= end) {
        int mid = start + (end - start) / 2;
        if (vec[mid] == key)
            return mid;
        if (vec[mid] < key)
            start = mid + 1;
        else
            end = mid - 1;
    }
    return -1;
}

int main() {
    std::vector<int> vec(1000000);
    std::iota(vec.begin(), vec.end(), 0); // Genera números de 0 a 999999

    // Barajamos el vector
    std::random_device rd;
    std::mt19937 g(rd());
    std::shuffle(vec.begin(), vec.end(), g);

    // Ordenamos el vector
    std::sort(vec.begin(), vec.end());

    int key = 123456; // Número a buscar

    // Prueba de referencia para la búsqueda binaria recursiva
    auto start = std::chrono::high_resolution_clock::now();
    int result = binary_search_recursive(vec, 0, vec.size() - 1, key);
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> diff = end - start;
    std::cout << "Búsqueda binaria recursiva: " << diff.count() << " s\n";

    // Prueba de referencia para la búsqueda binaria iterativa
    start = std::chrono::high_resolution_clock::now();
    result = binary_search_iterative(vec, key);
    end = std::chrono::high_resolution_clock::now();
    diff = end - start;
    std::cout << "Búsqueda binaria iterativa: " << diff.count() << " s\n";

    return 0;
}

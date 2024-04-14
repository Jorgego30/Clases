#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <random>

using namespace std;
using namespace std::chrono;

// Función para generar una lista aleatoria de tamaño 'size' con enteros en el rango [1, 1000]
vector<int> vectorAleatorio(int size){
    vector<int> vector (size);
    for (int i=0; i<size; i++){
        vector [i] = rand()%1000;
    }
    return vector;
}
// Función para realizar una búsqueda secuencial en una lista
int sequentialSearch(const vector<int>& arr, int target) {
    for (int i = 0; i < arr.size(); ++i) {
        if (arr[i] == target) {
            return i; // Devuelve el índice si se encuentra el elemento
        }
    }
    return -1; // Devuelve -1 si el elemento no está presente
}

// Función para realizar una búsqueda binaria en una lista ordenada
int binarySearch(const vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) {
            return mid; // Devuelve el índice si se encuentra el elemento
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1; // Devuelve -1 si el elemento no está presente
}

int main() {
    srand (time(NULL));

    // Generar una lista aleatoria de 200 enteros
    vector<int> randomList = vectorAleatorio(200);

    // Ordenar la lista para permitir la búsqueda binaria
    sort(randomList.begin(), randomList.end());

    // Elemento a buscar
    int target = randomList[rand() % 200]; // Selecciona un elemento aleatorio de la lista

    // Benchmark para la búsqueda secuencial
    clock_t begin = clock();
    int seqResult = sequentialSearch(randomList, target);
    clock_t end = clock();
    double segundos = double(end - begin) / CLOCKS_PER_SEC;
    // Benchmark para la búsqueda binaria
    clock_t begin1 = clock();
    int binResult = binarySearch(randomList, target);
    clock_t end1 = clock();
    double segundosBin = double(end1 - begin1) / CLOCKS_PER_SEC;

    // Imprimir los resultados
    cout << "Elemento buscado: " << target << endl;
    cout << "Índice encontrado por búsqueda secuencial: " << seqResult << endl;
    cout << "Índice encontrado por búsqueda binaria: " << binResult << endl;
    cout << fixed << "Tiempo de búsqueda secuencial: " << segundos << " segundos" << endl;
    cout << fixed << "Tiempo de búsqueda binaria: " << segundosBin << " segundos" << endl;

    return 0;
}

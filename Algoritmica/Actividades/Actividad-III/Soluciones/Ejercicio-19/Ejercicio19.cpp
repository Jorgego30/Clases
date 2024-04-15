#include <iostream>
#include <vector>
#include <random>
#include <ctime>

using namespace std;

// Función para generar una lista de enteros aleatorios
vector<int> generarListaAleatoria(int n) {
    vector<int> lista;
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 1000);
    for (int i = 0; i < n; ++i) {
        lista.push_back(dis(gen));
    }
    return lista;
}

// Implementación del algoritmo de ordenamiento burbuja
void bubbleSort(vector<int>& lista) {
    int n = lista.size();
    for (int i = 0; i < n - 1; ++i) {
        for (int j = 0; j < n - i - 1; ++j) {
            if (lista[j] > lista[j + 1]) {
                swap(lista[j], lista[j + 1]);
            }
        }
    }
}

// Implementación del algoritmo de ordenamiento por inserción
void insertionSort(vector<int>& lista) {
    int n = lista.size();
    for (int i = 1; i < n; ++i) {
        int key = lista[i];
        int j = i - 1;
        while (j >= 0 && lista[j] > key) {
            lista[j + 1] = lista[j];
            --j;
        }
        lista[j + 1] = key;
    }
}

// Implementación del algoritmo de ordenamiento por Shell
void shellSort(vector<int>& lista) {
    int n = lista.size();
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; ++i) {
            int temp = lista[i];
            int j;
            for (j = i; j >= gap && lista[j - gap] > temp; j -= gap) {
                lista[j] = lista[j - gap];
            }
            lista[j] = temp;
        }
    }
}

// Función para medir el tiempo de ejecución de un algoritmo de ordenamiento
double medirTiempoOrdenamiento(void(*algoritmo)(vector<int>&), vector<int>& lista) {
    clock_t inicio = clock();
    algoritmo(lista);
    clock_t fin = clock();
    return double(fin - inicio) / CLOCKS_PER_SEC;
}

int main() {
    // Generar una lista de 500 enteros aleatorios
    vector<int> listaAleatoria = generarListaAleatoria(500);

    // Copiar la lista aleatoria para cada algoritmo de ordenamiento
    vector<int> listaBubbleSort = listaAleatoria;
    vector<int> listaInsertionSort = listaAleatoria;
    vector<int> listaShellSort = listaAleatoria;

    // Medir el tiempo de ejecución de cada algoritmo
    cout << "Ordenamiento Burbuja: " << medirTiempoOrdenamiento(bubbleSort, listaBubbleSort) << " segundos" << endl;
    cout << "Ordenamiento por Insercion: " << medirTiempoOrdenamiento(insertionSort, listaInsertionSort) << " segundos" << endl;
    cout << "Ordenamiento por Shell: " << medirTiempoOrdenamiento(shellSort, listaShellSort) << " segundos" << endl;

    return 0;
}

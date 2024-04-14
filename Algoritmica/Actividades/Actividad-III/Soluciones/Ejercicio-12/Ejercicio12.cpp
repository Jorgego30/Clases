#include <bits/stdc++.h>
using namespace std;

// Función para imprimir un vector
void printVector(const vector<int>& vec) {
    for (int num : vec) {
        cout << num << " ";
    }
    cout << endl;
}

// Genera una lista aleatoria de números enteros
vector<int> generateRandomList(int size) {
    vector<int> randomList;
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, 100); // Números entre 1 y 100
    for (int i = 0; i < size; ++i) {
        randomList.push_back(dis(gen));
    }
    return randomList;
}

// Algoritmo de ordenamiento burbuja
void bubbleSort(vector<int>& vec) {
    int n = vec.size();
    for (int i = 0; i < n-1; ++i) {
        for (int j = 0; j < n-i-1; ++j) {
            if (vec[j] > vec[j+1]) {
                swap(vec[j], vec[j+1]);
            }
        }
    }
}

// Algoritmo de ordenamiento por selección
void selectionSort(vector<int>& vec) {
    int n = vec.size();
    for (int i = 0; i < n-1; ++i) {
        int min_idx = i;
        for (int j = i+1; j < n; ++j) {
            if (vec[j] < vec[min_idx]) {
                min_idx = j;
            }
        }
        swap(vec[i], vec[min_idx]);
    }
}

// Algoritmo de ordenamiento por inserción
void insertionSort(vector<int>& vec) {
    int n = vec.size();
    for (int i = 1; i < n; ++i) {
        int key = vec[i];
        int j = i - 1;
        while (j >= 0 && vec[j] > key) {
            vec[j+1] = vec[j];
            --j;
        }
        vec[j+1] = key;
    }
}

int main() {
    vector<int> randomList = generateRandomList(10);
    cout << "Lista aleatoria generada: ";
    printVector(randomList);

    // Ordenamiento burbuja
    vector<int> bubbleSorted = randomList;
    bubbleSort(bubbleSorted);
    cout << "Ordenamiento burbuja: ";
    printVector(bubbleSorted);

    // Ordenamiento por selección
    vector<int> selectionSorted = randomList;
    selectionSort(selectionSorted);
    cout << "Ordenamiento por selección: ";
    printVector(selectionSorted);

    // Ordenamiento por inserción
    vector<int> insertionSorted = randomList;
    insertionSort(insertionSorted);
    cout << "Ordenamiento por inserción: ";
    printVector(insertionSorted);

    return 0;
}

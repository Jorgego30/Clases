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

// Algoritmo de ordenamiento de Shell
void shellSort(vector<int>& vec) {
    int n = vec.size();
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; ++i) {
            int temp = vec[i];
            int j;
            for (j = i; j >= gap && vec[j - gap] > temp; j -= gap) {
                vec[j] = vec[j - gap];
            }
            vec[j] = temp;
        }
    }
}

// Función auxiliar para el ordenamiento por mezcla
void merge(vector<int>& vec, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    vector<int> L(n1), R(n2);

    for (int i = 0; i < n1; ++i) {
        L[i] = vec[left + i];
    }
    for (int j = 0; j < n2; ++j) {
        R[j] = vec[mid + 1 + j];
    }

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            vec[k] = L[i];
            ++i;
        } else {
            vec[k] = R[j];
            ++j;
        }
        ++k;
    }

    while (i < n1) {
        vec[k] = L[i];
        ++i;
        ++k;
    }

    while (j < n2) {
        vec[k] = R[j];
        ++j;
        ++k;
    }
}

// Algoritmo de ordenamiento por mezcla
void mergeSort(vector<int>& vec, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        mergeSort(vec, left, mid);
        mergeSort(vec, mid + 1, right);

        merge(vec, left, mid, right);
    }
}

// Función auxiliar para elegir el pivote en el ordenamiento rápido
int choosePivot(vector<int>& vec, int left, int right) {
    return vec[left]; // En este ejemplo, elegimos siempre el primer elemento como pivote
}

// Algoritmo de ordenamiento rápido
void quickSort(vector<int>& vec, int left, int right) {
    if (left < right) {
        int pivot = choosePivot(vec, left, right);
        int i = left, j = right;

        while (i <= j) {
            while (vec[i] < pivot) {
                ++i;
            }
            while (vec[j] > pivot) {
                --j;
            }
            if (i <= j) {
                swap(vec[i], vec[j]);
                ++i;
                --j;
            }
        }

        quickSort(vec, left, j);
        quickSort(vec, i, right);
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

    // Ordenamiento de Shell
    vector<int> shellSorted = randomList;
    shellSort(shellSorted);
    cout << "Ordenamiento de Shell: ";
    printVector(shellSorted);

    // Ordenamiento por mezcla
    vector<int> mergeSorted = randomList;
    mergeSort(mergeSorted, 0, mergeSorted.size() - 1);
    cout << "Ordenamiento por mezcla: ";
    printVector(mergeSorted);

    // Ordenamiento rápido
    vector<int> quickSorted = randomList;
    quickSort(quickSorted, 0, quickSorted.size() - 1);
    cout << "Ordenamiento rápido: ";
    printVector(quickSorted);

    return 0;
}

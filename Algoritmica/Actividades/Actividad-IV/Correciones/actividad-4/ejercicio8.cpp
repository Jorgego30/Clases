//Utilizando la clase MonticuloBinario, implementa una nueva clase llamada ColaPrioridad. Esta nueva
//clase ColaPrioridad debe implementar el constructor, además de los métodos agregar y avanzar

//IMplementamos las librerias necesarias 

#include <iostream>
#include <vector>

using namespace std;

//Clase necesaria 

class MonticuloBinario {
private:
    vector<int> heap;

    int parent(int i) {
        return (i - 1) / 2;
    }

    int leftChild(int i) {
        return 2 * i + 1;
    }

    int rightChild(int i) {
        return 2 * i + 2;
    }

    void swap(int& a, int& b) {
        int temp = a;
        a = b;
        b = temp;
    }

    void heapifyUp(int i) {
        while (i != 0 && heap[i] > heap[parent(i)]) {
            swap(heap[i], heap[parent(i)]);
            i = parent(i);
        }
    }

    void heapifyDown(int i) {
        int left = leftChild(i);
        int right = rightChild(i);
        int largest = i;

        if (left < heap.size() && heap[left] > heap[largest]) {
            largest = left;
        }

        if (right < heap.size() && heap[right] > heap[largest]) {
            largest = right;
        }

        if (largest != i) {
            swap(heap[i], heap[largest]);
            heapifyDown(largest);
        }
    }

public:
    MonticuloBinario() {}

    void insert(int item) {
        heap.push_back(item);
        heapifyUp(heap.size() - 1);
    }

    int extractMax() {
        if (heap.empty()) {
            return -1;
        }

        int maxItem = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        heapifyDown(0);

        return maxItem;
    }
};

class ColaPrioridad {
private:
    MonticuloBinario heap;

public:
    ColaPrioridad() {}

    void agregar(int item) {
        heap.insert(item);
    }

    int avanzar() {
        return heap.extractMax();
    }
};


//Programa principal encargdo de mostrar por panttalla los resultados
int main() {
    ColaPrioridad cola;

    cola.agregar(5);
    cola.agregar(10);
    cola.agregar(3);
    cola.agregar(8);

//Mostramos por terminal los resultados 
    cout << cola.avanzar() << endl;  
    cout << cola.avanzar() << endl;  
    cout << cola.avanzar() << endl;  
    cout << cola.avanzar() << endl;  
    return 0;
}
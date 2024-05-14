//7. Implementa un montículo binario como un montículo máx. 
#include "MonticuloBinario.h"

void MonticuloBinario::heapify(int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < heap.size() && heap[left] > heap[largest])
        largest = left;

    if (right < heap.size() && heap[right] > heap[largest])
        largest = right;

    if (largest != i) {
        swap(heap[i], heap[largest]);
        heapify(largest);
    }
}

void MonticuloBinario::swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

void MonticuloBinario::insert(int key) {
    heap.push_back(key);
    int i = heap.size() - 1;
    while (i > 0 && heap[(i - 1) / 2] < heap[i]) {
        swap(heap[i], heap[(i - 1) / 2]);
        i = (i - 1) / 2;
    }
}

int MonticuloBinario::extractMax() {
    if (heap.empty())
        return -1; // Indicador de que el montículo está vacío

    int maxElement = heap[0];
    heap[0] = heap.back();
    heap.pop_back();
    heapify(0);
    return maxElement;
}

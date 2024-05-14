#include <iostream>
#include <vector>

class Heap {
private:
    std::vector<int> heap;

    void descend(int index, int length) {
        int left = 2 * index + 1;
        int right = 2 * index + 2;
        int largest = index;

        if (left < length && heap[left] > heap[largest]) {
            largest = left;
        }
        if (right < length && heap[right] > heap[largest]) {
            largest = right;
        }

        if (largest != index) {
            std::swap(heap[index], heap[largest]);
            descend(largest, length);
        }
    }

    void buildHeap(std::vector<int>& list) {
        int n = list.size();
        heap = list;
        for (int i = n / 2 - 1; i >= 0; i--) {
            descend(i, n);
        }
    }

public:
    std::vector<int> heapSort(std::vector<int>& list) {
        buildHeap(list);
        int n = list.size();
        for (int i = n - 1; i > 0; i--) {
            std::swap(list[i], list[0]);
            descend(0, i);
        }
        return list;
    }
};

int main() {
    Heap heap;

    std::vector<int> lista = {12, 11, 13, 5, 6, 7};

    std::cout << "Lista original: ";
    for (int num : lista) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    std::vector<int> lista_ordenada = heap.heapSort(lista);

    std::cout << "Lista ordenada: ";
    for (int num : lista_ordenada) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}

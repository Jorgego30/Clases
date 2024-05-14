#include <vector>

class Heap {
private:
    std::vector<int> heap;

    void descender(int indice, int longitud) {
        int izquierda = 2 * indice + 1;
        int derecha = 2 * indice + 2;
        int mayor = indice;

        if (izquierda < longitud && heap[izquierda] > heap[mayor]) {
            mayor = izquierda;
        }
        if (derecha < longitud && heap[derecha] > heap[mayor]) {
            mayor = derecha;
        }

        if (mayor != indice) {
            std::swap(heap[indice], heap[mayor]);
            descender(mayor, longitud);
        }
    }

public:
    void construirMonticulo(std::vector<int>& lista) {
        int n = lista.size();
        heap = lista;
        for (int i = n / 2 - 1; i >= 0; i--) {
            descender(i, n);
        }
    }

    std::vector<int> heapSort(std::vector<int>& lista) {
        construirMonticulo(lista);
        int n = lista.size();
        for (int i = n - 1; i > 0; i--) {
            std::swap(lista[i], lista[0]);
            descender(0, i);
        }
        return lista;
    }
};

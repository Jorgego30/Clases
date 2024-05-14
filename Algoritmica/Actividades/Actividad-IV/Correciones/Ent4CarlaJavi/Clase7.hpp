//7. Implementa un montículo binario como un montículo máx. 
#ifndef MONTICULO_BINARIO_H
#define MONTICULO_BINARIO_H

#include <vector>

class MonticuloBinario {
private:
    std::vector<int> heap;

    void heapify(int i);
    void swap(int& a, int& b);

public:
    void insert(int key);
    int extractMax();
};

#endif

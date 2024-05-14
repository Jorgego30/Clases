//7. Implementa un montículo binario como un montículo máx. 
#include <iostream>
#include "Clase7.hpp"

int main() {
    MonticuloBinario heap;
    heap.insert(10);
    heap.insert(20);
    heap.insert(15);
    heap.insert(30);
    heap.insert(40);

    std::cout << "Elemento máximo extraído: " << heap.extractMax() << std::endl;

    return 0;
}

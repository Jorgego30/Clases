/*Escribe una función recursiva para invertir una lista enlazada.*/

struct Nodo {
    int valor;
    Nodo* siguiente;
};

Nodo* invertirLista(Nodo* cabeza) {
    if (cabeza == nullptr || cabeza->siguiente == nullptr) {
        return cabeza;
    }
    Nodo* resto = invertirLista(cabeza->siguiente);
    cabeza->siguiente->siguiente = cabeza;
    cabeza->siguiente = nullptr;
    return resto;
}


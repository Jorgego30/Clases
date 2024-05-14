#include <iostream>

class MaxHeap {
private:
    int *arr;
    int capacidad;
    int tamano;

public:
    MaxHeap(int capacidad);
    ~MaxHeap();

    int obtenerTamano();
    int padre(int hijo);
    int izquierda(int padre);
    int derecha(int padre);
    void filtrarArriba(int i);
    void insertar(int k);
    int obtenerMax();
    bool esHoja(int i);
    void filtrarAbajo(int i);
    int extraerMax();
    void construirMonticulo(int *arr, int len);
    int eliminarEn(int k);
};

MaxHeap::MaxHeap(int capacidad) {
    this->capacidad = capacidad;
    arr = new int[capacidad];
    tamano = 0;
}

MaxHeap::~MaxHeap() {
    delete[] arr;
}

int MaxHeap::obtenerTamano() {
    return tamano;
}

int MaxHeap::padre(int hijo) {
    if (hijo % 2 == 0)
        return (hijo / 2) - 1;
    else
        return (hijo / 2);
}

int MaxHeap::izquierda(int padre) {
    return (2 * padre + 1);
}

int MaxHeap::derecha(int padre) {
    return (2 * padre + 2);
}

void MaxHeap::filtrarArriba(int i) {
    if (i == 0)
        return; // solo un elemento en el arr
      
    int indice_padre = padre(i); // obtener el índice del padre 
  
    if (arr[indice_padre] < arr[i]) {
        int temp = arr[indice_padre]; // si el valor en el índice del padre es menor que el valor insertado
        arr[indice_padre] = arr[i];   // intercambiar los valores
        arr[i] = temp;
        filtrarArriba(indice_padre);  // repetir hasta que se satisfaga la relación de montículo máximo entre padre e hijo
    }
}

void MaxHeap::insertar(int k) {
    arr[tamano] = k; // insertar el valor en el arr
    filtrarArriba(tamano);
    tamano++;         // incrementar el tamaño del arr
    for (int i = 0; i < tamano; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

int MaxHeap::obtenerMax() {
    for (int i = 0; i < tamano; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    return arr[0]; // el valor máximo estará en el índice 0
}

bool MaxHeap::esHoja(int i) {
    if (i >= tamano)
        return true;
    return false;
}

void MaxHeap::filtrarAbajo(int i) {
    int l = izquierda(i);
    int r = derecha(i);
    
    if (esHoja(l))
        return;
    
    int indiceMax = i;
    if (arr[l] > arr[i]) {
        indiceMax = l;
    }
    
    if (!esHoja(r) && (arr[r] > arr[indiceMax])) {
        indiceMax = r;
    }
    
    if (indiceMax != i) {
        int temp = arr[i];
        arr[i] = arr[indiceMax];
        arr[indiceMax] = temp;
        filtrarAbajo(indiceMax);
    }
}

int MaxHeap::extraerMax() {
    int maximo = arr[0];
    arr[0] = arr[tamano - 1];
    tamano--;
    filtrarAbajo(0);
    return maximo;
}

void MaxHeap::construirMonticulo(int *arr, int len) {
    tamano = len;
    arr = arr;
  
    for (int i = tamano - 1; i >= 0; --i) {
        filtrarAbajo(i);
    }
}

int MaxHeap::eliminarEn(int k) {
    int r = arr[k];
    arr[k] = arr[tamano - 1]; // reemplazar con la hoja más a la derecha 
    tamano--;
    int p = padre(k);
    if (k == 0 || arr[k] < arr[p])
        filtrarAbajo(k);
    else
        filtrarArriba(k);
    return r;   
}

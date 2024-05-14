#include <iostream>
#include <vector>

using namespace std;

class MonticuloMaximo {
private:
    vector<int> listaMonticulo;
    int tamanoActual;

    void flotar_arriba(int i) {
        while (i / 2 > 0) {
            if (listaMonticulo[i] > listaMonticulo[i / 2]) {
                // Intercambiar los elementos
                swap(listaMonticulo[i], listaMonticulo[i / 2]);
            }
            i = i / 2;
        }
    }

    void hundir_abajo(int i) {
        while (i * 2 <= tamanoActual) {
            int max_hijo = hijo_maximo(i);
            if (listaMonticulo[i] < listaMonticulo[max_hijo]) {
                // Intercambiar los elementos
                swap(listaMonticulo[i], listaMonticulo[max_hijo]);
            }
            i = max_hijo;
        }
    }

    int hijo_maximo(int i) {
        int hijo_izquierdo = i * 2;
        int hijo_derecho = i * 2 + 1;
        if (hijo_derecho <= tamanoActual && listaMonticulo[hijo_derecho] > listaMonticulo[hijo_izquierdo]) {
            return hijo_derecho;
        } else {
            return hijo_izquierdo;
        }
    }

public:
    MonticuloMaximo() {
        listaMonticulo.push_back(0); // Agregar un elemento ficticio en el índice 0
        tamanoActual = 0;
    }

    void insertar(int k) {
        listaMonticulo.push_back(k);
        tamanoActual++;
        flotar_arriba(tamanoActual);
    }

    int eliminar_maximo() {
        int maximo = listaMonticulo[1];
        listaMonticulo[1] = listaMonticulo[tamanoActual];
        tamanoActual--;
        listaMonticulo.pop_back();
        hundir_abajo(1);
        return maximo;
    }

    void construir_monticulo(vector<int> una_lista) {
        tamanoActual = una_lista.size();
        listaMonticulo = vector<int>(tamanoActual + 1);
        for (int j = 0; j < tamanoActual; j++) {
            listaMonticulo[j + 1] = una_lista[j];
        }
        for (int i = tamanoActual / 2; i > 0; i--) {
            hundir_abajo(i);
        }
    }

    int getTamanoActual() const {
        return tamanoActual;
    }

    friend void imprimir_monticulo_maximo(const MonticuloMaximo& monticulo);
};

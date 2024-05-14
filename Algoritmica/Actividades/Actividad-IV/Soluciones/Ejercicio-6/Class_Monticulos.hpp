#include <vector>

using namespace std;

class MonticuloBinario {
private:
    vector<int> listaMonticulo;
    int tamanoActual;

    void infiltArriba(int i) {
        while (i / 2 > 0) {
            if (listaMonticulo[i] < listaMonticulo[i / 2]) {
                // Intercambiar los elementos
                swap(listaMonticulo[i / 2], listaMonticulo[i]);
            }
            i = i / 2;
        }
    }

    void infiltAbajo(int i) {
        while (i * 2 <= tamanoActual) {
            int hm = hijoMin(i);
            if (listaMonticulo[i] > listaMonticulo[hm]) {
                // Intercambiar los elementos
                swap(listaMonticulo[i], listaMonticulo[hm]);
            }
            i = hm;
        }
    }

    int hijoMin(int i) {
        if (i * 2 + 1 > tamanoActual) {
            return i * 2;
        } else {
            if (listaMonticulo[i * 2] < listaMonticulo[i * 2 + 1]) {
                return i * 2;
            } else {
                return i * 2 + 1;
            }
        }
    }

public:
    MonticuloBinario() {
        listaMonticulo = {0};
        tamanoActual = 0;
    }

    void insertar(int k) {
        listaMonticulo.push_back(k);
        tamanoActual++;
        infiltArriba(tamanoActual);
    }

    int eliminarMin() {
        int valorSacado = listaMonticulo[1];
        listaMonticulo[1] = listaMonticulo[tamanoActual];
        tamanoActual--;
        listaMonticulo.pop_back();
        infiltAbajo(1);
        return valorSacado;
    }

    void construirMonticulo(vector<int> unaLista) {
        int i = unaLista.size() / 2;
        tamanoActual = unaLista.size();
        listaMonticulo = vector<int>(tamanoActual + 1);
        for (int j = 0; j < unaLista.size(); j++) {
            listaMonticulo[j + 1] = unaLista[j];
        }
        while (i > 0) {
            infiltAbajo(i);
            i--;
        }
    }
};

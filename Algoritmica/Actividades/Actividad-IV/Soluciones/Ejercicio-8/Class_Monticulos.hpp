#include <bits/stdc++.h>

using namespace std;

// Definición de la clase MonticuloBinario
class MonticuloBinario {
private:
    vector<pair<int, string>> listaMonticulo; // Utilizamos un vector de pares para almacenar el elemento y su prioridad
    int tamanoActual;

    void flotar_arriba(int i) {
        while (i / 2 > 0) {
            if (listaMonticulo[i].first < listaMonticulo[i / 2].first) {
                swap(listaMonticulo[i], listaMonticulo[i / 2]);
            }
            i = i / 2;
        }
    }

    void hundir_abajo(int i) {
        while (i * 2 <= tamanoActual) {
            int hm = hijo_min(i);
            if (listaMonticulo[i].first > listaMonticulo[hm].first) {
                swap(listaMonticulo[i], listaMonticulo[hm]);
            }
            i = hm;
        }
    }

    int hijo_min(int i) {
        int hijo_izquierdo = i * 2;
        int hijo_derecho = i * 2 + 1;
        if (hijo_derecho <= tamanoActual && listaMonticulo[hijo_derecho].first < listaMonticulo[hijo_izquierdo].first) {
            return hijo_derecho;
        } else {
            return hijo_izquierdo;
        }
    }

public:
    MonticuloBinario() {
        listaMonticulo.push_back({0, ""}); // Agregar un elemento ficticio en el índice 0
        tamanoActual = 0;
    }

    void insertar(const string& elemento, int prioridad) {
        listaMonticulo.push_back({prioridad, elemento});
        tamanoActual++;
        flotar_arriba(tamanoActual);
    }

    pair<int, string> eliminarMin() {
        pair<int, string> minimo = listaMonticulo[1];
        listaMonticulo[1] = listaMonticulo[tamanoActual];
        tamanoActual--;
        listaMonticulo.pop_back();
        hundir_abajo(1);
        return minimo;
    }

    void construirMonticulo(const vector<pair<int, string>>& unaLista) {
        tamanoActual = unaLista.size();
        listaMonticulo = vector<pair<int, string>>(tamanoActual + 1);
        for (int j = 0; j < tamanoActual; j++) {
            listaMonticulo[j + 1] = unaLista[j];
        }
        for (int i = tamanoActual / 2; i > 0; i--) {
            hundir_abajo(i);
        }
    }
};

// Definición de la clase ColaPrioridad
class ColaPrioridad {
private:
    MonticuloBinario monticulo;

public:
    void agregar(const string& elemento, int prioridad) {
        monticulo.insertar(elemento, prioridad);
    }

    string avanzar() {
        return monticulo.eliminarMin().second;
    }
};


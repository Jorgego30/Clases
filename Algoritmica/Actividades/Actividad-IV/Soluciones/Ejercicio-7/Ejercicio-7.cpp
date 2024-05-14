#include <bits/stdc++.h>
#include "Class_MonticuloMax.hpp"

using namespace std;

void imprimir_monticulo_maximo(const MonticuloMaximo& monticulo) {
    cout << "Montículo máximo construido: ";
    for (int i = 1; i <= monticulo.tamanoActual; i++) {
        cout << monticulo.listaMonticulo[i] << " ";
    }
    cout << endl;
}

int main() {
    // Crear un montículo máximo y probar los métodos
    MonticuloMaximo monticulo_maximo;
    vector<int> lista_desordenada = {9, 5, 7, 2, 3, 6, 1, 8, 4};

    // Construir el montículo máximo
    monticulo_maximo.construir_monticulo(lista_desordenada);

    // Imprimir el montículo máximo
    imprimir_monticulo_maximo(monticulo_maximo);

    // Eliminar y imprimir el máximo repetidamente para ordenar la lista
    cout << "Lista ordenada: ";
    while (monticulo_maximo.getTamanoActual() > 0) {
        cout << monticulo_maximo.eliminar_maximo() << " ";
    }
    cout << endl;

    return 0;
}

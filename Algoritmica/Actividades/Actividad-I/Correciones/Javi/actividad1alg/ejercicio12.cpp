/*'''actividad12:Diseña un experimento para verificar que el operador indexación para listas es 𝑶𝑶(𝟏𝟏)'''*/
#include <iostream>
#include <vector>
#include <chrono>
#include <random>
using namespace std;

int main() {
    // Crear un vector grande
    int tamanio_vector = 1000000;
    std::vector<int> mi_vector(tamanio_vector);
    for (int i = 0; i < tamanio_vector; ++i) {
        mi_vector[i] = i;
    }

    // Medir el tiempo de acceso mediante el operador de indexación
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, tamanio_vector - 1);
    int indice_a_acceder = dis(gen);

    auto start_time = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < 1000000; ++i) {
        int valor_accedido = mi_vector[indice_a_acceder];
        // Hacer algo con el valor para evitar que el compilador lo optimice completamente
        if (valor_accedido == 42) {
            std::cout << "Valor accedido: " << valor_accedido << std::endl;
        }
    }
    auto end_time = std::chrono::high_resolution_clock::now();
    auto elapsed_time = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time);

    std::cout << "Tiempo de acceso mediante indexación: " << elapsed_time.count() << " microsegundos" << std::endl;

    return 0;
}

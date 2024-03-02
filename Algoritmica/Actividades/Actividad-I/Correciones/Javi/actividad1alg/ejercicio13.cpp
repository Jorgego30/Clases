'''actividad13:Diseña un experimento para verificar que las operaciones de obtención y asignación de ítems para
diccionarios son 𝑶𝑶(𝟏𝟏).'''
#include <iostream>
#include <unordered_map>
#include <chrono>
#include <random>

int main() {
    // Crear un unordered_map grande
    int tamanio_unordered_map = 1000000;
    std::unordered_map<int, int> mi_unordered_map;
    for (int i = 0; i < tamanio_unordered_map; ++i) {
        mi_unordered_map[i] = i;
    }

    // Medir el tiempo de obtención de ítems
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, tamanio_unordered_map - 1);
    int indice_a_obtener = dis(gen);

    auto start_time_obtencion = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < 1000000; ++i) {
        int valor_obtenido = mi_unordered_map[indice_a_obtener];
        // Hacer algo con el valor para evitar que el compilador lo optimice completamente
        if (valor_obtenido == 42) {
            std::cout << "Valor obtenido: " << valor_obtenido << std::endl;
        }
    }
    auto end_time_obtencion = std::chrono::high_resolution_clock::now();
    auto elapsed_time_obtencion = std::chrono::duration_cast<std::chrono::microseconds>(end_time_obtencion - start_time_obtencion);

    std::cout << "Tiempo de obtención de ítem: " << elapsed_time_obtencion.count() << " microsegundos" << std::endl;

    // Medir el tiempo de asignación de ítems
    int indice_a_asignar = dis(gen);
    int nuevo_valor = 42;

    auto start_time_asignacion = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < 1000000; ++i) {
        mi_unordered_map[indice_a_asignar] = nuevo_valor;
    }
    auto end_time_asignacion = std::chrono::high_resolution_clock::now();
    auto elapsed_time_asignacion = std::chrono::duration_cast<std::chrono::microseconds>(end_time_asignacion - start_time_asignacion);

    std::cout << "Tiempo de asignación de ítem: " << elapsed_time_asignacion.count() << " microsegundos" << std::endl;

    return 0;
}

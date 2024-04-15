#include <iostream>
#include "Class_Tablas_Hash.hpp"

using namespace std;

int main() {
    HashTable table;

    // Tamaño total de la tabla hash
    const int table_size = table.getSize();

    // Imprimir encabezado de la tabla
    cout << "Tasa de carga | Promedio de comparaciones (búsqueda exitosa) | Promedio de comparaciones (búsqueda sin éxito)" << endl;
    cout << "--------------|-------------------------------------------|-------------------------------------------" << endl;

    // Calcular y mostrar el número promedio de comparaciones para diferentes puntos de carga
    for (float load_factor : {0.1, 0.25, 0.5, 0.75, 0.9, 0.99}) {
        // Calcular el número de elementos en la tabla
        int num_elements = static_cast<int>(load_factor * table_size);

        // Insertar elementos en la tabla
        for (int i = 0; i < num_elements; ++i) {
            table.put(i, "word" + to_string(i)); // Insertar elementos ficticios en la tabla
        }

        // Realizar búsquedas exitosas y contar el número total de comparaciones
        int total_comparisons_successful_search = 0;
        for (int i = 0; i < num_elements; ++i) {
            string value;
            int index = table.get(i, value); // Realizar la búsqueda
            if (index != -1) {
                // Se encontró el elemento, contar las comparaciones realizadas
                total_comparisons_successful_search += table.getComparisons(); // Obtener el número de comparaciones
            }
        }

        // Realizar búsquedas sin éxito y contar el número total de comparaciones
        int total_comparisons_unsuccessful_search = 0;
        for (int i = table_size; i < 2 * table_size; ++i) {
            string value;
            int index = table.get(i, value); // Realizar la búsqueda
            if (index == -1) {
                // El elemento no se encontró, contar las comparaciones realizadas
                total_comparisons_unsuccessful_search += table.getComparisons(); // Obtener el número de comparaciones
            }
        }

        // Calcular el número promedio de comparaciones para búsqueda exitosa
        float avg_comparisons_successful_search = static_cast<float>(total_comparisons_successful_search) / num_elements;

        // Calcular el número promedio de comparaciones para búsqueda sin éxito
        float avg_comparisons_unsuccessful_search = static_cast<float>(total_comparisons_unsuccessful_search) / table_size;

        // Imprimir el resultado
        cout << load_factor << "            " << avg_comparisons_successful_search << "                                  " << avg_comparisons_unsuccessful_search << endl;
    }

    return 0;
}

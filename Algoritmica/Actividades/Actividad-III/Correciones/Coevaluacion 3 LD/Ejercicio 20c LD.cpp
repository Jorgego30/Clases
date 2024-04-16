/******************************************************************************
Enunciado: Un ordenamiento burbuja puede modificarse para que “burbujee” en ambas direcciones. La primera pasada
mueve la lista hacia “arriba”, y la segunda pasada la mueve hacia “abajo”. Este patrón alternante continúa
hasta que no son necesarias más pasadas. Implementa esta variación y describe en qué circunstancias podría
ser apropiada.
*******************************************************************************/
#include <iostream>
#include <vector>

// Función para realizar un ordenamiento de burbuja bidireccional
void ordenamientoBurbujaBidireccional(std::vector<int>& arr) {
    bool intercambiado = true;
    int inicio = 0;
    int fin = arr.size() - 1;

    while (intercambiado) {
        // Reseteamos la bandera a false esperando que el arreglo esté ordenado
        intercambiado = false;

        // Ordenamiento de burbuja en la dirección hacia arriba
        for (int i = inicio; i < fin; ++i) {
            if (arr[i] > arr[i + 1]) {
                std::swap(arr[i], arr[i + 1]);
                intercambiado = true;
            }
        }

        // Si no se intercambiaron elementos, el arreglo está ordenado
        if (!intercambiado)
            break;

        // De lo contrario, reseteamos la bandera para la siguiente iteración
        intercambiado = false;

        // Los elementos al final de la lista están en su lugar, así que reducimos el rango
        --fin;

        // Ordenamiento de burbuja en la dirección hacia abajo
        for (int i = fin - 1; i >= inicio; --i) {
            if (arr[i] > arr[i + 1]) {
                std::swap(arr[i], arr[i + 1]);
                intercambiado = true;
            }
        }

        // Los elementos al inicio de la lista están en su lugar, así que incrementamos el inicio
        ++inicio;
    }
}

int main() {
    std::vector<int> arr = {5, 1, 4, 2, 8, 0, 2};
    ordenamientoBurbujaBidireccional(arr);
    for (int i = 0; i < arr.size(); i++)
        std::cout << arr[i] << " ";
    return 0;
}

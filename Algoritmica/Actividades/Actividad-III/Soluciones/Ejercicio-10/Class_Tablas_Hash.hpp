
#include <iostream>
#include <vector>

class HashTable {
private:
    static const int size = 32767; // Tamaño máximo de la tabla
    std::vector<std::pair<int, std::string>> table[size]; // Tabla hash como un arreglo de vectores de pares clave-valor
    int comparisons; // Variable para almacenar el número de comparaciones realizadas durante la última operación de búsqueda

public:
    HashTable() : comparisons(0) {}
    int getSize() const {
        return size; // Devuelve el tamaño máximo de la tabla
    }
    // Función hash
    int hash(int key) {
        return key % size;
    }

    // Insertar un elemento en la tabla
    void put(int key, const std::string& value) {
        int index = hash(key); // Calcular el índice hash
        table[index].push_back(std::make_pair(key, value)); // Insertar el par clave-valor en la lista correspondiente
    }

    // Buscar un elemento en la tabla
    int get(int key, std::string& value) {
        int index = hash(key); // Calcular el índice hash
        comparisons = 0; // Restablecer el contador de comparaciones
        for (const auto& pair : table[index]) {
            comparisons++; // Incrementar el contador de comparaciones
            if (pair.first == key) { // Si se encuentra la clave
                value = pair.second; // Asignar el valor asociado a la clave
                return index; // Devolver el índice donde se encontró la clave
            }
        }
        // Si la clave no se encuentra
        return -1;
    }

    // Obtener el número de comparaciones realizadas durante la última operación de búsqueda
    int getComparisons() const {
        return comparisons;
    }
};


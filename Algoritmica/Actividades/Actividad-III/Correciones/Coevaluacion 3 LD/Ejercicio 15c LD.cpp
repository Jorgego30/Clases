/******************************************************************************
Enunciado: Implementa el método tamano (__len__) para la implementación del TAD Vector Asociativo o mapa de las
tablas hash, de manera que sea 𝑶(𝟏).
*******************************************************************************/
#include <unordered_map> 
#include <iostream>


class HashTable {
private:
    std::unordered_map<int, int> table; // La tabla hash se implementa como un mapa desordenado

public:
    // Método para insertar un par clave-valor en la tabla
    void insert(int key, int value) {
        table[key] = value;
    }

    // Método para obtener el tamaño de la tabla hash
    int size() const {
        return table.size(); // Devuelve el número de elementos en la tabla hash
    }
};

int main() {
    HashTable ht;

    // Insertamos algunos valores en la tabla hash
    ht.insert(1, 100);
    ht.insert(2, 200);
    ht.insert(3, 300);

    // Imprimimos el tamaño de la tabla hash
    std::cout << "El tamaño de la tabla hash es: " << ht.size() << std::endl;

    return 0;
}

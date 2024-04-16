#include <iostream>
#include <unordered_map>

using namespace std;

template<typename KeyType, typename ValueType>
class VectorAsociativo {
private:
    unordered_map<KeyType, ValueType> tabla_hash;
    size_t tamano_tabla; // Contador del número de elementos en la tabla hash
    
public:
    VectorAsociativo() : tamano_tabla(0) {}

    // Insertar un par clave-valor en el vector asociativo
    void insertar(const KeyType& clave, const ValueType& valor) {
        tabla_hash[clave] = valor;
        tamano_tabla++;
    }

    // Eliminar un elemento del vector asociativo
    void eliminar(const KeyType& clave) {
        auto it = tabla_hash.find(clave);
        if (it != tabla_hash.end()) {
            tabla_hash.erase(it);
            tamano_tabla--;
        }
    }

    // Obtener el tamaño del vector asociativo
    size_t tamano() const {
        return tamano_tabla;
    }
};
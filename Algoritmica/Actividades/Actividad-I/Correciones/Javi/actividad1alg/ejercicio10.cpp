'''actividad 10:Completar la clase Fracción en C++ para que sea como la desarrollada en Python'''
#include <iostream>
#include "Fraccion.hpp"

int main() {
    // Ejemplo de uso de la clase Fraccion en un programa

    // Crear fracciones
    Fraccion fraccion1(1, 2);
    Fraccion fraccion2(3, 4);

    // Realizar operaciones
    Fraccion suma = fraccion1 + fraccion2;
    Fraccion resta = fraccion1 - fraccion2;
    Fraccion multiplicacion = fraccion1 * fraccion2;
    Fraccion division = fraccion1 / fraccion2;

    // Imprimir resultados
    std::cout << "Fraccion1: " << fraccion1 << std::endl;
    std::cout << "Fraccion2: " << fraccion2 << std::endl;
    std::cout << "Suma: " << suma << std::endl;
    std::cout << "Resta: " << resta << std::endl;
    std::cout << "Multiplicacion: " << multiplicacion << std::endl;
    std::cout << "Division: " << division << std::endl;

    // Comparar fracciones
    if (fraccion1 == fraccion2) {
        std::cout << "Las fracciones son iguales." << std::endl;
    } else {
        std::cout << "Las fracciones no son iguales." << std::endl;
    }

    if (fraccion1 != fraccion2) {
        std::cout << "Las fracciones no son iguales." << std::endl;
    } else {
        std::cout << "Las fracciones son iguales." << std::endl;
    }

    return 0;
}

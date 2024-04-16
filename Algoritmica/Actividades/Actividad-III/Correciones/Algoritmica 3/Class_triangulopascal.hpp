#include <iostream>
#include <vector>

class TrianguloPascal {
public:
    // Método para imprimir el triángulo de Pascal utilizando recursividad
    static void imprimirRecursivo(int numFilas) {
        for (int i = 0; i < numFilas; ++i) {
            for (int j = 0; j <= i; ++j) {
                std::cout << coeficienteBinomial(i, j) << " ";
            }
            std::cout << std::endl;
        }
    }

    // Método para imprimir el triángulo de Pascal utilizando fuerza bruta
    static void imprimirFuerzaBruta(int numFilas) {
        std::vector<std::vector<int>> triangulo(numFilas);
        for (int i = 0; i < numFilas; ++i) {
            triangulo[i].resize(i + 1);
            triangulo[i][0] = 1;
            triangulo[i][i] = 1;
            for (int j = 1; j < i; ++j) {
                triangulo[i][j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j];
            }
        }
        imprimirTriangulo(triangulo);
    }

private:
    // Función para calcular el coeficiente binomial (nCr)
    static int coeficienteBinomial(int n, int r) {
        if (r == 0 || r == n) return 1;
        return coeficienteBinomial(n - 1, r - 1) + coeficienteBinomial(n - 1, r);
    }

    // Función para imprimir el triángulo
    static void imprimirTriangulo(const std::vector<std::vector<int>>& triangulo) {
        for (const auto& fila : triangulo) {
            for (int num : fila) {
                std::cout << num << " ";
            }
            std::cout << std::endl;
        }
    }
};
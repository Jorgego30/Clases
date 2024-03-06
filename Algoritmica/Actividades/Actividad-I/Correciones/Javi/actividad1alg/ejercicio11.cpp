/*'''actividad11: Escribe dos funciones para encontrar el número mínimo en una lista. La primera función debe comparar
cada número de una lista con todos los demás de la lista. 𝑶𝑶(𝒏𝒏𝟐𝟐). La segunda función debe ser lineal 𝑶𝑶(𝒏𝒏)'''*/
#include <iostream>
#include <vector>

int encontrarMinCuadratico(const std::vector<int>& lista) {
    int n = lista.size();
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (lista[j] < lista[i]) {
                break;
            }
        }
        // Este bloque se ejecuta si el bucle 'for' interior no fue interrumpido por 'break'
        return lista[i];
    }

    // Si no se encontró un mínimo, se devuelve -1 (podría ocurrir si la lista está vacía)
    return -1;
}

int encontrarMinLineal(const std::vector<int>& lista) {
    if (lista.empty()) {
        // Manejar caso de lista vacía
        return -1;
    }

    int minimo = lista[0];
    for (int i : lista) {
        if (i < minimo) {
            minimo = i;
        }
    }
    return minimo;
}

int main() {
    // Ejemplo de uso
    std::vector<int> numeros = {5, 3, 8, 2, 1, 7, 4};

    int resultadoCuadratico = encontrarMinCuadratico(numeros);
    int resultadoLineal = encontrarMinLineal(numeros);

    std::cout << "Mínimo cuadrático: " << resultadoCuadratico << std::endl;
    std::cout << "Mínimo lineal: " << resultadoLineal << std::endl;

    return 0;
}

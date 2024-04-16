#include <iostream>
#include <vector>
#include <climits>

class CambioMonedas {
public:
    // Función para encontrar el menor número de monedas utilizando programación dinámica
    static int minMonedas(int valor, const std::vector<int>& denominaciones) {
        std::vector<int> dp(valor + 1, INT_MAX); // Inicializar un vector de tamaño valor+1 con valores INT_MAX
        dp[0] = 0; // Caso base: se necesitan 0 monedas para devolver 0 céntimos

        for (int i = 1; i <= valor; ++i) { // Iterar a través de los valores desde 1 hasta valor
            for (int j = 0; j < denominaciones.size(); ++j) { // Iterar a través de las denominaciones
                if (denominaciones[j] <= i) { // Verificar si la denominación actual es menor o igual al valor actual
                    int subproblema = dp[i - denominaciones[j]]; // Obtener el valor óptimo del subproblema
                    if (subproblema != INT_MAX && subproblema + 1 < dp[i]) {
                        dp[i] = subproblema + 1; // Actualizar el valor óptimo si es menor que el valor actual
                    }
                }
            }
        }
        return dp[valor]; // Devolver el valor óptimo para devolver el cambio
    }
};

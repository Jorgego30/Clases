/*Actividad 4:

Usando el algoritmo de programación dinámica para dar las vueltas, encuentra el menor número de
monedas que se podrían usar para completar unas vueltas de 33 céntimos. Además de las monedas usuales,
supón que disponemos de una moneda de 8 céntimos. Realizar una simulación con distintas cantidades a
devolver y distintos valores de monedas.
*/

#include <iostream>
#include <vector>
#include <climits>
#include "Class_cambiarmonedas.hpp"

using namespace std;

int main() {
    int cantidad = 33; // Cantidad a devolver: 33 céntimos
    vector<int> denominaciones = {1, 2, 5, 8}; // Denominaciones de monedas disponibles

    // Se imprime la cantidad a devolver y las denominaciones de monedas disponibles
    cout << "Cantidad a devolver: " << cantidad << " centimos" << endl;
    cout << "Denominaciones de monedas disponibles: ";
    for (int d : denominaciones) {
        cout << d << " ";
    }
    cout << endl;

    // Se calcula el número mínimo de monedas necesarias utilizando el algoritmo implementado en la clase CambioMonedas
    int minMonedas = CambioMonedas::minMonedas(cantidad, denominaciones);
    
    // Se imprime el número mínimo de monedas necesarias para devolver la cantidad solicitada
    cout << "Numero minimo de monedas necesarias: " << minMonedas << endl;

    return 0;
}

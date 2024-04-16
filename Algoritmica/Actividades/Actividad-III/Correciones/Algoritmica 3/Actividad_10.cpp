/*Actividad 10:

Utilizando las fórmulas de desempeño de la tabla hash que se dan en el Tema 4, calcula el número promedio
de comparaciones necesarias cuando la tabla está
10% completa
25% completa
50% completa
75% completa
90% completa
99% completa
¿En qué punto crees que la tabla hash es demasiado pequeña? Explícalo.
*/


#include <iostream>
#include <cmath>
using namespace std;

// Función para calcular el valor promedio de comparaciones en direccionamiento abierto cuando tiene éxito
float direcionamiento_abierto_exito(float landa)
{
    // Mostramos el valor de lambda en la terminal
    cout << "Lambda: " << landa << endl;
    // Calculamos el valor promedio de comparaciones cuando el direccionamiento abierto tiene éxito
    float exito = (0.5*(1+1/(1-landa)));
    return exito;
}

// Función para calcular el valor promedio de comparaciones en direccionamiento abierto cuando fracasa
float direcionamiento_abierto_fracaso(float landa)
{
    // Calculamos el valor promedio de comparaciones cuando el direccionamiento abierto fracasa
    float fracaso = (1.0/2)*(1+(1/pow((1-landa),2)));
    return fracaso;
}

// Función para calcular el valor promedio de comparaciones en encadenamiento cuando tiene éxito
float encadenamiento_exito(float landa)
{
    // Calculamos el valor promedio de comparaciones cuando el encadenamiento tiene éxito
    float exito = 1+(landa/2);
    return exito;
}

// Función para calcular el valor promedio de comparaciones en encadenamiento cuando fracasa
float encadenamiento_fracaso(float landa)
{
    // Calculamos el valor promedio de comparaciones cuando el encadenamiento fracasa
    float fracaso = landa;
    return fracaso;
}

int main()
{
    // Declaramos los distintos valores de carga a trabajar
    float cargas[6] = {0.1, 0.25, 0.5, 0.75, 0.9, 0.99};

    // Recorremos el array de cargas
    for (int i = 0; i < 6; i++)
    {
        // Mostramos la ocupación actual
        cout << "\nOcupacion del " << cargas[i] * 100 << "%\n" << endl;

        // Calculamos y mostramos los valores promedio de comparaciones para el direccionamiento abierto
        float dir_abierto_exito = direcionamiento_abierto_exito(cargas[i]);
        float dir_abierto_fracaso = direcionamiento_abierto_fracaso(cargas[i]);
        cout << "Valor promedio de comparaciones en direccionamiento abierto (exito): " << dir_abierto_exito << endl;
        cout << "Valor promedio de comparaciones en direccionamiento abierto (fracaso): " << dir_abierto_fracaso << endl;

        // Calculamos y mostramos los valores promedio de comparaciones para el encadenamiento
        float encadenamiento_ex = encadenamiento_exito(cargas[i]);
        float encadenamiento_frac = encadenamiento_fracaso(cargas[i]);
        cout << "Valor promedio de comparaciones en encadenamiento (exito): " << encadenamiento_ex << endl;
        cout << "Valor promedio de comparaciones en encadenamiento (fracaso): " << encadenamiento_frac << "\n" << endl;
    }

    return 0;
}

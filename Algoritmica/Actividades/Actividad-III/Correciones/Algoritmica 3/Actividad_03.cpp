/*Actividad 3:
El triángulo de Pascal es un triángulo numérico con números dispuestos en filas escalonadas de manera que
Esta ecuación es la ecuación para un coeficiente binomial. Se puede construir el triángulo de Pascal
agregando los dos números que están, en diagonal, encima de un número en el triángulo. A continuación, se
muestra un ejemplo del triángulo de Pascal.
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
Escribe, siguiendo técnicas descritas en los apuntes, distintas versiones de un programa que imprima el
triángulo de Pascal. El programa debe aceptar un parámetro que indique cuántas filas se imprimirán del
triángulo.

*/

#include <iostream>
#include <vector>
#include "Class_triangulopascal.hpp"

using namespace std;

int main() {
    int numFilas; // Se declara una variable para almacenar el número de filas ingresado por el usuario
    cout << "Ingrese el numero de filas para el triangulo de Pascal: ";
    cin >> numFilas; // Se solicita al usuario que ingrese el número de filas para el triángulo de Pascal

    cout << "Triangulo de Pascal utilizando recursividad:" << endl;
    TrianguloPascal::imprimirRecursivo(numFilas); // Se llama al método estático imprimirRecursivo de la clase TrianguloPascal para imprimir el triángulo de Pascal utilizando recursividad

    cout << "\nTriangulo de Pascal utilizando fuerza bruta:" << endl;
    TrianguloPascal::imprimirFuerzaBruta(numFilas); // Se llama al método estático imprimirFuerzaBruta de la clase TrianguloPascal para imprimir el triángulo de Pascal utilizando fuerza bruta

    return 0; // Se indica que el programa finalizó correctamente
}

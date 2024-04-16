/*El triángulo de Pascal es un triángulo numérico con números dispuestos en filas escalonadas de manera que 
anr=n!/(r!*(n-r)!) 
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
triángulo.*/
#include <iostream>
#include <vector>

// Función para calcular el coeficiente binomial
int coeficienteBinomial(int n, int k) {
    if (k==0 || k==n)
        return 1;
    if (k==1 || k==n-1)
        return n;
    if (k>n-k)
        k=n-k;
    int c = 1;
    for (int i = 0; i < k; i++)
        c = c * (n-i) / (i+1);
    return c;
}

// Función para imprimir el triángulo de Pascal
void imprimirPascal(int filas) {
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j <= i; j++)
            std::cout << coeficienteBinomial(i, j) << " ";
        std::cout << "\n";
    }
}

int main() {
    int filas;
    std::cout << "Introduce el número de filas: ";
    std::cin >> filas;
    imprimirPascal(filas);
    return 0;
}

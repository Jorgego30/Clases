#include <bits/stdc++.h>
using namespace std;

// Se calcula el coeficiente de cada numero del triangulo de pascal
int coeficiente(int n, int k){
    // Se define el resto con el valor base del triangulo
    int resto = 1;

    // k es el numero que corresponde a la posicion en el triangulo mientras que n corresponde al numero de fila con el que estamos trabajando
    // En el siguiente for calculamos el numero de la fila n en la posicion k usando la formula del triangulo de Pascal (a(nk) = (n!)/(k!(n-k)!) )
    for (int i = 0; i < k; ++i) {
        resto *= (n - i);
        resto /= (i + 1);
    }
 
    return resto;
}

// Calcula el producto de todos los números en una fila del Triángulo de Pascal
long long multiplicarFila(int n) {
    long long producto = 1;
    for (int i = 0; i <= n; ++i) {
        producto *= coeficiente(n, i);
    }
    return producto;
}

// La siguiente funcion imprime por pantalla el triangulo de Pascal con el metodo binario
void trianguloBinario(int numeroFilas){
    vector <int> valores;
    // Se define la variable espacios para poder formatear bien el triangulo
    int espacios = numeroFilas-1;
    // Variable para almacenar el resultado de la fila anterior
    long double resultadoFilaAnterior = 1;
    // El siguiente for es el que imprime el triangulo
    for (int i=0; i < numeroFilas; i++){
        // El siguiente for imprime los espacios convenientes a la izquierda de los numeros (Solo a la izquierda ya que el lado derecho se formatea solo)
        for (int j=0; j<espacios; j++){
            cout << " ";
        }

        // El siguiente for llama a la funcion coeficiente para poder calcular el numero que hay que cada posicion
        for (int j=0; j<i+1; j++){
                int numero = coeficiente(i,j);
                valores.push_back(numero);
                cout << " " << numero;
            }

        // Multiplicar los números en la fila actual
        long long producto = multiplicarFila(i);

        // Dividir entre el resultado de la fila anterior
        long double resultado = producto / resultadoFilaAnterior;
        cout << " (Resultado: " << resultado << ")";

        // Se actualiza el resultado de la fila anterior
        resultadoFilaAnterior = producto;

        // Se inserta un salto de linea
        cout << endl;

        // Se reduce en uno el numero de espacios pues cada vez que avanzo una linea hay un espacio menos
        espacios--;

        valores.clear();
    }
}

// Programa principal
int main(){
    // Se define la variable que contendra el total de lineas, tiene un valor arbitrario para hacer la validacion
    int numeroFilas = -1;

    // Se crea un bool para poder controlar mejor la validacion
    bool validacionMal = true;

    // Se realiza la validacion de datos
    while (validacionMal==true && numeroFilas<=0){
        try{
            // Se pide al usuario que indique cuantas lineas quiere que conforme el triangulo
            cout << "Introduce el numero de filas que quieres que tenga el triangulo de pascal: "; cin >> numeroFilas;
            validacionMal = false;
            if (cin.fail() || numeroFilas<=0){
                cin.clear();
                cin.ignore();
                validacionMal = true;
                throw 1;
            }
        }catch(...){
            cout << "Debes introducir un numero entero positivo" << endl;
        }

    }

    trianguloBinario(numeroFilas);
}

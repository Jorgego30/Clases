//Importamos todo lo necesario:
#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <cstdlib> // Para std::rand()
using namespace std;

//Creamos una función que imprima la lista
void printVector(const vector<int>& vec) {
    cout<<"[";
    for (int x : vec) {
        cout << x << " ";
    }
    cout<<"]"<<endl;
}

void Burbuja_bidireccional(vector<int>& lista)
{
    int n = lista.size();

    int derecha = n - 1;
    int izquierda = 0;

    bool intercambiar = true;

    while(intercambiar)
    {
        intercambiar = false;
        
        // Ordenamos la lista de izquierda a derecha para el último elemento
        for(int i = izquierda; i < derecha; i++) {
            // Se intercambian los elementos si el que se encuentra es más grande que el siguiente:
            if (lista[i] > lista[i + 1]) {
                swap(lista[i], lista[i + 1]);
                intercambiar = true;
            }
        }
        derecha--; //Acortamos el límite de la lista a ordenar ya que hay un número más ordenado

        if (!intercambiar)
            break;

        // Ordenamos la lista de derecha a izquierda para el primer elemento
        for(int j = derecha; j > izquierda; j--) {
            if (lista[j] < lista[j - 1]) {
                swap(lista[j], lista[j - 1]);
                intercambiar = true;
            }
        }
        izquierda++; //Acortamos el límite de la lista a ordenar ya que hay un número más ordenado


        // Imprimimos la lista después de cada paso para ver cómo se ordena:
        printVector(lista);
    }
}

//Importamos todo lo necesario:
#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <cstdlib> // Para std::rand()
using namespace std;
int Elegir_Pivote(vector<int>& lista);

//Creamos una función que imprima la lista
void printVector(const vector<int>& vec) {
    cout<<"[";
    for (int x : vec) {
        cout << x << " ";
    }
    cout<<"]"<<endl;
}

void Seleccion(vector<int>& lista)
{
    int n,min,elemento;
    n=lista.size();

    //Entramos en un bucle para recorrer la lista entera
    for(int i=0;i<n;i++)
    {
        min=i;
        //Buscamos el mínimo elemento en la parte de la lista que queda por ordenar:
        for(int j=i+1;j<n;j++)
        {
            if (lista[min]>lista[j])
            {
                min=j;
            }
        }
        //Intercambiamos el primer elemento por el mínimo encontrado en la parte que nos faltaba por ordenar        
        elemento=lista[i];
        lista[i]=lista[min];
        lista[min]=elemento;
    }
}

void Shell_Knuth(vector<int>& lista)
{
    int n = lista.size();
    int gap, temp;
    gap = 1;

    // Calculamos el valor inicial de gap
    while (gap <= n/3)
        gap = gap * 3 + 1;

    // Comienza con la sublista más grande y la reduce en cada iteración
    while (gap > 0){
        for(int i = gap; i < n; i++){
            temp = lista[i];
            int j = i;
            // Inserta el elemento en la posición correcta dentro de su sublista
            while ((j >= gap) && (lista[j - gap] > temp)){
                lista[j] = lista[j - gap];
                j -= gap;
            }
            lista[j] = temp;
        }
        // Reducimos la sublista
        gap = gap / 3;
    }
}

void Mezcla(vector<int>& lista)
{
    int n,medio,i,j,k;
    vector<int> izq,der;
    n=lista.size();

    if (n>1)
    {
        //Buscamos el medio de la lista:
        medio=n/2;

        //Dividimos la lista en 2 por la mitad:
        izq.assign(lista.begin(), lista.begin() + medio);
        der.assign(lista.begin()+medio, lista.end());

        Mezcla(izq);
        Mezcla(der);

        i=j=k=0;

        //Copiamos el contenido de las listas izq y der
        while ((i < izq.size()) && (j < der.size())){
            if (izq[i] <= der[j]){
                lista[k] = izq[i];
                i += 1;
            }
            else{
                lista[k] = der[j];
                j += 1;
            }
            k += 1;
        }
        //Comprobamos si quedan elementos por ordenar
        while (i < izq.size()){
            lista[k] = izq[i];
            i += 1;
            k += 1;
        }
        while (j < der.size()){
            lista[k] = der[j];
            j += 1;
            k += 1;
        }
    }
}

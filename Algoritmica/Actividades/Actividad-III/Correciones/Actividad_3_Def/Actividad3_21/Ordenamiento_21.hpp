//Importamos todo lo necesario:
#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <cstdlib> // Para rand()
using namespace std;

void Shell_mitad(vector<int>& lista)
{
    int n,gap;
    n=lista.size();
    gap=n/2;

    while (gap>0)
    {
        int j=gap;
        while(j<n)
        {
           int i=j-gap;
           while(i>=0)
           {
                //Si el valor de la derecha es mayor que el de la izquierda no se intercambian, sino si
                if (lista[i+gap]>lista[i])
                    break;
                else
                    swap(lista[i+gap],lista[i]);
                i=i-gap;
           }
            j+=1; 
        } 
        gap=gap/2;
    }
}

void Shell_raiz(vector<int>& lista)
{
    int n = lista.size();
    int gap = int(sqrt(n));

    while (gap > 0)
    {
        for (int i = gap; i < n; ++i)
        {
            int temp = lista[i];
            int j = i;
            while (j >= gap && lista[j - gap] > temp)
            {
                lista[j] = lista[j - gap];
                j -= gap;
            }
            lista[j] = temp;
        }
        
        gap = gap/2; // Reducir el gap
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

void Shell_Hibbard(vector<int>& lista)
{
    int n,gap,temp;
    n=lista.size();
    gap=1;

    //Calculamos el tamaño inicial del contadorSublistas usando la secuencia de Hibbard
    while (gap<n/3)
        gap = gap*2+1;

    //Comenzamos con el contadorSublistas más grande y lo reducimos en cada iteración
    while (gap>0){
        //Insertamos los valores en orden
        for(int i=gap;i<n;i++){
            temp = lista[i];
            int j = i;

            while ((j>=gap) && (lista[j-gap]>temp)){
                lista[j] = lista[j-gap];
                j -= gap;
            }
            lista[j] = temp;
        }
        //Reducimos el contadorSublistas
        gap = (gap-1)/2;
    }
}

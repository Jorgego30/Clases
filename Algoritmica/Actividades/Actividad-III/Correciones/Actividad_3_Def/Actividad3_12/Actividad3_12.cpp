#include "Class_Ordenamiento.hpp"
#include <iostream>
#include <ostream>
using namespace std;

int main()
{
    vector<int> lista,M1,M2,M3,M4,M5,M6,M7,M8,M9;
    
    //Creamos vectores nuevos
    for(int i=0;i<20;i++){
        lista.push_back(rand() % 100);
    }

    //Pasamos la lista a distintas variables para que siempre sea la misma lista la que ordenamos y veamos los distintos procesos:
    M1=lista;
    M2=lista;
    M3=lista;
    M4=lista;
    M5=lista;
    M6=lista;
    M7=lista;
    M8=lista;
    M9=lista;

    //Primer método (Ordenamiento burbuja unidireccional):
    cout<<"Método de ordenamiento Burbuja Unidireccional: "<<endl;
    Burbuja_unidireccional(M1);

    //Segundo método (Ordenamiento burbuja bidireccional):
    cout<<endl<<"Método de ordenamiento Burbuja Bidireccional: "<<endl;
    Burbuja_bidireccional(M2);

    //Tercer método (Ordenamiento por selección):
    cout<<endl<<"Método de ordenamiento por Selección: "<<endl;
    Seleccion(M3);

    //Cuarto método (Ordenamiento por inserción):
    cout<<endl<<"Método de ordenamiento por Inserción: "<<endl;
    insercion(M4); 

    //Quinto método (Ordenamiento de Shell por la mitad):
    cout<<endl<<"Método de ordenamiento de Shell por la mitad: "<<endl;
    Shell_mitad(M5);

    //Sext método (Ordenamiento de Shell por la raíz):
    cout<<endl<<"Método de ordenamiento de Shell por la raíz: "<<endl;
    Shell_raiz(M6);

    //Séptimo método (Ordenamiento de Shell variante Knuth):
    cout<<endl<<"Método de ordenamiento por Shell variante Knuth: "<<endl;
    Shell_Knuth(M7);
    
    //Octavo método (Ordenamiento por Mezcla):
    cout<<endl<<"Método de ordenamiento por Mezcla: "<<endl;
    Mezcla(M8); 

    //Noveno método (Ordenamiento rápido (Quicksort)):
    cout<<endl<<"Método de ordenamiento por Quicksort: "<<endl;
    Quicksort(M9); 
}

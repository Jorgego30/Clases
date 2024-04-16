#include <iostream>
#include <ostream> 
#include "Class_Listas_No_Ordenadas2.hpp"
using namespace std; 

//Funcion que invierte una lista de tipo 'ListaNoOrdenada'
ListaNoOrdenada invertirlista(ListaNoOrdenada lista_inicial){
     ListaNoOrdenada lista_final;
     //Si la lista inicial esta vacia, se devuelve una lista vacia
     if (lista_inicial.estavacia()) {
          return lista_final;
     }
     //Si no esta vacia, se extrae el elemento de la ultima posicion y se llama recursivamente a la funcion. 
     //Finalmente se le agrega el elemento extraido y se devuelve la lista resultante
     else{
          int n;
          n = lista_inicial.extraer(lista_inicial.tamano()-1);
          lista_final = invertirlista(lista_inicial);
          lista_final.agregar(n);
          return lista_final;
     }
}

int main()
{
     //Se crea una lista y se le anhaden elementos
    ListaNoOrdenada lista1;
    lista1.agregar(31);
    lista1.agregar(77);
    lista1.agregar(17);
    lista1.agregar(93);
    lista1.agregar(26);
    lista1.agregar(54);
    lista1.agregar(1);
     //Se imprime la lista
    cout << "Lista inicial: " << endl;
    cout << lista1 << endl;
    //Se invierte la lista y se imprime
    ListaNoOrdenada lista_invertida;
    lista_invertida = invertirlista(lista1);
    cout << "Lista invertida: " << endl;
    cout << lista_invertida << endl;

    return 0;
}



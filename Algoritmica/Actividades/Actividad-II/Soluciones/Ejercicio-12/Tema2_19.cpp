#include <iostream>  //se podria quitar, dado que esta en la clase
#include <ostream>  //se podria quitar, dado que esta en la clase
#include "Class_Listas_Ordenadas.hpp"
using namespace std;  //se podria quitar, dado que esta en la clase

// similar to unordered lists except it orders the data

int main(){
     OrderedList mylist;
     mylist.add(31);
     mylist.add(77);
     mylist.add(17);
     mylist.add(93);
     mylist.add(26);
     mylist.add(54);

     cout << "Tamaño: " << mylist.size() << endl;
     cout << "Contiene 93?\t" << mylist.search(93) << endl;
     cout << "Contiene 100?\t" << mylist.search(100) << endl << endl;
     cout << "La lista esta formada por: " << endl << mylist;

     mylist.borrar(93);
     cout << "La lista esta formada por: " << endl << mylist << endl;

     cout << "El numero 17 esta en la posicion: " << mylist.indice(17) << endl;

     cout << "El ultimo numero de la lista era: " << mylist.extraer() << endl;

     cout << "El tercer numero de la lista era: " << mylist.extraer(2) << endl;
    
     cout << "La lista esta formada por: " << endl << mylist << endl;


    return 0;
}

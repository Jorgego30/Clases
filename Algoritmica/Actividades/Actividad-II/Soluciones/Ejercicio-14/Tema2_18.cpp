#include <iostream> //se podria quitar, dado que esta en la clase
#include <ostream>  //se podria quitar, dado que esta en la clase
#include "Class_Listas_No_Ordenadas.hpp"
using namespace std;  //se podria quitar, dado que esta en la clase


int main()
{
     UnorderedList mylist;
     mylist.add(31);
     mylist.add(77);
     mylist.add(17);
     mylist.add(93);
     mylist.add(26);
     mylist.add(54);

     cout << "Tanaño: " << mylist.size() << endl;
     cout << "Contiene 93?\t" << mylist.search(93) << endl;
     cout << "Contiene 100?\t" << mylist.search(100) << endl << endl;

     mylist.add(100);
     cout << "Contiene 100?\t" << mylist.search(100) << endl << endl;
     cout << "Tamaño: " << mylist.size() << endl;

     mylist.remove(54);
     cout << "Tamaño: " << mylist.size() << endl;
     mylist.remove(93);
     cout << "Tamaño: " << mylist.size() << endl;
     mylist.remove(31);
     cout << "Tamaño: " << mylist.size() << endl;

     cout << "La primera lista esta formada por: " << endl << mylist;

     cout << "El numero 100 esta en la posicion: " << mylist.search(100) << endl;

     UnorderedList mySecondList;
     mySecondList.add(32);
     mySecondList.add(73);
     mySecondList.add(14);
     mySecondList.add(96);
     mySecondList.add(76);
     mySecondList.add(354);

     cout << "Tamaño: " << mySecondList.size() << endl;
     cout << "Contiene 93?\t" << mySecondList.search(93) << endl;
     cout << "Contiene 100?\t" << mySecondList.search(100) << endl << endl;

     mySecondList.add(100);
     cout << "Contiene 100?\t" << mySecondList.search(100) << endl << endl;
     cout << "Tamaño: " << mySecondList.size() << endl;

     mySecondList.remove(354);
     cout << "Tamaño: " << mySecondList.size() << endl;
     mySecondList.remove(73);
     cout << "Tamaño: " << mySecondList.size() << endl;
     mySecondList.remove(14);
     cout << "Tamaño: " << mySecondList.size() << endl;

     cout << "La segunda lista esta formada por: " << endl << mySecondList;

     mylist.anexar(mySecondList);

     cout << "La segunda lista anexada a la primera quedaria de la siguiente forma formada por: " << endl << mylist << endl;

     cout << "El primer numero en la lista es: " << mylist.inicio() << endl;
     cout << "El ultimo numero en la lista es: " << mylist.fin() << endl;
     cout << "El numero que esta despues de 96 es: " << mylist.siguiente(96) << endl;
     cout << "El numero que esta antes de 96 es: " << mylist.anterior(96) << endl;

    
    return 0;
}

#include <iostream> 
using namespace std;
#include "Class_Listas_Ordenadas.hpp"



int main()
{
    OrderedList lista = OrderedList();
    lista.add(78);
    lista.add(8);
    lista.add(46);
    lista.add(89);
    lista.add(4);
    lista.add(3);
    lista.add(120);
    lista.add(57);

    cout << lista.impresion() << endl;

    cout << "tamano de lista: " << lista.size() << endl;

    
}
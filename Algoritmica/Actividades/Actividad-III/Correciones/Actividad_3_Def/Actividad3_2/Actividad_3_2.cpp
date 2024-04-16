#include <iostream>
#include <ostream> 
#include "Class_Jarras.hpp"
using namespace std; 


int main()
{
     //Se crean la jarra de 3l y la de 4l
     cout << " - - - - - - - - - - Se crean las dos jarras - - - - - - - - - - " << endl;
     Jarra jarra3l(3);
     Jarra jarra4l(4);
     cout << "¿Esta llena la jarra de 4l? (0:No / 1:Si) " << jarra4l.estallena() << endl;
     cout << "¿Esta llena la jarra de 3l? (0:No / 1:Si) " << jarra3l.estallena() << endl;
     //Se llena la jarra de 3l
     cout << " - - - - - - - - - - Se llena la jarra de 3l - - - - - - - - - - " << endl;
     jarra3l.llenar();
     cout << "¿Esta llena la jarra de 3l? (0:No / 1:Si) " << jarra3l.estallena() << endl;
     cout << "¿Cuantos litros contiene la jarra de 3l? " << jarra3l.litros() << endl;
     //Se trasvasa el agua de la jarra de 3l a la de 4l (Quedara 1l libre en la jarra de 4l)
     cout << " - - - - - - - - - - Se trasvasa el agua de la jarra de 3l a la de 4l - - - - - - - - - - " << endl;
     jarra3l = jarra4l.trasvasar(jarra3l);
     cout << "¿Cuantos litros contiene la jarra de 3l? " << jarra3l.litros() << endl;
     cout << "¿Cuantos litros contiene la jarra de 4l? " << jarra4l.litros() << endl;
     //Se llena nuevamente la jarra de 3l
     cout << " - - - - - - - - - - Se llena nuevamente la jarra de 3l - - - - - - - - - - " << endl;
     jarra3l.llenar();
     cout << "¿Cuantos litros contiene la jarra de 3l? " << jarra3l.litros() << endl;
     cout << "¿Cuantos litros contiene la jarra de 4l? " << jarra4l.litros() << endl;
     //Se trasvasa el agua de la jarra de 3l a la de 4l (Como queda 1l libre en la jarra de 4l, se llenara esa jarra y la de 3l quedara con 2l)
     cout << " - - - - - - - - - - Se trasvasa el agua de la jarra de 3l a la de 4l (Hasta que se llena la jarra) - - - - - - - - - - " << endl;
     jarra3l = jarra4l.trasvasar(jarra3l);
     cout << "¿Cuantos litros contiene la jarra de 3l? " << jarra3l.litros() << endl;
     cout << "¿Cuantos litros contiene la jarra de 4l? " << jarra4l.litros() << endl;
     //Se vacia la jarra de 4l
     cout << " - - - - - - - - - - Se vacia la jarra de 4l - - - - - - - - - - " << endl;
     jarra4l.vaciar();
     //Se cambia el agua de la jarra de 3l a la de 4l
     cout << " - - - - - - - - - - Se trasvasa el agua de la jarra de 3l a la de 4l - - - - - - - - - - " << endl;
     jarra3l = jarra4l.trasvasar(jarra3l);
     cout << "¿Cuantos litros contiene la jarra de 3l? " << jarra3l.litros() << endl;
     cout << "¿Cuantos litros contiene la jarra de 4l? " << jarra4l.litros() << endl;
    return 0;
}



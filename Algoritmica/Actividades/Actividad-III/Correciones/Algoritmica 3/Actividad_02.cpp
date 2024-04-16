/*Actividad 2:

Escribe un programa de POO para resolver el siguiente problema:
Tienes dos jarras, una de 4 litros y otra de 3 litros. Ninguna de las jarras tiene marcas en ella. Hay una
bomba que se puede utilizar para llenar las jarras con agua. ¿Cómo se pueden obtener exactamente dos
litros de agua en la jarra de 4 litros?*/


#include <iostream>
#include "Class_Jarra.hpp"

using namespace std;

int main() {
    // Crear jarras de 4 y 3 litros
    Jarra jarra4(4);
    Jarra jarra3(3);

    // Llenar la jarra de 4 litros
    jarra4.llenar();
    cout << "Jarra de 4 litros: " << jarra4.getCantidad() << " litros, Jarra de 3 litros: " << jarra3.getCantidad() << " litros" << endl;

    // Transferir agua de la jarra de 4 litros a la de 3 litros hasta que se llene
    jarra4.transferirA(jarra3);
    cout << "Jarra de 4 litros: " << jarra4.getCantidad() << " litros, Jarra de 3 litros: " << jarra3.getCantidad() << " litros" << endl;

    // Vaciar la jarra de 3 litros
    jarra3.vaciar();
    cout << "Jarra de 4 litros: " << jarra4.getCantidad() << " litros, Jarra de 3 litros: " << jarra3.getCantidad() << " litros" << endl;

    // Transferir agua de la jarra de 4 litros a la de 3 litros
    jarra4.transferirA(jarra3);
    cout << "Jarra de 4 litros: " << jarra4.getCantidad() << " litros, Jarra de 3 litros: " << jarra3.getCantidad() << " litros" << endl;

    // Llenar la jarra de 4 litros
    jarra4.llenar();
    cout << "Jarra de 4 litros: " << jarra4.getCantidad() << " litros, Jarra de 3 litros: " << jarra3.getCantidad() << " litros" << endl;

    // Transferir agua de la jarra de 4 litros a la de 3 litros hasta que esté llena
    jarra4.transferirA(jarra3);
    cout << "Jarra de 4 litros: " << jarra4.getCantidad() << " litros, Jarra de 3 litros: " << jarra3.getCantidad() << " litros" << endl;

    cout << "Tras estas operaciones hay 2L en la jarra de 4L" << endl;

    return 0;
}

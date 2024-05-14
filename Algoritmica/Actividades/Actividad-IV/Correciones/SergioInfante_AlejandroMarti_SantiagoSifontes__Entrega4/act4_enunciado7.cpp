/*7. Implementa un montículo binario como un montículo máx.*/

/*Prueba de la clase del archivo act4_enunciado7.hpp*/

#include <iostream>
#include "MaxHeap.hpp"
using namespace std;

int main()
{
    MaxHeap h(11);
    h.insertar(4);
    h.insertar(7);
    h.insertar(15);
    h.insertar(10);
    h.insertar(4);
    h.insertar(45);
    h.eliminarEn(2);
    cout << h.extraerMax() << " "<<endl;
    cout << h.obtenerMax() << endl;
    
    return 0;
}
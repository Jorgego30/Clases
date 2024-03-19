/*Implementar el método anexar una nueva lista para ListaNoOrdenada. ¿Cuál es la
complejidad de tiempo del método que creaste?*/


//Importamos las librerias necesarias 

#include <iostream>
#include "class_ejercicio10.hpp"
using namespace std;


int main(){

    UnorderedList lista1,lista2;
	
	//Creando la lista 1
    lista1.add(5);
    lista1.add(4);
	
	//Mostrandola
    cout << "Lista 1: "<<endl;
    cout << lista1 <<endl;
	
	//Creando la lista 2
    lista2.add(3);
    lista2.add(2);
    lista2.add(1);
	
	//Mostrandola
    cout << "Lista 2: "<<endl;
    cout << lista2 <<endl;

    lista1.anexar_lista(lista2);
	
	//Mostrando las listas anexadas
    cout << "Listas anexadas: "<<endl;
    cout << lista1 <<endl;
    
    cout<<"Pulsa Enter para finalizar: ";
    cin.ignore().get();
    return 0;
}
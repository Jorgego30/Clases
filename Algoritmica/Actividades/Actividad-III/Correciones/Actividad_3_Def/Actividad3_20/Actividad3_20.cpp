/*  Pregunta: Este patrón alternante continúa hasta que no son necesarias más pasadas. Implementa esta
 variación y describe en qué circunstancias podría ser apropiada.
    Respuesta: Este método puede ser apropiado cuando se busca una mejora del método unidireccional o 
 cuando la lista ya está parcialmente ordenada ya que podría reducir el número de comparaciones que 
 se hacen.
*/

#include "Ordenamiento_20.hpp" //Importamos la función de ordenamiento Burbuja bidireccional
#include <iostream>
#include <ctime>
#include <ostream>
using namespace std;

int main()
{
    vector<int> lista;

    //Creamos vectores nuevos
    for(int i=0;i<25;i++){
        lista.push_back(rand() % 100);
    }

    cout<<"La lista original es: ";
    printVector(lista);
    cout<<endl;

    //Ordenamos la lista con Burbuja bidireccional:
    Burbuja_bidireccional(lista);
}

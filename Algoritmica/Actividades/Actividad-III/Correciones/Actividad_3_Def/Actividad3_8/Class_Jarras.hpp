#include <iostream>
#include <ostream>
using namespace std;

//Clase que usa nodos para crear una lista no ordenada
class Jarra
{
public:
    float max_litros = 0;
    float litros_actuales = 0;
    Jarra(int litros_jarra)
    { //Crea la jarra. Se debe indicar el tamanho de la jarra
        max_litros = litros_jarra;
    }

    int litros()
    {   //Funcion que devuelve los litros actuales que tiene la jarra
        return litros_actuales;
    }
    bool estavacia()
    { //Funcion que indica si la jarra esta vacia
        return litros_actuales == 0; 
    }

    bool estallena()
    { //Funcion que indica si la jarra esta vacia
        return litros_actuales == max_litros; 
    }

    bool llenar(int litros)
    { //Funcion que permite llenar la jarra con una cantidad exacta de litros. En el caso de que los litros llenados excedan el limite de llenado, no se llenara la jarra y se devolvera 0. En caso contrario, se llenara y devolvera 1.
        if ((litros_actuales + litros) > max_litros){
            return 0;
        }
        else{
            litros_actuales = litros_actuales + litros;
            return 1;
        }
    }

    void llenar()
    { //Funcion que permite llenar la jarra al maximo. 
        litros_actuales = max_litros;
    }

    bool vaciar(int litros)
    { //Funcion que permite sacar cierta cantidad de litros a la jarra. En el caso de que los litros vaciados sean menore que 0, no se vaciara la jarra y se devolvera 0. En caso contrario, se vaciara y devolvera 1.
        if ((litros_actuales - litros) < 0){
            return 0;
        }
        else{
            litros_actuales = litros_actuales - litros;
            return 1;
        }
    }

    void vaciar()
    { //Funcion que permite llenar la jarra al maximo. 
        litros_actuales = 0;
    }

    Jarra trasvasar(Jarra jarra2)
    { //Funcion que permite llenar la jarra. En el caso de que los litros llenados excedan el limite de llenado, no se llenara la jarra y se devolvera 0. En caso contrario, se llenara y devolvera 1.
        if (jarra2.litros() > (max_litros-litros_actuales)){
            jarra2.vaciar(max_litros-litros_actuales);
            litros_actuales = max_litros;
            return jarra2;
        }
        else{
            litros_actuales = litros_actuales + jarra2.litros();
            jarra2.vaciar();
            return jarra2;
            
        }
    }
};

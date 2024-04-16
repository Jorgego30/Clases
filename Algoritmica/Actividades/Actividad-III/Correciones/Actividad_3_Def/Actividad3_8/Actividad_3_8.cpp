#include <iostream>
#include <ostream> 
#include "Class_Jarras.hpp"
#include <list>
#include <cmath>
using namespace std; 

// Objetivo: Conseguir x/2 litros en la jarra 1

/*Eventos: 
    1-> Vaciar la jarra 1
    2-> Vaciar la jarra 2
    3-> Llenar la jarra 1
    4-> Llenar la jarra 2
    5-> Trasvasar la jarra 1 a la 2
    6-> Trasvasar la jarra 2 a la 1
*/

list<int> buscarsolucion(const float objetivo, int evento, Jarra jarra1, Jarra jarra2, int n, int nmax)
    /*
    Objetivo de la funcion:
        A partir de 2 jarras, se buscara la manera de que, realizando diferentes acciones sobre ellas (trasvasar agua, llenalas, vaciarlas...) se consiga
        la cantidad de litros deseada en la jarra 1. Se usan arboles de backtracking mediante recursividad.
    Descripcion de los argumentos:
        Objetivo-> Cantidad de litros que se quieren conseguir en la jarra 1
        Evento -> Evento que se quiere realizar en la rama a la que se esta llamando:
            1-> Vaciar la jarra 1
            2-> Vaciar la jarra 2
            3-> Llenar la jarra 1
            4-> Llenar la jarra 2
            5-> Trasvasar la jarra 1 a la 2
            6-> Trasvasar la jarra 2 a la 1
        Jarra1 -> Jarra 1 (X)
        Jarra2 -> Jarra 2 (Y)
        N -> Altura de la rama a la que se esta llamando
        Nmax -> Numero maximo de ramas a las que se quieren llamar
    */
{
    //cout << "1" << endl;
    // - - - - - - - - - - - - - - - Si ya se ha llegado al numero maximo de ramas, se devuelve una lista vacia. - - - - - - - - - - - - - - - 
    if (nmax == n){
        //cout << "Se ha llegado al numero maximo de ramas" << endl;
        list<int> lista;
        return lista;
    }
    // - - - - - - - - - - - - - - - Si no se ha llegado al numero maximo de ramas, se realiza el evento requerido y se generan el resto de ramas. - - - - - - - - - - - - - - - 
    else{
        //cout << "2" << endl;
        //Evento 1
        if (evento == 1){
            //Se realiza el evento
            jarra1.vaciar();
            //Se comprueba si se ha conseguido el objetivo
            if ((round(jarra1.litros()*100)/100) == objetivo){
                //cout << "Se ha encontrado el objetivo al realizar el evento " << evento << endl;
                //Si se ha conseguido el objetivo, se crea una lista, se le inserta el numero de evento realizado y se devuelve.
                list<int> lista1;
                lista1.push_back(evento);
                return lista1;
            }
        }
        //Evento 2
        if (evento == 2){
            //Se realiza el evento
            jarra2.vaciar();
            //Se comprueba si se ha conseguido el objetivo
            if ((round(jarra1.litros()*100)/100) == objetivo){
                //cout << "Se ha encontrado el objetivo al realizar el evento " << evento << endl;
                //Si se ha conseguido el objetivo, se crea una lista, se le inserta el numero de evento realizado y se devuelve.
                list<int> lista1;
                lista1.push_back(evento);
                return lista1;
            }
        }
        //Evento 3
        if (evento == 3){
            //Se realiza el evento
            jarra1.llenar();
            //Se comprueba si se ha conseguido el objetivo
            if ((round(jarra1.litros()*100)/100) == objetivo){
                //cout << "Se ha encontrado el objetivo al realizar el evento " << evento << endl;
                //Si se ha conseguido el objetivo, se crea una lista, se le inserta el numero de evento realizado y se devuelve.
                list<int> lista1;
                lista1.push_back(evento);
                return lista1;
            }
        }
        //Evento 4
        if (evento == 4){
            //Se realiza el evento
            jarra2.llenar();
            //Se comprueba si se ha conseguido el objetivo
            if ((round(jarra1.litros()*100)/100) == objetivo){
                //cout << "Se ha encontrado el objetivo al realizar el evento " << evento << endl;
                //Si se ha conseguido el objetivo, se crea una lista, se le inserta el numero de evento realizado y se devuelve.
                list<int> lista1;
                lista1.push_back(evento);
                return lista1;
            }
        }
        //Evento 5
        if (evento == 5){
            //Se realiza el evento
            jarra1 = jarra2.trasvasar(jarra1);
            //Se comprueba si se ha conseguido el objetivo
            if ((round(jarra1.litros()*100)/100) == objetivo){
                //cout << "Se ha encontrado el objetivo al realizar el evento " << evento << endl;
                //Si se ha conseguido el objetivo, se crea una lista, se le inserta el numero de evento realizado y se devuelve.
                list<int> lista1;
                lista1.push_back(evento);
                return lista1;
            }
        }
        //Evento 6
        if (evento == 6){
            //Se realiza el evento
            jarra2 = jarra1.trasvasar(jarra2);
            //Se comprueba si se ha conseguido el objetivo
            if ((round(jarra1.litros()*100)/100) == objetivo){
                //cout << "Se ha encontrado el objetivo al realizar el evento " << evento << endl;
                //Si se ha conseguido el objetivo, se crea una lista, se le inserta el numero de evento realizado y se devuelve.
                list<int> lista1;
                lista1.push_back(evento);
                return lista1;
            }
        }
        //cout << "3" << endl;
        // - - - - - - - - - - - - - - - Si no se ha conseguido el objetivo, se llaman a las ramas con todos los posibles eventos - - - - - - - - - - - - - - - 
        list<int> lista2;
        //Rama 1
        if ((evento != 1) and (not jarra1.estavacia())){
            //cout << "Se comienza a buscar el evento 1 de la altura " << n << endl;
            lista2 = buscarsolucion(objetivo, 1, jarra1, jarra2, n+1, nmax);
                //Si el resultado de la rama no esta vacio, quiere decir que se ha encontrado la solucion. Se le anhade el evento y se devuelve la lista
            if (not lista2.empty()){
                lista2.push_back(evento);
                return lista2;
            }
            else{
                lista2.clear();
            }
        }
        //Rama 2
        if ((evento != 2) and (not jarra2.estavacia())){
            //cout << "Se comienza a buscar el evento 2 de la altura " << n << endl;
            lista2 = buscarsolucion(objetivo, 2, jarra1, jarra2, n+1, nmax);
                //Si el resultado de la rama no esta vacio, quiere decir que se ha encontrado la solucion. Se le anhade el evento y se devuelve la lista
            if (not lista2.empty()){
                lista2.push_back(evento);
                return lista2;
            }
            else{
                lista2.clear();
            }
        }
        //Rama 3
        if ((evento != 3)){
            //cout << "Se comienza a buscar el evento 3 de la altura " << n << endl;
            lista2 = buscarsolucion(objetivo, 3, jarra1, jarra2, n+1, nmax);
                //Si el resultado de la rama no esta vacio, quiere decir que se ha encontrado la solucion. Se le anhade el evento y se devuelve la lista
            if (not lista2.empty()){
                lista2.push_back(evento);
                return lista2;
            }
            else{
                lista2.clear();
            }
        }
        //Rama 4
        if ((evento != 4)){
            //cout << "Se comienza a buscar el evento 4 de la altura " << n << endl;
            lista2 = buscarsolucion(objetivo, 4, jarra1, jarra2, n+1, nmax);
                //Si el resultado de la rama no esta vacio, quiere decir que se ha encontrado la solucion. Se le anhade el evento y se devuelve la lista
            if (not lista2.empty()){
                lista2.push_back(evento);
                return lista2;
            }
            else{
                lista2.clear();
            }
        }
        //Rama 5
        if (evento != 5){
            //cout << "Se comienza a buscar el evento 5 de la altura " << n << endl;
            lista2 = buscarsolucion(objetivo, 5, jarra1, jarra2, n+1, nmax);
                //Si el resultado de la rama no esta vacio, quiere decir que se ha encontrado la solucion. Se le anhade el evento y se devuelve la lista
            if (not lista2.empty()){
                lista2.push_back(evento);
                return lista2;
            }
            else{
                lista2.clear();
            }
        }
        //Rama 6
        if (evento != 6){
            //cout << "Se comienza a buscar el evento 6 de la altura " << n << endl;
            lista2 = buscarsolucion(objetivo, 6, jarra1, jarra2, n+1, nmax);
                //Si el resultado de la rama no esta vacio, quiere decir que se ha encontrado la solucion. Se le anhade el evento y se devuelve la lista
            if (not lista2.empty()){
                lista2.push_back(evento);
                return lista2;
            }
            else{
                lista2.clear();
            }
        }
        return lista2;
        }

}


int main()
{
    int litrosjarra1, litrosjarra2, nmaxramas;
    cout << "Objetivo: Conseguir x/2 litros en la jarra 1. Ejemplos: (Jarra 1: 4l / Jarra 2: 1l), (Jarra 1: 2l / Jarra 2: 1l)" << endl;
    cout << "Ingresar la cantidad de litros maximos de la jarra 1 (X): ";
    cin >> litrosjarra1;
    bool verificado = false;
    while (verificado != true){
        cout << "Ingresar la cantidad de litros maximos de la jarra 2 (Y): ";
        cin >> litrosjarra2;
        if (litrosjarra2>=litrosjarra1){
            cout << "Los litros de la jarra 1 deben ser mayores que los de la jarra 2" << endl;
        }
        else{
            verificado = true;
        }
    }
    Jarra jarra1(litrosjarra1);
    Jarra jarra2(litrosjarra2);
    float objetivo = litrosjarra1 / 2;
    list<int> solucion;
    bool validacion = false;
    nmaxramas = 5;
    int n = 0;
    while(validacion == false){
        n++;
        solucion = buscarsolucion(objetivo, 0, jarra1, jarra2, 0, n);
        if (solucion.empty()){
            cout << "No se ha encontrado solucion para " << n << " niveles." << endl;
        }
        else{
            cout << "Se ha encontrado una solucion para " << n << " niveles:" << endl;
            solucion.reverse();
            int valor;
            for (auto v : solucion){
                //std::cout << v << "\n";
                valor = v;
                if (valor==1){
                    cout << "Vaciar la jarra 1" << endl;
                }
                if (valor==2){
                    cout << "Vaciar la jarra 2" << endl;
                }
                if (valor==3){
                    cout << "Llenar la jarra 1" << endl;
                }
                if (valor==4){
                    cout << "Llenar la jarra 2" << endl;
                }
                if (valor==5){
                    cout << "Trasvasar la jarra 1 a la 2" << endl;
                }
                if (valor==6){
                    cout << "Trasvasar la jarra 2 a la 1" << endl;
                }
            }
            cout << "La jarra 1 finalmente contiene " << litrosjarra1/2 << " litros." << endl;
            validacion = true;
        }
        if (n>= nmaxramas){
            validacion = true;
        }
    }
    return 0;
}



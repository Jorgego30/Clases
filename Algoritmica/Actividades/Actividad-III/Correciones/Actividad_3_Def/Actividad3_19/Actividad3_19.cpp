#include "Ordenamiento_19.hpp"
#include <iostream>
#include <ctime>
#include <ostream>
using namespace std;

int main()
{
    vector<int> lista,M1,M2,M3;
    vector<double> Tiempo1,Tiempo2,Tiempo3,tamaño;
    float media1=0,media2=0,media3=0;

    for(int j=1;j<30;j+=1) {
        //Creamos vectores nuevos
        for(int i=0;i<500;i++){
            lista.push_back(rand() % 100);
        }

        //Hacemos copias de la lista:
        M1=lista;
        M2=lista;
        M3=lista;
        tamaño.push_back(j);

        //Primer método (Ordenamiento por Selección):
        clock_t begin_t1 = clock();
        Seleccion(M1);
        clock_t end_t1 = clock();
        double tiempo1 = double(end_t1 - begin_t1)/CLOCKS_PER_SEC;
        Tiempo1.push_back(tiempo1);
  
        //Segundo método (Ordenamiento por Mezcla):
        clock_t begin_t2 = clock();
        Mezcla(M2);
        clock_t end_t2 = clock();
        double tiempo2 = double(end_t2 - begin_t2)/CLOCKS_PER_SEC;
        Tiempo2.push_back(tiempo2);

        //Tercer método (Ordenamiento de Shell variante Knuth):
        clock_t begin_t3 = clock();
        Shell_Knuth(M3);
        clock_t end_t3 = clock();
        double tiempo3 = double(end_t3 - begin_t3)/CLOCKS_PER_SEC;
        Tiempo3.push_back(tiempo3);
    }

    //Comunicamos resultados:
    cout<<"Tamaño \t    Tiempo Selección \t     Tiempo Mezcla \t   Tiempo Shell Knuth "<<endl;
    for(int k=0;k<Tiempo1.size();k++)
    {
        cout<<"500 \t \t"<<Tiempo1[k]<<"\t \t"<<Tiempo2[k]<<"\t \t"<<Tiempo3[k]<<endl;
        media1+=Tiempo1[k];
        media2+=Tiempo2[k];
        media3+=Tiempo3[k];
    }
    media1/=Tiempo1.size();
    media2/=Tiempo2.size();
    media3/=Tiempo3.size();

    cout<<"Media: \t \t"<<media1<<"\t \t"<<media2<<"\t \t"<<media3<<endl;

    cout<<"Viendo los datos obtenidos podemos ver que el método de Ordenamiento por Selección es el que más tiempo"<<endl;
    cout<<"consume de los tres y que el método Shell variante Knuth es el más rápido de los tres"<<endl;
}
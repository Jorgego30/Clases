#include "Ordenamiento_21.hpp"
#include <iostream>
#include <ctime>
#include <ostream>
using namespace std;

int main()
{
    vector<int> lista,M1,M2,M3,M4;
    vector<double> tiempoM,tiempoR,tiempoK,tiempoH,tamaño;
    float mediaM=0,mediaR=0,mediaK=0,mediaH=0;

    for(int j=1000;j<10001;j+=500) {
        //Creamos vectores nuevos
        for(int i=0;i<j;i++){
            lista.push_back(rand() % 100);
        }

        //Hacemos copias de la lista:
        M1=lista;
        M2=lista;
        M3=lista;
        M4=lista;
        tamaño.push_back(j);

        //Primer método (Ordenamiento de Shell por la mitad):
        clock_t begin_t1 = clock();
        Shell_mitad(M1);
        clock_t end_t1 = clock();
        double tiempo1 = double(end_t1 - begin_t1)/CLOCKS_PER_SEC;
        tiempoM.push_back(tiempo1);
  
        //Segundo método (Ordenamiento de Shell por la raíz):
        clock_t begin_t2 = clock();
        Shell_raiz(M2);
        clock_t end_t2 = clock();
        double tiempo2 = double(end_t2 - begin_t2)/CLOCKS_PER_SEC;
        tiempoR.push_back(tiempo2);

        //Tercer método (Ordenamiento de Shell variante Knuth):
        clock_t begin_t3 = clock();
        Shell_Knuth(M3);
        clock_t end_t3 = clock();
        double tiempo3 = double(end_t3 - begin_t3)/CLOCKS_PER_SEC;
        tiempoK.push_back(tiempo3);

        //Cuarto método (Ordenamiento de Shell variante Hibbard):
        clock_t begin_t4 = clock();
        Shell_Hibbard(M4);
        clock_t end_t4 = clock();
        double tiempo4 = double(end_t4 - begin_t4)/CLOCKS_PER_SEC;
        tiempoH.push_back(tiempo4);        
    }

    //Comunicamos resultados:
    cout<<"Tamaño \t Tiempo Shell medio \t Tiempo Shell raiz \t Tiempo Shell Knuth \t Tiempo Shell Hibbard"<<endl;
    for(int k=0;k<tiempoM.size();k++)
    {
        cout<<tamaño[k]<<"\t \t"<<tiempoM[k]<<"\t \t"<<tiempoR[k]<<"\t \t"<<tiempoK[k]<<" \t \t"<<tiempoH[k]<<endl;
        mediaM+=tiempoM[k];
        mediaR+=tiempoR[k];
        mediaK+=tiempoK[k];
        mediaH+=tiempoH[k];
    }
    mediaM/=tiempoM.size();
    mediaR/=tiempoM.size();
    mediaK/=tiempoM.size();
    mediaH/=tiempoM.size();

    cout<<"Media: \t \t"<<mediaM<<"\t \t"<<mediaR<<"\t \t"<<mediaK<<"\t \t"<<mediaH<<endl;
}
//Ejercicio15
#include <iostream>
using namespace std;
int main () 
{   
    int tam,i,j,aux,k;
    int vector[200];
    
    cout<<"Dame el tamano del vector: ";
    cin>>tam;

    for (i=0;i<tam;i++){
        vector[i]= rand() % 1001;
    }
    for (i=0;i<tam;i++)
    {
        for (j=i+1;j<tam;j++)
        {
            if(vector[i]>vector[j])
            {
                aux=vector[i];
                vector[i]=vector[j];
                vector[j]=aux;
            }
        }

    }
    for (i=0;i<tam;i++){
        cout<<vector[i]<<",";
    }
    
    cout<<endl<<"Introduce el k-esimo numero que quieres buscar: ";
    cin>>k;
    cout<<"El k-esimo número mas pequeno  del array es: "<<vector[k];

    return 0;
}  
#include <iostream>
#include <vector>
#define Max_tam 2000
using namespace std;
void leer_vector (int v[],int);
int main () 
{   
    int tam;
    int vector[Max_tam];
    int minimo1;
    int minimo2;
    
    cout<<"Dame el tamanyo del vector: ";
    cin>>tam;
    leer_vector (vector,tam);
    minimo1 = vector[0];
    minimo2 = vector[0];

  for(int  i=0;i < tam ; i++){

    if(vector[i] < minimo1){
      minimo1 = vector[i];
    }
  }


  for(int  i=0;i < tam;i++){

      for(int  j=0;j < tam ;j++){

          if((vector[i] < vector[j])&&(vector[i]<minimo2)){
          minimo2 = vector[i];
          }
      }
  }


  cout<<"\nEl minimo entero de la serie es: "<< minimo1;
  cout<<"\nEl minimo entero de la serie es: "<< minimo2 << endl;
  cout << vector;

  return 0;
}  
 // fin de main
/*Devuelve un vector con los numeros dados*/
void leer_vector (int v[], int t) {
    int i;
/*Pide cada numero y lo mete en el vector*/
    for (i=0;i<t;i++) 
	{
        v[i] = rand() % 1001;
        cout << v[i] << ' ';
        
    }
} // fin de leer_vector
/*Devuelve el mayor valor del vector dado*/


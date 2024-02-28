#include <bits/stdc++.h>
using namespace std;

void numero_a_numero(vector<int> numeros){
    int menor=100000;
    clock_t begin = clock();
    for (int i=0; i<numeros.size(); i++){
        for (int j=0; j < numeros.size(); j++){
            if (numeros[j] < numeros[i] && numeros[j]<menor){
                menor = numeros[j];
            }
        }
    }
    clock_t end = clock(); 
    double segundos = double(end - begin)/CLOCKS_PER_SEC;
    cout << fixed << endl;
    cout << "El programa con complejidad O(n²) da el minimo de: " << menor << " con un tiempo de ejecucion de: " << segundos << endl;
}

void recorrer_lista (vector<int> numeros){
    int menor = 100000;
    clock_t begin = clock();
    for (int i=0; i<numeros.size(); i++){
        if (numeros[i] < menor){
            menor = numeros[i];
        }
    }
    clock_t end = clock();
    double segundos = double(end - begin)/CLOCKS_PER_SEC;
    cout << fixed << endl;
    cout << "El programa com complejidad O(n) da el minimo de: " << menor << " con un tiempo de ejecucion de: " << segundos << endl;
}

int main(){
    srand(time(NULL));
    vector <int> numeros;
    
    for (int i=0; i<10000; i++){
        numeros.push_back(1+rand()%(101-1));
    }

    cout << "La lista es: ";

    for (int i=0; i<numeros.size(); i++){
        cout << numeros[i] << ", "; 
    }
    cout << endl;

    numero_a_numero(numeros);

    recorrer_lista(numeros);
}
#include <bits/stdc++.h>
using namespace std;

int numero_a_numero(vector<int> numeros){
    int menor=100000;
    for (int i=0; i<numeros.size(); i++){
        for (int j=0; j != numeros.size(); j++){
            if (numeros[j] < numeros[i]){
                menor = numeros[j];
            }
        }
    }

    return menor;
}

int recorrer_lista (vector<int> numeros){
    int menor = 100000;
    for (int i=0; i<numeros.size(); i++){
        if (numeros[i] < menor){
            menor = numeros[i];
        }
    }

    return menor;

}

int main(){
    vector <int> numeros = {10,23,435,4,565,32,321,2,543};

    cout << numero_a_numero(numeros) << endl;

    cout << recorrer_lista(numeros) << endl;
}
#include <bits/stdc++.h>
using namespace std;

void recorrer_lista(std::vector<int> numeros) {
    set<int> conjunto_numeros(numeros.begin(), numeros.end());
    
    clock_t begin = clock();
    int menor = *conjunto_numeros.begin();
    clock_t end = clock();
    
    double segundos = double(end - begin) / CLOCKS_PER_SEC;
    cout << fixed << endl;
    cout << "El programa con complejidad O(n log(n)) da el mínimo de: " << menor << " con un tiempo de ejecución de: " << segundos << " segundos" << endl;
}

int main(){
    srand(time(NULL));
    vector <int> numeros_desordenados;
    
    for (int i=0; i<10000; i++){
        numeros_desordenados.push_back(1+rand()%(101-1));
    }

    recorrer_lista(numeros_desordenados);

}
#include <bits/stdc++.h>
using namespace std;

void indexacion(vector<int>a){
    clock_t begin = clock();
    for (int i=0; i<a.size(); i++){
        int b = a[i];
    }
    clock_t end = clock(); 
    double segundos = double(end - begin)/CLOCKS_PER_SEC;
    cout << fixed << endl;
    cout << "La indexacion de un vector tiene una complejidad de O(1) como se ve en el tiempo: " << segundos << endl;
}


int main(){
    srand(time(NULL));
    vector <int> a;
    
    for (int i=0; i<10000; i++){
        a.push_back(1+rand()%(101-1));
    }

    indexacion(a);
}
#include <bits/stdc++.h>
using namespace std;

void imprimirVector(vector<int> vector){
    for (int i=0; i<vector.size(); i++){
        cout << vector[i] << " ";
    }
    cout << endl;
}

vector<int> vectorAleatorio(){
    int size = rand()%100;
    vector<int> vector (size);
    for (int i=0; i<size; i++){
        vector [i] = rand()%1000;
    }
    return vector;
}

// Función recursiva para encontrar el valor máximo en un tramo específico [izq; der] de un vector V
int maxValueInRange(const vector<int>& V, int izq, int der) {
    // Caso base: cuando el tramo tiene solo un elemento
    if (izq == der) {
        return V[izq];
    }

    // Calculamos el índice medio del tramo
    int medio = (izq + der) / 2;

    // Obtenemos el valor máximo de la mitad izquierda y derecha del tramo
    int maxIzq = maxValueInRange(V, izq, medio);
    int maxDer = maxValueInRange(V, medio + 1, der);

    // Devolvemos el máximo entre los valores de la mitad izquierda y derecha
    return max(maxIzq, maxDer);
}

int main() {
    srand (time(NULL));
    vector<int> V = vectorAleatorio();

    int izq = -1; // Índice izquierdo del tramo
    int der = -1; // Índice derecho del tramo
    imprimirVector(V);
    while(izq<0){
        try{
            cout << "Introduce el indice izquierdo del tramo que quieras: "; cin >> izq;
            if(cin.fail()){
                cin.clear();
                cin.ignore();
                throw 1;
            }
        }catch(...){
            cout << "Debes introducir un entero positivo" << endl;
            izq = -1;
        }
    }
    while (der<izq){
        try{
            cout << "Introduce el indice derecho del tramo que quieras: "; cin >> der;
            if(cin.fail()){
                cin.clear();
                cin.ignore();
                throw 1;
            }
        }catch(...){
            cout << "Debes introducir un entero positivo" << endl;
            der = -1;
        }

    }

    clock_t begin = clock();
    int maxValor = maxValueInRange(V, izq, der);
    clock_t end = clock();
    double segundos = double(end - begin) / CLOCKS_PER_SEC;
    cout << "El valor máximo en el tramo [" << izq << "; " << der << "] es: " << maxValor << endl;
    cout << fixed << endl;
    cout << "El tiempo de ejecucion del programa ha sido de " << segundos << endl;


    return 0;
}

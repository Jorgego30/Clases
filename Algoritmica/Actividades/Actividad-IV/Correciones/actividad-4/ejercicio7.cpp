//mplementa un montículo binario como un montículo máx

//IMplementamos las librerias necesarias 

#include <iostream>
#include <vector>
using namespace std;

#include "Class_binheap_max.hpp"


// Programa peincipal
int main(){
    int arr[] = {27, 17, 33, 21};
    vector<int> a(arr,arr+(sizeof(arr)/ sizeof(arr[0])));

    vector<int> vec;
    vec.push_back(0);

    BinHeap *bh = new BinHeap(vec);

    bh->insert(27);
    bh->insert(17);
    bh->insert(33);
    bh->insert(21);

    cout << "Eliminamos valor maximo: " << bh->delMax() << endl;
    cout << "Eliminamos valor maximo: " << bh->delMax() << endl;
    cout << "Eliminamos valor maximo: " << bh->delMax() << endl;
    cout <<"Eliminamos valor maximo: " << bh->delMax() << endl;

    cout << "Creacion del monticulo mediante un vector "<<endl;
    bh->buildheap(a);


    cout << "Eliminamos valo r maximo: " << bh->delMax() << endl;
    cout << "Eliminamos valor maximo: " << bh->delMax() << endl;
    cout << "Eliminamos valor maximo: " << bh->delMax() << endl;
    cout << "Eliminamos valor maximo: " << bh->delMax() << endl;

    return 0;
}



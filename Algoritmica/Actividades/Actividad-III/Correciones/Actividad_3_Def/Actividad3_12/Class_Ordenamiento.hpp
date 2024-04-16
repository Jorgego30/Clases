//Importamos todo lo necesario:
#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <cstdlib> // Para std::rand()
#include <algorithm>
using namespace std;
int Elegir_Pivote(vector<int>& lista);

//Creamos una función que imprima la lista
void printVector(const vector<int>& vec) {
    cout<<"[";
    for (int x : vec) {
        cout << x << " ";
    }
    cout<<"]"<<endl;
}

//Creamos la función de ordenamiento burbuja:
void Burbuja_unidireccional(vector<int>& lista)
{
    int n=lista.size();

    //Entramos en un bucle para recorrer la lista entera
    for(int i=0;i<n;i++)
    {
        bool intercambiar = false;
        //Recorremos la lista eliminando el último elemento porque ya está ordenado
        for(int j=0;j<n-i-1;j++)
        {
            //Se intercambian los elementos si el que se encuentra es más grande que el anterior:
            if (lista[j] > lista[j+1])
            {
                swap(lista[j],lista[j+1]);
                intercambiar = true;
            }
        }
        //Imprimimos la lista después de cada paso para ver como se ordena:
        printVector(lista);

        //Si el elemento ya está donde tiene que estar no intercambiamos nada para esa posición y volvemos a recorrer:
        if (intercambiar == false)
            break;
    }
}

//Creamos la función de ordenamiento burbuja bidireccional:
void Burbuja_bidireccional(vector<int>& lista)
{
    int n = lista.size();

    int derecha = n - 1;
    int izquierda = 0;

    bool intercambiar = true;

    while(intercambiar)
    {
        intercambiar = false;
        
        // Ordenamos la lista de izquierda a derecha para el último elemento
        for(int i = izquierda; i < derecha; i++) {
            // Se intercambian los elementos si el que se encuentra es más grande que el siguiente:
            if (lista[i] > lista[i + 1]) {
                swap(lista[i], lista[i + 1]);
                intercambiar = true;
            }
        }
        derecha--;

        if (!intercambiar)
            break;

        // Ordenamos la lista de derecha a izquierda para el primer elemento
        for(int j = derecha; j > izquierda; j--) {
            if (lista[j] < lista[j - 1]) {
                swap(lista[j], lista[j - 1]);
                intercambiar = true;
            }
        }
        izquierda++;

        // Imprimimos la lista después de cada paso para ver cómo se ordena:
        printVector(lista);
    }
}

//Creamos la función de ordenamiento por selección:
void Seleccion(vector<int>& lista)
{
    int n,min,elemento;
    n=lista.size();

    //Entramos en un bucle para recorrer la lista entera
    for(int i=0;i<n;i++)
    {
        min=i;
        //Buscamos el mínimo elemento en la parte de la lista que queda por ordenar:
        for(int j=i+1;j<n;j++)
        {
            if (lista[min]>lista[j])
            {
                min=j;
            }
        }
        //Intercambiamos el primer elemento por el mínimo encontrado en la parte que nos faltaba por ordenar        
        elemento=lista[i];
        lista[i]=lista[min];
        lista[min]=elemento;

        //Imprimimos la lista después de cada paso para ver como se ordena:
        printVector(lista);
    }
}

//Creamos la función de ordenamiento por inserción:
void insercion(vector<int>& lista)
{
    int n,posicion,valorActual;
    n=lista.size();

    //Entramos en un bucle para recorrer la lista entera
    for(int i=1;i<n;i++)
    {
        valorActual=lista[i];
        posicion=i;

        while ((posicion > 0) && (lista[posicion-1] > valorActual))
        {
            lista[posicion] = lista[posicion-1];
            posicion = posicion-1;
        }
        lista[posicion] = valorActual; //Pasamos elemento a elemento a su posición correcta

        //Imprimimos la lista después de cada paso para ver como se ordena:
        printVector(lista);
    }
}
//Creamos la función de ordenamiento por método shell (con incrementos de la mitad):
void Shell_mitad(vector<int>& lista)
{
    int n,gap;
    n=lista.size();
    gap=n/2;

    while (gap>0)
    {
        int j=gap;
        while(j<n)
        {
           int i=j-gap;
           while(i>=0)
           {
                //Si el valor de la derecha es mayor que el de la izquierda no se intercambian, sino si
                if (lista[i+gap]>lista[i])
                    break;
                else
                    swap(lista[i+gap],lista[i]);
                i=i-gap;
           }
            j+=1; 
        } 
        gap=gap/2;
        printVector(lista);
    }
}

//Creamos la función de ordenamiento por método shell (con incrementos de la raíz):
void Shell_raiz(vector<int>& lista)
{
    int n = lista.size();
    int gap = int(sqrt(n));

    while (gap > 0)
    {
        for (int i = gap; i < n; ++i)
        {
            int temp = lista[i];
            int j = i;
            while (j >= gap && lista[j - gap] > temp)
            {
                lista[j] = lista[j - gap];
                j -= gap;
            }
            lista[j] = temp;
        }
        
        printVector(lista);

        gap = gap/2; // Reducir el gap
    }
}

//Creamos la función de ordenamiento por método shell variante Knuth:
void Shell_Knuth(vector<int>& lista)
{
    int n = lista.size();
    int gap, temp;
    gap = 1;

    // Calculamos el valor inicial de gap
    while (gap <= n/3)
        gap = gap * 3 + 1;

    // Comienza con la sublista más grande y la reduce en cada iteración
    while (gap > 0){
        for(int i = gap; i < n; i++){
            temp = lista[i];
            int j = i;
            // Inserta el elemento en la posición correcta dentro de su sublista
            while ((j >= gap) && (lista[j - gap] > temp)){
                lista[j] = lista[j - gap];
                j -= gap;
            }
            lista[j] = temp;
        }
        // Reducimos la sublista
        gap = gap / 3;
        printVector(lista);
    }
}

//Creamos la función de ordenamiento por método shell variante Hibbard:
void Shell_Hibbard(vector<int>& lista)
{
    int n,gap,temp;
    n=lista.size();
    gap=1;

    //Calculamos el tamaño inicial del contadorSublistas usando la secuencia de Hibbard
    while (gap<n/3)
        gap = gap*2+1;

    //Comenzamos con el contadorSublistas más grande y lo reducimos en cada iteración
    while (gap>0){
        //Insertamos los valores en orden
        for(int i=gap;i<n;i++){
            temp = lista[i];
            int j = i;

            while ((j>=gap) && (lista[j-gap]>temp)){
                lista[j] = lista[j-gap];
                j -= gap;
            }
            lista[j] = temp;
        }
        //Reducimos el contadorSublistas
        gap = (gap-1)/2;
        printVector(lista);
    }
}

//Creamos la función de ordenamiento por método de mezcla:
void Mezcla(vector<int>& lista)
{
    int n,medio,i,j,k;
    vector<int> izq,der;
    n=lista.size();

    if (n>1)
    {
        //Buscamos el medio de la lista:
        medio=n/2;

        //Dividimos la lista en 2 por la mitad:
        izq.assign(lista.begin(), lista.begin() + medio);
        der.assign(lista.begin()+medio, lista.end());

        Mezcla(izq);
        Mezcla(der);

        i=j=k=0;

        //Copiamos el contenido de las listas izq y der
        while ((i < izq.size()) && (j < der.size())){
            if (izq[i] <= der[j]){
                lista[k] = izq[i];
                i += 1;
            }
            else{
                lista[k] = der[j];
                j += 1;
            }
            k += 1;
        }
        //Comprobamos si quedan elementos por ordenar
        while (i < izq.size()){
            lista[k] = izq[i];
            i += 1;
            k += 1;
        }
        while (j < der.size()){
            lista[k] = der[j];
            j += 1;
            k += 1;
        }
        printVector(lista);
    }
}

//Creamos funciones de ordenamiento por método de Quicksort para cada una de las opciones de pivote
//Entramos en la función de partición para cuando el pivote elegido es el primer elemento:
int partition1(vector<int>& lista, int low, int high, int pivote) {
    int i = low + 1;
    int j = high;

    while (true) {
        while (i <= j && lista[i] <= pivote) {
            i++;
        }
        while (i <= j && lista[j] >= pivote) {
            j--;
        }
        if (i <= j) {
            swap(lista[i], lista[j]);
        } else {
            break;
        }
    }
    //Devolvemos el pivote a donde corresponde:
    swap(lista[low], lista[j]);
    return j;
}

//Si se elige el primer elemento como pivote se ejecuta este código:
void Quicksort_primero(vector<int>& lista, int izq, int der) {
    if (izq < der) {
        printVector(lista); //Imprimimos la lista para ir viendo como va variando
        //Llamamos a la función que lo va a ir ordenando:
        int pi = partition1(lista, izq, der, lista[izq]);
        //Hacemos llamadas recursivas para seguir ordenando la lista:
        Quicksort_primero(lista, izq, pi - 1);
        Quicksort_primero(lista, pi + 1, der);
        printVector(lista); //Imprimimos la lista para ir viendo como va variando
    }
}

//Entramos en la función de partición para cuando el pivote elegido es el último elemento:
int partition2(vector<int>& lista, int low, int high, int pivot) {
    int i = low - 1;
    
    //Vamos recorriendo la lista entre los extremos que queremos ordenar:
    for (int j = low; j < high; j++) {
        if (lista[j] <= pivot) {
            i++;
            swap(lista[i], lista[j]); //Intercambiamos el valor en la posición con con el de la posición j
        }
    }
    //Devolvemos el pivote, el cual colocáramos en la última posición, a donde estaba:
    swap(lista[i + 1], lista[high]);
    return i + 1;
}

//Si se elige el último elemento como pivote se ejecuta esta función:
void Quicksort_ultimo(vector<int>& lista, int izq, int der) {
    if (izq < der) {
        printVector(lista); //Imprimimos la lista para ir viendo como va variando
        //Llamamos a la función que lo va a ir ordenando:
        int pi = partition2(lista, izq, der, lista[der]);
        //Hacemos llamadas recursivas para seguir ordenando la lista:
        Quicksort_ultimo(lista, izq, pi - 1);
        Quicksort_ultimo(lista, pi + 1, der);
        printVector(lista); //Imprimimos la lista para ir viendo como va variando
    }
}

//Entramos en la función de partición para cuando el pivote elegido es un elemento aleatorio:
int partition3(vector<int>& lista, int low, int high, int pivot, int pivot_index) {
    swap(lista[pivot_index], lista[high]);
    int i = low - 1;
    
    //Vamos recorriendo la lista entre los extremos que queremos ordenar:
    for (int j = low; j < high; j++) {
        if (lista[j] <= pivot) {
            i++;
            swap(lista[i], lista[j]); //Intercambiamos el valor en la posición con con el de la posición j
        }
    }
    //Devolvemos el pivote, el cual colocáramos en la última posición, a donde estaba:
    swap(lista[i + 1], lista[high]);
    return i + 1;
}

//Si se elige un elemento aleatorio como pivote se ejecuta esta función
void Quicksort_aleatorio(vector<int>& lista, int izq, int der) {
    if (izq < der) {
        //Elegimos un índice aleatorio de la lista para que sea el pivote
        int pos_pivote = rand() % (der - izq + 1) + izq;
        printVector(lista); //Imprimimos la lista para ir viendo como va variando
        //Llamamos a la función que lo va a ir ordenando:
        int pi = partition3(lista, izq, der, lista[pos_pivote], pos_pivote);
        //Hacemos llamadas recursivas para seguir ordenando la lista:
        Quicksort_aleatorio(lista, izq, pi - 1);
        Quicksort_aleatorio(lista, pi + 1, der);
        printVector(lista); //Imprimimos la lista para ir viendo como va variando
    }
}

//Entramos en la función de partición para cuando el pivote elegido es la mediana:
int partition4(vector<int>& lista, int low, int high, int pivote) {
    int i = low - 1;

    //Vamos recorriendo la lista entre los extremos que queremos ordenar:
    for (int j = low; j < high; j++) {
        if (lista[j] <= pivote) {
            i++;
            swap(lista[i], lista[j]); //Intercambiamos el valor en la posición con con el de la posición j
        }
    }
    //Devolvemos el pivote, el cual colocáramos en la última posición, a donde estaba:
    swap(lista[i + 1], lista[high]);
    return i + 1;
}

//Calculamos la mediana entre el primer valor, el último y el del medio
int median_of_three(vector<int>& lista, int low, int high) {
    int mid = (low + high) / 2; //Calculamos cual es el medio
    //Vamos poniendo condiciones para ver cual es la mediana y que valor tenemos que devolver:
    if (lista[low] < lista[mid]) {
        if (lista[mid] < lista[high]) {
            return mid;
        } else if (lista[low] < lista[high]) {
            return high;
        } else {
            return low;
        }
    } else {
        if (lista[low] < lista[high]) {
            return low;
        } else if (lista[mid] < lista[high]) {
            return high;
        } else {
            return mid;
        }
    }
}

//Si se elige la mediana como pivote se ejecuta este código:
void Quicksort_mediana(vector<int>& lista, int izq, int der) {
    if (izq < der) {
        //Calculamos cual va a ser el pivote haciendo la mediana
        int pivot_index = median_of_three(lista, izq, der);
        //Pasamos el pivote al último elemento de la lista
        swap(lista[pivot_index], lista[der]);
        printVector(lista); //Imprimimos la lista para ir viendo como va variando
        //Llamamos a la función que lo va a ir ordenando:
        int pi = partition4(lista, izq, der, lista[der]);
        //Hacemos llamadas recursivas para seguir ordenando la lista:
        Quicksort_mediana(lista, izq, pi - 1);
        Quicksort_mediana(lista, pi + 1, der);
        printVector(lista); //Imprimimos la lista para ir viendo como va variando
    }
}

//Función que dependiendo de que pivote elijas llama a un quicksort o a otro para ordenar la lista
void Quicksort(vector<int>& lista){
    int pivote=Elegir_Pivote(lista);

    if (pivote==1){
        Quicksort_primero(lista,0,lista.size()-1);
    }
    else if (pivote==2){
        Quicksort_ultimo(lista,0,lista.size()-1);
    }
    else if (pivote==3){
        Quicksort_aleatorio(lista,0,lista.size()-1);
    }
    else if (pivote==4){
        Quicksort_mediana(lista,0,lista.size()-1);
    }}

//Definimos una función que es un menú para preguntar que pivote quieren para el quicksort. Está validado
int Elegir_Pivote(vector<int>& lista)
{
    int x;
    while (true) //Estamos en un bucle infinito hasta que se introduzca una respuesta válida
    {
        try{
            //Creamos un menú para preguntar que pivote quieren utilizar:
            cout<<"Que pivote quieres utilizar? (Hay varias opciones): "<<endl;
            cout<<"El pivote será el primer elemento (Pulsa 1)"<<endl;
            cout<<"El pivote será el último elemento (Pulsa 2)"<<endl;
            cout<<"El pivote será un elemento aleatorio (Pulsa 3)"<<endl;
            cout<<"El pivote será la mediana entre el primer, el último y el elemento del medio (Pulsa 4)"<<endl;
            cout<<"Cual de las opciones eliges? ";
            cin>>x;
            if(cin.fail())
            {
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                throw 1; //Si introduces un caracter no numérico lanza un error
            }
            if ((x==1)||(x==2)||(x==3)||(x==4)){
                return x; //Devuelve la opción que diste
            }
            else{
                cout<<("Ese no es un valor válido. Vuelva a introducirlo.")<<endl;
            }
        }
        catch(...){
            cout<<("El valor debía ser numérico. Vuelva a introducirlo.")<<endl;
        }
    }
}

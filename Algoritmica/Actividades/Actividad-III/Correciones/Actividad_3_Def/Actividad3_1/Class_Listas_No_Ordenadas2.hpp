#include <iostream>
#include <ostream>
using namespace std;
//Se crea la clase Nodo
class Node
{
    //Se definen data y next como punteros
private:
    int data;   //data en el nodo inicial
    Node *next; //puntero al siguiente nodo

public:
    Node(int initdata)
    {
        data = initdata; //los datos inicializados son establecidos como la cabeza
        next = NULL;     //el siguiente nodo se establece como nulo, ya que aun no hay siguiente nodo
    }

    int getData()
    { //funcion que devuelve los datos del nodo
        return data;
    }

    Node *getNext()
    { //puntero que consiguie el siguiente nodo
        return next;
    }

    void setData(int newData)
    { //ingresa los datos en el nodo
        data = newData;
    }

    void setNext(Node *newnext)
    { //Indica el siguiente nodo
        next = newnext;
    }
};

//Clase que usa nodos para crear una lista no ordenada
class ListaNoOrdenada
{
public:
    Node *head;
    int valoractual = 0;

    ListaNoOrdenada()
    { //Crea la lista, estableciendo la cabeza como nula
        head = NULL;
    }

    bool estavacia()
    { //Funcion que indica si la lista esta vacia. Esta vacia si la cabeza es nula
        return head == NULL; 
    }

    void agregar(int item)
    { //Funcion que permite anhadir un item a la lista. Se crea un puntero temporal que anhade el nuevo nodo a la cabeza
        Node *temp = new Node(item);
        temp->setNext(head);
        head = temp;
    }

    int tamano()
    {  //Funcion que indica el tamanho de la lista. 
        Node *current = head;
        int count = 0;
        while (current != NULL)
        {
            count++;
            current = current->getNext();
        }

        return count;
    }
    void anexar(const ListaNoOrdenada &ol)
    {
        //Coloca los elementos de la lista que entra como argumento despues de los elementos de la lista principal
        Node *current = ol.head;
        int item = 0;
        while (current != NULL)
        {
            //Recorre toda la lista ol
            item = current->getData();
            current = current->getNext();
            //Anexar
            Node *temp = new Node(item);
            temp->setNext(head);
            head = temp;
        }
    }

    int fin()
    {
        //Devolvera el ultimo valor de la lista
        Node *current = head;
        int valor = 0;
        while (current != NULL)
        {
            valor = current->getData();
            current = current->getNext();
        }
        return valor;
    }

    int primero()
    {
        //Devolvera el primer valor de la lista
        Node *current = head;
        int valor = 0;
        valor = current->getData();
        return valor;
    }

    int siguiente()
    {
        //Siempre empezara por el primer valor
        Node *current = head;
        int n = 0;
        int valor = 0;
        valoractual = valoractual + 1; //Posicion en la que va a buscar
        while (n != valoractual)
        {
            n = n + 1;
            valor = current->getData();
            current = current->getNext();
        }
        return valor;
        
    }

    int anterior()
    {
        if (valoractual <= 0)
            return 0;
        //Siempre empezara por el primer valor
        Node *current = head;
        int n = 0;
        int valor = 0;
        valoractual = valoractual - 1; //Posicion en la que va a buscar
        while (n != valoractual)
        {
            n = n + 1;
            valor = current->getData();
            current = current->getNext();
        }
        return valor;
        
    }

    bool buscar(int item)
    {
        Node *current = head;
        while (current != NULL)
            if (current->getData() == item)
                return true;
            else
                current = current->getNext();
        return false;
    }

    int indice(int a)
    {
        Node *current = head;
        int count = 0;
        int valor = 0;
        while ((current != NULL) and (count != a))
        {
            valor = current->getData();
            current = current->getNext();
            count++;

        }
        return valor;
    }
    int extraer(int pos)
    {   //Elimina y devuelve el item de la posicion pos
        Node *current = head;
        Node *previous = NULL;
        int n = 0;
        int resultado = 0;
        bool found = false;
        while (!found)
        {
            if (pos == n)
            {
                resultado = current->getData();
                found = true;
            }
            else
            {
                previous = current;
                current = current->getNext();
            }
            n++;
        }
        if (previous == NULL)
            head = current->getNext();
        else
            previous->setNext(current->getNext());
        return resultado;
    }

    void insertar(int pos, int item)
    {   //Se anhade el valor 'item' a la posicion 'pos'
        //La variable 'pos' no puede ser 0, ya que para eso ya existe el metodo 'agregar'
        Node *nuevo = new Node(item);
        Node *current = head;
        Node *previous = NULL;
        int n = 0;
        bool found = false;
        while (!found)
        {
            if (n == pos)
            {
                nuevo->setNext(current);
                previous->setNext(nuevo);
                found = true;
            }
            else
            {
                previous = current;
                current = current->getNext();
            }
            n++;
        }
    }

    int extraer()
    {   //Elimina y devuelve el ultimo item de la lista
        int pos = this->tamano() -1;
        Node *current = head;
        Node *previous = NULL;
        int n = 0;
        int resultado = 0;
        bool found = false;
        while (!found)
        {
            if (pos == n)
            {
                resultado = current->getData();
                found = true;
            }
            else
            {
                previous = current;
                current = current->getNext();
            }
            n++;
        }
        if (previous == NULL)
            head = current->getNext();
        else
            previous->setNext(current->getNext());
        return resultado;
    }

    // uses current and previous pointer to iterate through the lists
    // finds the items that is searched for, and removes it

    void borrar(int item)
    {
        Node *current = head;
        Node *previous = NULL;
        bool found = false;
        while (!found)
            if (current->getData() == item)
                found = true;
            else
            {
                previous = current;
                current = current->getNext();
            }
        if (previous == NULL)
            head = current->getNext();
        else
            previous->setNext(current->getNext());
    }

    friend ostream& operator<<(ostream& os, const ListaNoOrdenada& ol);
};

ostream &operator<<(ostream &os, const ListaNoOrdenada &ol)
{
    Node *current = ol.head;
    while (current != NULL)
    {
        os << current->getData() << endl;
        current = current->getNext();
    }
    return os;
}
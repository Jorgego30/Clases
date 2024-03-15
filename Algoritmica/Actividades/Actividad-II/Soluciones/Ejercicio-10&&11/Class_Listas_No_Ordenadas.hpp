#include <iostream>
#include <ostream>
using namespace std;
//creates a node class
class Node
{
    //defines data, and next as a pointer.
private:
    int data;   //data in the beginning node
    Node *next; //pointer to the next node

public:
    Node(int initdata)
    {
        data = initdata; //the initialized data is set as the head
        next = NULL;     //the next node is set as NULL, as there is no next node yet.
    }

    int getData()
    { //function that return data of a given node.
        return data;
    }

    Node *getNext()
    { // pointer that gets the next node
        return next;
    }

    void setData(int newData)
    { // sets data in node
        data = newData;
    }

    void setNext(Node *newnext)
    {
        next = newnext;
    }
};

// creates unorderedlist that points to the head of the linked list
class UnorderedList
{
public:
    Node *head;

    UnorderedList()
    { // makes the head node equal to null
        head = NULL;
    }

    bool isEmpty()
    { // the head node is empty if it is null
        return head == NULL;
    }

    void add(int item)
    { //cerates a "temp" pointer that adds the new node to the head of the list
        Node *temp = new Node(item);
        temp->setNext(head);
        head = temp;
    }

    void anexar(UnorderedList mySecondList){
    Node *current = mySecondList.head;
    while (current != NULL){
        // Agregar el elemento actual de la segunda lista a la primera lista
        add(current->getData()); 
        current = current->getNext();
        }
    }

    int size()
    { //cereates a "current" pointer that iterates through the list until it reaches null
        Node *current = head;
        int count = 0;
        while (current != NULL)
        {
            count++;
            current = current->getNext();
        }

        return count;
    }

    // creates "current" pointer that iterates through the list
    // untli it finds the item being searched for, and returns a boolean value

    bool search(int item)
    {
        Node *current = head;
        while (current != NULL)
            if (current->getData() == item)
                return true;
            else
                current = current->getNext();
        return false;
    }

    // uses current and previous pointer to iterate through the lists
    // finds the items that is searched for, and removes it

    void remove(int item)
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

    friend ostream& operator<<(ostream& os, const UnorderedList& ol);
  
    int inicio() const {
        return head->getData();
    }

    int fin() const {

        Node *current = head;
        while (current->getNext() != nullptr) {
            current = current->getNext(); 
        }

        return current->getData(); 
    }

    int siguiente(int valor) const {
        Node* current = head;

        // Buscar el nodo con el valor proporcionado
        while (current != nullptr && current->getData() != valor) {
            current = current->getNext();
        }

        // Verificar si se encontró el nodo
        if (current != nullptr && current->getNext() != nullptr) {
            // Devolver el valor del nodo siguiente
            return current->getNext()->getData();
        } else {
            // Si el nodo no se encontró o es el último de la lista, devolver un valor predeterminado
            cerr << "No se pudo encontrar el nodo siguiente para el valor dado." << endl;
            return -1; // Valor predeterminado en caso de que no se encuentre el nodo siguiente
        }
    }

    int anterior(int valor) const {
        if (head == nullptr) {
            // Si la lista está vacía, no hay nodo anterior
            cerr << "La lista está vacía." << endl;
            return -1; // Valor predeterminado en caso de lista vacía
        }

        // Caso especial: Si el valor proporcionado es el primero en la lista, no tiene nodo anterior
        if (head->getData() == valor) {
            cerr << "El valor proporcionado es el primero en la lista y no tiene nodo anterior." << endl;
            return -1; // Valor predeterminado para el primer nodo
        }

        Node* current = head;
        while (current->getNext() != nullptr) {
            if (current->getNext()->getData() == valor) {
                // Si se encuentra el nodo con el valor dado, devolver el valor del nodo actual
                return current->getData();
            }
            current = current->getNext();
        }

        // Si no se encontró el nodo con el valor proporcionado, o si es el último nodo de la lista
        cerr << "No se pudo encontrar el nodo anterior para el valor dado." << endl;
        return -1; // Valor predeterminado en caso de que no se encuentre el nodo anterior
    }


};

ostream &operator<<(ostream &os, const UnorderedList &ol)
{
    Node *current = ol.head;
    while (current != NULL)
    {
        os << current->getData() << endl;
        current = current->getNext();
    }
    return os;
}

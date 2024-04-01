#include <iostream>
using namespace std;

class Node
{
private:
    int data;
    Node *next;

public:
    Node(int initdata)
    {
        data = initdata;
        next = NULL;
    }

    int getData()
    {
        return data;
    }

    Node *getNext()
    {
        return next;
    }

    void setData(int newData)
    {
        data = newData;
    }

    void setNext(Node *newnext)
    {
        next = newnext;
    }
};

class UnorderedList
{
public:
    Node *head;

    UnorderedList()
    {
        head = NULL;
    }

    bool isEmpty()
    {
        return head == NULL;
    }

    void add(int item)
    {
        Node *temp = new Node(item);
        temp->setNext(head);
        head = temp;
    }

    int size()
    {
        Node *current = head;
        int count = 0;
        while (current != NULL)
        {
            count++;
            current = current->getNext();
        }

        return count;
    }

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

    void append(UnorderedList &otherList)
    {
        if (head == NULL)
        {
            head = otherList.head;
        }
        else
        {
            Node *current = head;
            while (current->getNext() != NULL)
            {
                current = current->getNext();
            }
            current->setNext(otherList.head);
        }
        otherList.head = NULL;
    }

    friend ostream &operator<<(ostream &os, const UnorderedList &ol);
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

int main()
{
    // Crear una lista no ordenada
    UnorderedList lista1;

    // Agregar elementos a la lista
    lista1.add(1);
    lista1.add(2);
    lista1.add(3);

    // Imprimir la lista
    cout << "Lista 1:" << endl;
    cout << lista1;

    // Crear otra lista no ordenada
    UnorderedList lista2;

    // Agregar elementos a la segunda lista
    lista2.add(4);
    lista2.add(5);
    lista2.add(6);

    // Imprimir la segunda lista
    cout << "Lista 2:" << endl;
    cout << lista2;

    // Agregar la segunda lista a la primera
    lista1.append(lista2);

    // Imprimir la primera lista después de la concatenación
    cout << "Lista 1 después de anexar la Lista 2:" << endl;
    cout << lista1;

    return 0;
}

//La complejidad de tiempo del método anexar depende del tamaño de la lista actual y la longitud de la otra lista. Si la lista actual tiene nn elementos y la otra lista tiene mm elementos, la complejidad de tiempo del método anexar es O(n)O(n), ya que tenemos que encontrar el último nodo de la lista actual, lo que requiere un recorrido a través de la lista actual una vez.

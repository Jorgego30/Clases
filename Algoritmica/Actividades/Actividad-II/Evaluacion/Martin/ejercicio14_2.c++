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
private:
    Node *head;
    int size;

public:
    UnorderedList()
    {
        head = NULL;
        size = 0;
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
        size++;
    }

    int tamano()
    {
        return size;
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
        while (!found && current != NULL)
            if (current->getData() == item)
                found = true;
            else
            {
                previous = current;
                current = current->getNext();
            }
        if (found)
        {
            if (previous == NULL)
                head = current->getNext();
            else
                previous->setNext(current->getNext());
            delete current;
            size--;
        }
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
        size += otherList.size;
        otherList.head = NULL;
        otherList.size = 0;
    }

    friend ostream &operator<<(ostream &os, const UnorderedList &ol);
};

ostream &operator<<(ostream &os, const UnorderedList &ol)
{
    Node *current = ol.head;
    while (current != NULL)
    {
        os << current->getData() << " ";
        current = current->getNext();
    }
    return os;
}

int main()
{
    UnorderedList lista1;
    lista1.add(1);
    lista1.add(2);
    lista1.add(3);

    cout << "Tamaño de la lista 1: " << lista1.tamano() << endl;

    UnorderedList lista2;
    lista2.add(4);
    lista2.add(5);
    lista2.add(6);

    cout << "Tamaño de la lista 2: " << lista2.tamano() << endl;

    lista1.append(lista2);
    cout << "Tamaño de la lista 1 después de la concatenación: " << lista1.tamano() << endl;

    return 0;
}
//Con esta modificación, el método tamano() simplemente devuelve el valor del atributo size, que ya está actualizado cada vez que se añade o elimina un nodo de la lista. La complejidad del método tamano() ahora es O(1), ya que solo requiere una operación de acceso a una variable de clase para obtener el tamaño de la lista. No es necesario recorrer toda la lista para contar los nodos.
#include <iostream>
#include <ostream>
using namespace std;

class Node
{
private:
    int data;
    Node *next;

public:
    Node(int initdata)
    {
        data = initdata; //the nodes data.
        next = NULL;     //next will become a pointer to another Node object.
    }

    int getData()
    {
        //returns the data of the Node.
        return data;
    }

    Node *getNext()
    {
        //returns the next Node in the linked list.
        return next;
    }

    void setData(int newData)
    {
        //Changes the data of the Node.
        data = newData;
    }

    void setNext(Node *newnext)
    {
        //assigns the next item in the linked list.
        next = newnext;
    }
};

class OrderedList
{
public:
    Node *head; //The first Node of the linked list.

    OrderedList()
    {
        head = NULL;
    }

    bool search(int item)
    {
        //finds a Node that contains item in the linked list.
        Node *current = head;
        bool found = false;
        bool stop = false;
        while (current != NULL && !found && !stop)
            //iterates through the entire list until item is found.
            if (current->getData() == item)
                found = true;
            else
                if (current->getData() > item)
                    stop = true;
                else
                    current = current->getNext();

        return found;
    }

    void add(int item)
    {
        if (head == NULL)
        {
            Node *newNode = new Node(item);
            head = newNode;
        }
        else
        {
            Node *current = head;
            Node *previous = NULL;
            bool stop = false;
            while (current != NULL && !stop)
                if (current->getData() > item)
                //if the data of the current Node is greater than item:
                    stop = true;
                else
                {
                    previous = current;
                    current = current->getNext();
                }
            Node *temp = new Node(item);
            if (previous == NULL)
            {
                //sets the current head as temp's next item,
                //sets temp as the new head.
                temp->setNext(head);
                head = temp;
            }
            else
            {
                //sets the current Node as temp's next Node,
                //sets temp to previous's next Node.
                temp->setNext(current);
                previous->setNext(temp);
            }
        }
    }

    bool isEmpty()
    {
        //Returns true if the head is NULL.
        return head == NULL;
    }

    int size()
    {
        //returns the length of the linked list.
        Node *current = head;
        int count = 0;
        while (current != NULL)
        {
            count++;
            current = current->getNext();
        }

        return count;
    }

    friend ostream& operator<<(ostream& os, const OrderedList& ol);

    void borrar(int item){
        Node *current = head;
        Node *previous = NULL;

        // Buscamos el nodo que contiene el elemento a borrar
        while (current != NULL && current->getData() != item){
            previous = current;
            current = current->getNext();
        }

        // Si el nodo no se encuentra, salimos
        if (current == NULL)
            return;

        // Si el nodo a borrar es el primer nodo
        if (previous == NULL){
            head = current->getNext(); // El siguiente nodo se convierte en el nuevo nodo principal
            delete current;            // Borramos el nodo actual
        }
        else{
            previous->setNext(current->getNext()); // El siguiente nodo del anterior apunta al siguiente del actual
            delete current;                         // Borramos el nodo actual
        }
    }

    int indice(int item){
        Node *current = head;
        int index = 0;

        // Recorremos la lista enlazada para buscar el elemento
        while (current != NULL){
            if (current->getData() == item)
                return index; // Devolvemos el índice si encontramos el elemento

            current = current->getNext();
            index++;
        }

        // Si no encontramos el elemento, devolvemos -1
        return -1;
    }

    int extraer()
{
    if (isEmpty())
        return -1; // Devuelve -1 si la lista está vacía

    Node *current = head;
    Node *previous = NULL;

    // Avanzar hasta el último nodo
    while (current->getNext() != NULL)
    {
        previous = current;
        current = current->getNext();
    }

    int extractedData = current->getData(); // Guardamos el dato a extraer

    // Si hay más de un elemento en la lista
    if (previous != NULL)
    {
        previous->setNext(NULL); // El nodo anterior al último apunta a NULL
    }
    else
    {
        head = NULL; // Si solo hay un elemento en la lista, se establece head a NULL
    }

    delete current; // Liberamos la memoria del nodo extraído
    return extractedData; // Devolvemos el dato extraído
}

int extraer(int pos)
{
    if (pos < 0 || pos >= size() || isEmpty())
        return -1; // Devolver -1 si la posición está fuera de rango o la lista está vacía

    Node *current = head;
    Node *previous = NULL;
    int currentIndex = 0;

    // Avanzar hasta la posición indicada
    while (current != NULL && currentIndex != pos)
    {
        previous = current;
        current = current->getNext();
        currentIndex++;
    }

    // Si el nodo a extraer es el primer nodo
    if (previous == NULL)
    {
        head = current->getNext(); // El siguiente nodo se convierte en el nuevo nodo principal
    }
    else
    {
        previous->setNext(current->getNext()); // El siguiente nodo del anterior apunta al siguiente del actual
    }

    int extractedData = current->getData(); // Guardamos el dato a extraer
    delete current;                         // Liberamos la memoria del nodo extraído
    return extractedData;                   // Devolvemos el dato extraído
}



};

ostream &operator<<(ostream &os, const OrderedList &ol)
{
    //operator for printing the data of every Node in the list.
    Node *current = ol.head;
    while (current != NULL)
    {
        os << current->getData() << endl;
        current = current->getNext();
    }
    return os;
}
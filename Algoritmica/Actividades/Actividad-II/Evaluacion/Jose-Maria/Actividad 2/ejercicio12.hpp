/*Implementar los métodos no desarrollados en el TAD ListaOrdenada, así como los
métodos borrar, indice, extraer y extraer(pos)*/


//Importamos las libreria snecesarias 
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
    void borrar(int item)
    {
        if (head == NULL) {
            return;
        }
        Node *current = head;
        Node *previous = NULL;
        while (current != NULL && current->getData() != item) {
            previous = current;
            current = current->getNext();
        }
        if (current == NULL) {
            return;
        }
        if (previous == NULL) {
            head = current->getNext();
        } else {
            previous->setNext(current->getNext());
        }
        delete current;
    }

    int indice(int item)
    {
        Node *current = head;
        int index = 0;
        while (current != NULL && current->getData() != item) {
            current = current->getNext();
            index++;
        }
        if (current == NULL) {
            return -1;
        }
        return index;
    }

    int extraer()
    {
        if (head == NULL) {
            return -1;
        }
        int data = head->getData();
        Node *temp = head;
        head = head->getNext();
        delete temp;
        return data;
    }

    int extraer_pos(int pos)
    {
        if (head == NULL) {
            return -1;
        }
        if (pos == 0) {
            return extraer();
        }
        Node *current = head;
        Node *previous = NULL;
        int index = 0;
        while (current != NULL && index != pos) {
            previous = current;
            current = current->getNext();
            index++;
        }
        if (current == NULL) {
            return -1;
        }
        int data = current->getData();
        previous->setNext(current->getNext());
        delete current;
        return data;
    }


    friend ostream& operator<<(ostream& os, const OrderedList& ol);
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


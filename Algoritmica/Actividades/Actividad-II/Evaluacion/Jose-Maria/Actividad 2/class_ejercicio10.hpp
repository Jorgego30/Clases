//Importamos las librerias necesairas 

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

    void anexar_lista(UnorderedList lista2){
        while(lista2.isEmpty() == false){
            Node *l = lista2.head;
            int a = l->getData();

            Node *temp = new Node(a);
            temp->setNext(head);
            head = temp;            

            lista2.remove(a);
        }
    }

    friend ostream& operator<<(ostream& os, const UnorderedList& ol);
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
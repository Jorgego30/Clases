#include <iostream>
using namespace std;

class Node {
private:
    int data;
    Node* next;

public:
    Node(int initdata) {
        data = initdata;
        next = nullptr;
    }

    int getData() {
        return data;
    }

    Node* getNext() {
        return next;
    }

    void setData(int newData) {
        data = newData;
    }

    void setNext(Node* newnext) {
        next = newnext;
    }
};

class UnorderedList {
private:
    Node* head;

public:
    UnorderedList() {
        head = nullptr;
    }

    bool isEmpty() {
        return head == nullptr;
    }

    void add(int item) {
        Node* temp = new Node(item);
        temp->setNext(head);
        head = temp;
    }

    int size() {
        Node* current = head;
        int count = 0;
        while (current != nullptr) {
            count++;
            current = current->getNext();
        }
        return count;
    }

    bool search(int item) {
        Node* current = head;
        while (current != nullptr) {
            if (current->getData() == item)
                return true;
            current = current->getNext();
        }
        return false;
    }

    void remove(int item) {
        Node* current = head;
        Node* previous = nullptr;
        bool found = false;
        while (!found && current != nullptr) {
            if (current->getData() == item)
                found = true;
            else {
                previous = current;
                current = current->getNext();
            }
        }
        if (found) {
            if (previous == nullptr)
                head = current->getNext();
            else
                previous->setNext(current->getNext());
            delete current;
        }
    }

    int fin() {
        if (isEmpty()) {
            cerr << "La lista está vacía." << endl;
            return -1; // Valor de retorno predeterminado si la lista está vacía
        }
        Node* current = head;
        while (current->getNext() != nullptr) {
            current = current->getNext();
        }
        return current->getData();
    }

    int primero() {
        if (isEmpty()) {
            cerr << "La lista está vacía." << endl;
            return -1; // Valor de retorno predeterminado si la lista está vacía
        }
        return head->getData();
    }

    int siguiente(int item) {
        Node* current = head;
        while (current != nullptr && current->getData() != item) {
            current = current->getNext();
        }
        if (current != nullptr && current->getNext() != nullptr) {
            return current->getNext()->getData();
        }
        cerr << "El elemento dado no está en la lista o es el último elemento." << endl;
        return -1; // Valor de retorno predeterminado si el elemento no se encuentra o es el último
    }

    int anterior(int item) {
        if (isEmpty() || head->getData() == item) {
            cerr << "No hay elementos anteriores o el elemento dado es el primero en la lista." << endl;
            return -1; // Valor de retorno predeterminado si no hay elementos anteriores o el elemento es el primero
        }
        Node* current = head;
        Node* previous = nullptr;
        while (current != nullptr && current->getData() != item) {
            previous = current;
            current = current->getNext();
        }
        if (current != nullptr && previous != nullptr) {
            return previous->getData();
        }
        cerr << "El elemento dado no está en la lista." << endl;
        return -1; // Valor de retorno predeterminado si el elemento no se encuentra en la lista
    }

    friend ostream& operator<<(ostream& os, const UnorderedList& ol);
};

ostream& operator<<(ostream& os, const UnorderedList& ol) {
    Node* current = ol.head;
    while (current != nullptr) {
        os << current->getData() << endl;
        current = current->getNext();
    }
    return os;
}

int main() {
    UnorderedList lista;
    lista.add(1);
    lista.add(2);
    lista.add(3);
    
    cout << "El último elemento de la lista es: " << lista.fin() << endl;
    cout << "El primer elemento de la lista es: " << lista.primero() << endl;
    cout << "El siguiente elemento después del 2 es: " << lista.siguiente(2) << endl;
    cout << "El elemento anterior al 3 es: " << lista.anterior(1) << endl;

    return 0;
}

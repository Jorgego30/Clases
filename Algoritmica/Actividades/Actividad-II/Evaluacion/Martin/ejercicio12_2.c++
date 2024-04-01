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

class OrderedList {
public:
    Node* head;

    OrderedList() {
        head = nullptr;
    }

    bool search(int item) {
        Node* current = head;
        bool found = false;
        while (current != nullptr && !found) {
            if (current->getData() == item)
                found = true;
            else if (current->getData() > item)
                break;
            else
                current = current->getNext();
        }
        return found;
    }

    void add(int item) {
        Node* temp = new Node(item);
        if (head == nullptr || head->getData() > item) {
            temp->setNext(head);
            head = temp;
        } else {
            Node* current = head;
            Node* previous = nullptr;
            while (current != nullptr && current->getData() < item) {
                previous = current;
                current = current->getNext();
            }
            temp->setNext(current);
            previous->setNext(temp);
        }
    }

    bool isEmpty() {
        return head == nullptr;
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

    void remove(int item) {
        if (isEmpty()) {
            cout << "La lista está vacía." << endl;
            return;
        }
        Node* current = head;
        Node* previous = nullptr;
        bool found = false;
        while (current != nullptr && !found) {
            if (current->getData() == item)
                found = true;
            else if (current->getData() > item)
                break;
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
        } else {
            cout << "El elemento no se encontró en la lista." << endl;
        }
    }

    int indice(int item) {
        Node* current = head;
        int index = 0;
        while (current != nullptr) {
            if (current->getData() == item)
                return index;
            else if (current->getData() > item)
                break;
            else {
                current = current->getNext();
                index++;
            }
        }
        return -1; // Si el elemento no se encuentra en la lista.
    }

    int extraer() {
        if (isEmpty()) {
            cerr << "La lista está vacía." << endl;
            return -1; // Valor de retorno predeterminado si la lista está vacía
        }
        Node* temp = head;
        int item = temp->getData();
        head = head->getNext();
        delete temp;
        return item;
    }

    int extraer(int pos) {
        if (isEmpty()) {
            cerr << "La lista está vacía." << endl;
            return -1; // Valor de retorno predeterminado si la lista está vacía
        }
        if (pos < 0) {
            cerr << "La posición no puede ser negativa." << endl;
            return -1; // Valor de retorno predeterminado si la posición es negativa
        }
        if (pos == 0) {
            return extraer(); // Si la posición es 0, extraer el primer elemento
        }
        Node* current = head;
        Node* previous = nullptr;
        int index = 0;
        while (current != nullptr && index < pos) {
            previous = current;
            current = current->getNext();
            index++;
        }
        if (current == nullptr) {
            cerr << "La posición está más allá del final de la lista." << endl;
            return -1; // Valor de retorno predeterminado si la posición está más allá del final de la lista
        }
        int item = current->getData();
        previous->setNext(current->getNext());
        delete current;
        return item;
    }

    friend ostream& operator<<(ostream& os, const OrderedList& ol);
};

ostream& operator<<(ostream& os, const OrderedList& ol) {
    Node* current = ol.head;
    while (current != nullptr) {
        os << current->getData() << endl;
        current = current->getNext();
    }
    return os;
}

int main() {
    OrderedList lista;
    lista.add(5);
    lista.add(3);
    lista.add(7);
    lista.add(4);
    
    cout << "Lista ordenada:" << endl;
    cout << lista << endl;

    cout << "El tamaño de la lista es: " << lista.size() << endl;
    cout << "El índice del elemento 7 es: " << lista.indice(7) << endl;

    cout << "Extrayendo el primer elemento: " << lista.extraer() << endl;
    cout << "Lista después de extraer el primer elemento:" << endl;
    cout << lista << endl;

    cout << "Extrayendo el elemento en la posición 1: " << lista.extraer(1) << endl;
    cout << "Lista después de extraer el elemento en la posición 1:" << endl;
    cout << lista << endl;

    return 0;
}

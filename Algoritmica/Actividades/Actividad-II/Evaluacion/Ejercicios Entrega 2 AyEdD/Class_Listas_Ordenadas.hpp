

class Node
{
private:
    int data;
    Node *next;

public:
    Node(int initdata)
    {
        data = initdata; 
        next = nullptr;     
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

class OrderedList
{
public:
    Node *head;

    OrderedList()
    {
        head = nullptr;
    }

    bool search(int item)
    {
        Node *current = head;
        bool found = false;
        bool stop = false;
        while (current != nullptr && !found && !stop)
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
        if (head == nullptr)
        {
            Node *newNode = new Node(item);
            head = newNode;
        }
        else
        {
            Node *current = head;
            Node *previous = nullptr;
            bool stop = false;
            while (current != nullptr && !stop)
                if (current->getData() > item)
                    stop = true;
                else
                {
                    previous = current;
                    current = current->getNext();
                }
            Node *temp = new Node(item);
            if (previous == nullptr)
            {
                temp->setNext(head);
                head = temp;
            }
            else
            {
                temp->setNext(current);
                previous->setNext(temp);
            }
        }
    }

    bool isEmpty()
    {
        return head == nullptr;
    }

    int size()
    {
        Node *current = head;
        int count = 0;
        while (current != nullptr)
        {
            count++;
            current = current->getNext();
        }

        return count;
    }


    int impresion()
    {
        Node *current = head;

        while (current->getNext() != nullptr)
        {
            current=current->getNext();
            cout << current->getData() << endl;
        }

        return current->getData(); 
    }

    void borraMayor()
    {
        Node *current = head;
        Node *previo = nullptr;

        while (current->getNext() != nullptr)
        {
            previo=current;
            current=current->getNext();
        }
        previo->setNext(nullptr);
    }
};






//Example code of a deque.

#include <iostream>
#include <deque>
#include <string>

using namespace std;

int main()
{
    deque<string> d;
    cout << "Deque Empty? " << d.empty() << endl;
    d.push_back("Zebra");
    cout << "Deque Empty? " << d.empty() << endl;

    d.push_front("Turtle"); //pushes to the front of the deque.
    d.push_front("Panda");
    d.push_back("Catfish"); //pushes to the back of the deque.
    d.push_back("Giraffe");

    cout << "Deque Size: " << d.size() << endl;
    cout << "Item at the front: " << d.front() << endl;
    cout << "Item at the back: " << d.back() << endl;

    cout << endl
         << "Items in the Deque: " << endl;
    int dsize = d.size();
    for (int i = 0; i < dsize; i++) //prints each item in the deque.
        cout << d.at(i) << " ";

    cout << endl;

    d.pop_back();
    d.pop_front();

    cout << endl
         << "Item at the front: " << d.front() << endl;
    cout << "Itm at the back: " << d.back() << endl;
    cout << "Deque Size: " << d.size() << endl;

    cout << endl
         << "Items in the Deque: " << endl;
    int dsize2 = d.size();
    for (int i = 0; i < dsize2; i++)
    {
        //prints each item in the deque.
        cout << d.at(i) << " ";

        return 0;
    }
}

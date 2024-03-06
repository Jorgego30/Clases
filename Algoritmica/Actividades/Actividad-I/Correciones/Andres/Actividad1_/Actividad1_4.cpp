#include "Class_fracionesC.hpp"
using namespace std;
int main()
{
    Fraction x(1, -2);
    Fraction y(2.1111110, 4);
    cout << x << " + " << y << " = " << x + y << endl;
    cout << x << " + " << y << " = " << x + y << endl;
    if (x == y)
        cout << "x is equal y" << endl;
    else
        cout << "x is not equal y" << endl;

    if (x <= y)
        cout << "x es menor o igual que y" << endl;
    else
        cout << "x no es menor o igual y" << endl;

    if (x >= y)
        cout << "x es mayor o igual que y" << endl;
    else
        cout << "x no es mayor o igual que y" << endl;

    if (x < y)
        cout << "x es menor que y" << endl;
    else
        cout << "x no es menor que y" << endl;

    if (x > y)
        cout << "x es mayor que y" << endl;
    else
        cout << "x no es mayor y" << endl;

    if (x != y)
        cout << "x no es y" << endl;
    else
        cout << "x es igual y" << endl;

}
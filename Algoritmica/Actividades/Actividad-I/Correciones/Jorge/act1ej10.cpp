#include "Class_Fracciones.hpp"
#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    Fraction x(1, -2);
    Fraction y(2, 2);
    cout << x << " + " << y << " = " << x + y << endl;
    cout<< x.getnum(x)<<endl;
    cout<< x.getdet(x)<<endl;
    cout<< y.getnum(y)<<endl;
    cout<< y.getdet(y)<<endl;
    if (x == y)
        cout << "x is equal y" << endl;
    else
        cout << "x is not equal y" << endl;
    if (x >> y)
        cout << "x mayor y" << endl;
    else
        cout << "x no es mayor y" << endl;
    if (x << y)
        cout << "x es menor y" << endl;
    else
        cout << "x no es menor y" << endl;
    if (x <= y)
        cout << "x es menor o igual y" << endl;
    else
        cout << "x no es menor o igual a y" << endl;
    if (x >= y)
        cout << "x es mayor o igual a y" << endl;
    else
        cout << "x no es mayor o igual a y" << endl;
    return 0;
}

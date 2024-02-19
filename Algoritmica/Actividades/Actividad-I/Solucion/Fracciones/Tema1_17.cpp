#include "Class_Fracciones.hpp"
int main(){

    Fraction x(1, -2);
    Fraction y(1, -2);
    cout << x << " + " << y << " = " << x + y << endl;
    cout << x << " - " << y << " = " << x - y << endl;
    cout << x << " * " << y << " = " << x * y << endl;
    cout << x << " / " << y << " = " << x / y << endl;

    cout << endl << "El numerador de " << x << " es: " <<  x.getNum() << endl;
    cout << endl << "El denominador de " << x << " es: " <<  x.getDen() << endl;
    if (x == y)
        cout << "x is equal y" << endl;
    if (x != y)
        cout << "x is not equal y" << endl;
    if (x < y)
        cout << "x is lower than y" << endl;
    if (x <= y)
        cout << "x is lower or equal y" << endl;
    if (x > y)
        cout << "x is lower than y" << endl;
    if (x >= y)
        cout << "x is bigger or equal y" << endl;
    return 0;
}

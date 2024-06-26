//Recursive example of converting from int to string.

#include <iostream>
#include <string>
using namespace std;

string toStr(int n, int base)
{
    string convertString = "0123456789ABCDEF";
    if (n < base)
        return string(1, convertString[n]); // converts char to string, and returns it
    else
        return toStr(n / base, base) + convertString[n % base]; // function makes a recursive call to itself.
}

int main()
{
    int number, base;
    cout << "Give me a natural number"<<endl;
    cin>>number;
    cout << "Give me a base <16"<<endl;
    cin>>base;    
    cout << toStr(number, base);
}

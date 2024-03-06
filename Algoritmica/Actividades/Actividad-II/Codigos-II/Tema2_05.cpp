////Tema2_05.cpp converts a decimal number into desired base 1-16.

#include <iostream>
#include <stack> // Calling Stack from the STL
#include <string>

using namespace std;

string baseConverter(int decNumber, int base)
{
    // performs the conversion process.
    string digits[] = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"};

    stack<int> remstack;

    while (decNumber > 0)
    {
        // adds the remainder after division of base, to the stack.
        int rem = decNumber % base;
        remstack.push(rem);
        decNumber = decNumber / base;
    }

    string newString = "";
    while (!remstack.empty())
    {
        // makes a string out of all the items in the stack.
        newString.append(digits[remstack.top()]);
        remstack.pop();
    }

    return newString;
}

int main()
{
    int mynum = 421;
    cout << baseConverter(mynum, 2) << endl;
    cout << baseConverter(mynum, 16) << endl;

    return 0;
}

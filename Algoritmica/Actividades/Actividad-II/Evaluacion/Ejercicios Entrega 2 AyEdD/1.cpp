#include <bits/stdc++.h>
using namespace std;
 
bool operador(char c)
{
    return (!isalpha(c) && !isdigit(c));
}
 
int prioridad(char C)
{
    if (C == '-' || C == '+')
        return 1;
    else if (C == '*' || C == '/')
        return 2;
    else if (C == '^')
        return 3;
    return 0;
}

string infijo2postfijo(string infijo)
{
    infijo = '(' + infijo + ')';
    int l = infijo.size();
    stack<char> char_stack;
    string output;
 
    for (int i = 0; i < l; i++) {
 

        if (isalpha(infijo[i]) || isdigit(infijo[i]))
            output += infijo[i];
 
        else if (infijo[i] == '(')
            char_stack.push('(');
 

        else if (infijo[i] == ')') {
            while (char_stack.top() != '(') {
                output += char_stack.top();
                char_stack.pop();
            }
 

            char_stack.pop();
        }
 
        else
        {
            if (operador(char_stack.top()))
            {
                if(infijo[i] == '^')
                {
                      while (prioridad(infijo[i]) <= prioridad(char_stack.top()))
                       {
                         output += char_stack.top();
                         char_stack.pop();
                       }
                     
                }
                else
                {
                    while (prioridad(infijo[i]) < prioridad(char_stack.top()))
                       {
                         output += char_stack.top();
                         char_stack.pop();
                       }
                     
                }
 
                char_stack.push(infijo[i]);
            }
        }
    }
      while(!char_stack.empty()){
          output += char_stack.top();
        char_stack.pop();
    }
    return output;
}
 
string infijo2prefijo(string infijo)
{

    int l = infijo.size();
 
    reverse(infijo.begin(), infijo.end());
 
    for (int i = 0; i < l; i++) {
 
        if (infijo[i] == '(') {
            infijo[i] = ')';
        }
        else if (infijo[i] == ')') {
            infijo[i] = '(';
        }
    }
 
    string prefix = infijo2postfijo(infijo);
 
    reverse(prefix.begin(), prefix.end());
 
    return prefix;
}

int main()
{
    string s = ("(a+b)*(c+d)*(e+f)");
    cout << "Infijo a prefijo de la expresion (a+b)*(c+d)*(e+f) :" << std::endl;
    cout << infijo2prefijo(s) << std::endl;

    string y = ("a+((b+c)*(d+e))");
    cout << "Infijo a prefijo de la expresion a+((b+c)*(d+e)) :" << std::endl;
    cout << infijo2prefijo(y) << std::endl;

    string x = ("a*b*c*d+e+f");
    cout << "Infijo a prefijo de la expresion a*b*c*d+e+f :" << std::endl;
    cout << infijo2prefijo(x) << std::endl;
    return 0;
}
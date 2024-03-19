#Implementa un algoritmo y el programa correspondiente para convertir las siguientes
#expresiones infijas a expresiones prefijas (usa el método de agrupar completamente) y
#evaluarlas dando valores a los operandos:

def infijo_a_prefijo(exp_infija):
    # Invertir la expresión infija original
    exp_infija = exp_infija[::-1]

    # Reemplazar paréntesis izquierdos por paréntesis derechos y viceversa
    exp_infija = exp_infija.replace('(', '_').replace(')', '(').replace('_', ')')

    # Convertir la expresión infija invertida y con los paréntesis reemplazados a postfija
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    pila_operadores = []
    exp_postfija = []
    for caracter in exp_infija:
        if caracter.isdigit() or caracter.isalpha():
            exp_postfija.append(caracter)
        elif caracter == '(':
            pila_operadores.append(caracter)
        elif caracter == ')':
            while pila_operadores[-1] != '(':
                exp_postfija.append(pila_operadores.pop())
            pila_operadores.pop()
        else:
            while pila_operadores and pila_operadores[-1] != '(' and precedencia[caracter] <= precedencia[pila_operadores[-1]]:
                exp_postfija.append(pila_operadores.pop())
            pila_operadores.append(caracter)
    while pila_operadores:
        exp_postfija.append(pila_operadores.pop())

    # Invertir la expresión postfija obtenida para obtener la expresión prefija
    exp_prefija = exp_postfija[::-1]
    return ''.join(exp_prefija)


exp_infija1 = '(A+B)*(C+D)*(E+F)'
exp_infija2 = 'A+((B+C)*(D+E))'
exp_infija3 = 'A*B*C*D+E+F'
exp_prefija1 = infijo_a_prefijo(exp_infija1)
exp_prefija2 = infijo_a_prefijo(exp_infija2)
exp_prefija3 = infijo_a_prefijo(exp_infija3)
print(exp_prefija1)
print(exp_prefija2)
print(exp_prefija3)
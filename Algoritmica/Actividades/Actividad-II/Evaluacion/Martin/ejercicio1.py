from clase_pila import *

def infijo_a_prefijo(expresion):
    precedencia = {'+': 1, '*': 2}
    operadores = Pila()
    prefijo = []

    for char in reversed(expresion):
        if char.isalnum():
            prefijo.append(char)
        elif char == ')':
            operadores.apilar(char)
        elif char == '(':
            while operadores.inspeccionar() != ')':
                prefijo.append(operadores.desapilar())
            operadores.desapilar()  # Descarta el '('
        else:
            while (not operadores.esta_vacia()) and (operadores.inspeccionar() != ')') and (precedencia.get(char, 0) <= precedencia.get(operadores.inspeccionar(), 0)):
                prefijo.append(operadores.desapilar())
            operadores.apilar(char)

    while not operadores.esta_vacia():
        prefijo.append(operadores.desapilar())

    return ''.join(reversed(prefijo))


def evaluar_prefijo(expresion, valores_operandos):
    operadores = Pila()

    for char in reversed(expresion):
        if char.isalnum():
            operadores.apilar(int(valores_operandos[char]))
        else:
            operando1 = operadores.desapilar()
            operando2 = operadores.desapilar()
            if char == '+':
                resultado = operando1 + operando2
            elif char == '*':
                resultado = operando1 * operando2
            operadores.apilar(resultado)

    return operadores.desapilar()


# Expresiones dadas
expresiones = [
    "(A+B)*(C+D)*(E+F)",
    "A+((B+C)*(D+E))",
    "A*B*C*D+E+F"
]

# Valores de los operandos
valores_operandos = {'A': 2, 'B': 3, 'C': 4, 'D': 5, 'E': 6, 'F': 7}

for expr in expresiones:
    prefijo_expr = infijo_a_prefijo(expr)
    print("Expresión prefija:", prefijo_expr)
    resultado = evaluar_prefijo(prefijo_expr, valores_operandos)
    print("Resultado de la expresión:", resultado)
    print()

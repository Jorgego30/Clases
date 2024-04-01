from Class_Estructuras_lineales import Pila


def evaluacionNotacionSufija(expresionSufija):
    pilaOperandos = Pila()
    listaSimbolos = expresionSufija.split()

    for simbolo in listaSimbolos:
        try: 
            variable=float(simbolo)
            pilaOperandos.incluir(variable)
        except:
            operando2 = pilaOperandos.extraer()
            operando1 = pilaOperandos.extraer()
            resultado = hacerAritmetica(simbolo, operando1, operando2)
            pilaOperandos.incluir(resultado)
    return pilaOperandos.extraer()


def hacerAritmetica(operador, operandoIzquierda, operandoDerecha):
    if operador == "*":
        return operandoIzquierda * operandoDerecha
    elif operador == "/":
        return operandoIzquierda / operandoDerecha
    elif operador == "+":
        return operandoIzquierda + operandoDerecha
    else:
        return operandoIzquierda - operandoDerecha


print(evaluacionNotacionSufija('4.5 5 6 * +'))
print(evaluacionNotacionSufija('7 8 + 3 2 + /'))

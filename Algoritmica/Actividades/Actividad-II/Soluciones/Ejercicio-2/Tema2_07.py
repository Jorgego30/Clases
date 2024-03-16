from Class_Estructuras_lineales import Pila


def evaluacionNotacionSufija(expresionSufija):
    pilaOperandos = Pila()
    listaSimbolos = expresionSufija.split()

    for simbolo in listaSimbolos:
        try:
            # Intentamos convertir el símbolo en un número (int o float)
            if "." in simbolo:
                operando = float(simbolo)
            else:
                operando = int(simbolo)
        except ValueError:
            # Si el símbolo no es un número, intentamos operar con él
            if simbolo in ['+', '-', '*', '/']:
                if pilaOperandos.tamano() < 2:
                    return "Error: Expresión inválida"
                operando2 = pilaOperandos.extraer()
                operando1 = pilaOperandos.extraer()
                try:
                    resultado = hacerAritmetica(simbolo, operando1, operando2)
                    pilaOperandos.incluir(resultado)
                except ZeroDivisionError:
                    return "Error: División por cero"
                except:
                    return "Error: Operador inválido"
            else:
                return "Error: Símbolo no reconocido"
        else:
            # Si el símbolo es un número, lo agregamos directamente a la pila
            pilaOperandos.incluir(operando)

    # Al final, si la pila tiene más de un elemento, la expresión era inválida
    if pilaOperandos.tamano() != 1:
        return "Error: Expresión inválida"
    else:
        return pilaOperandos.extraer()


def hacerAritmetica(operador, operandoIzquierda, operandoDerecha):
    if operador == "*":
        return operandoIzquierda * operandoDerecha
    elif operador == "/":
        if operandoDerecha == 0:
            raise ZeroDivisionError
        return operandoIzquierda / operandoDerecha
    elif operador == "+":
        return operandoIzquierda + operandoDerecha
    elif operador == "-":
        return operandoIzquierda - operandoDerecha
    else:
        raise ValueError("Operador no reconocido")


print(evaluacionNotacionSufija('42.5 5 6 * +'))  # Resultado esperado: 72.5
print(evaluacionNotacionSufija('72 8 + 3 2 + /'))  # Resultado esperado: 16.0
print(evaluacionNotacionSufija('3 0 /'))  # Resultado esperado: Error: División por cero
print(evaluacionNotacionSufija('10 2 %'))  # Resultado esperado: Error: Símbolo no reconocido

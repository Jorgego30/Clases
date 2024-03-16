from Class_Estructuras_lineales import Pila

def evaluacionNotacionSufija(expresionSufija):
    pilaOperandos = Pila()
    listaSimbolos = expresionSufija.split()

    print("Expresión Sufija:", expresionSufija)

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
                    print("Error: Expresión inválida")
                    return
                operando2 = pilaOperandos.extraer()
                operando1 = pilaOperandos.extraer()
                try:
                    resultado = hacerAritmetica(simbolo, operando1, operando2)
                    pilaOperandos.incluir(resultado)
                except ZeroDivisionError:
                    print("Error: División por cero")
                    return
                except:
                    print("Error: Operador inválido")
                    return
            else:
                print("Error: Símbolo no reconocido")
                return
        else:
            # Si el símbolo es un número, lo agregamos directamente a la pila
            pilaOperandos.incluir(operando)
        print("Pila:", pilaOperandos)

    # Al final, si la pila tiene más de un elemento, la expresión era inválida
    if pilaOperandos.tamano() != 1:
        print("Error: Expresión inválida")
    else:
        print("Resultado:", pilaOperandos.extraer())

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

# Evaluación de expresiones
evaluacionNotacionSufija('2.5 31 * 4 +')
evaluacionNotacionSufija('1.5 22 + 3 + 4 + 5 +')
evaluacionNotacionSufija('123 2.5 3.1 4 5 * + * +')

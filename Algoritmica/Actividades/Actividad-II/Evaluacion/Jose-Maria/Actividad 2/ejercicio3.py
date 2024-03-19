#Evalúa las siguientes expresiones sufijas. Muestra la pila a medida que es procesado 
#cada operando y cada operador.

def expresionsufija(expresion):
    pila=[]
    for elemento in expresion.split():
        if es_operando(elemento):
            pila.append(float(elemento))
            print(pila)
        elif es_operador(elemento):
            if len(pila) < 2:
                raise ValueError("Error: no hay suficientes operandos en la pila.")
            operando2 = pila.pop()
            operando1 = pila.pop()
            resultado = realizar_operacion(elemento, operando1, operando2)
            pila.append(resultado)
        else:
            raise ValueError("Error: elemento desconocido en la expresión.")
    if len(pila) != 1:
        raise ValueError("Error: la expresión no está bien formada.")
    return pila[0]

def es_operando(elemento):
    try:
        float(elemento)
        return True
    except ValueError:
        return False

def es_operador(elemento):
    return elemento in ["+", "-", "*", "/"]

def realizar_operacion(operador, operando1, operando2):
    if operador == "+":
        return operando1 + operando2
    elif operador == "-":
        return operando1 - operando2
    elif operador == "*":
        return operando1 * operando2
    elif operador == "/":
        return operando1 / operando2



c1=expresionsufija('1.5 22 + 3 + 4 + 5 +')
c2=expresionsufija('123 2.5 3.1 4 5 * + * +')
c=expresionsufija('2.5 31 * 4 +')
print("la primera expresion es ('2.5 31 * 4 +'):",c)

print(c1)
print(c2)

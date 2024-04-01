class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def inspeccionar(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None

    def esta_vacia(self):
        return len(self.items) == 0


def evaluar_sufijo(expresion):
    operadores = Pila()

    for token in expresion.split():
        try:
            operando = float(token)
            operadores.apilar(operando)
        except ValueError:
            if len(operadores.items) < 2:
                raise ValueError("Error: La expresión está mal formada")
            operando2 = operadores.desapilar()
            operando1 = operadores.desapilar()
            if token == '+':
                resultado = operando1 + operando2
            elif token == '*':
                resultado = operando1 * operando2
            operadores.apilar(resultado)

        print("Token procesado:", token)
        print("Pila:", operadores.items)
        print()

    if len(operadores.items) != 1:
        raise ValueError("Error: La expresión está mal formada")

    return operadores.desapilar()

# Expresiones sufijas dadas
expresiones_sufijas = [
    "2.5 31 * 4 +",
    "1.5 22 + 3 + 4 + 5 +",
    "123 2.5 3.1 4 5 * + * +"
]

# Procesar cada expresión y mostrar el proceso paso a paso
for expresion in expresiones_sufijas:
    print("Expresión sufija:", expresion)
    resultado = evaluar_sufijo(expresion)
    print("Resultado de la expresión:", resultado,'\n\n')
    print("------------------------------")

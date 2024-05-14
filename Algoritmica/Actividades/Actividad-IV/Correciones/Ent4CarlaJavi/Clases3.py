class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def encontrarSucesor(nodo):
    actual = nodo
    while actual.izquierda is not None:
        actual = actual.izquierda
    return actual

def recorridoInordenNoRecursivo(raiz):
    pila = []
    actual = raiz
    while True:
        if actual is not None:
            pila.append(actual)
            actual = actual.izquierda
        elif pila:
            actual = pila.pop()
            print(actual.valor, end=" ")
            actual = actual.derecha
        else:
            break

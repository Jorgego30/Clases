class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Cola:
    def __init__(self):
        self.inicio = None
        self.fin = None
        
    def es_vacia(self):
        return self.inicio == None
        
    def encolar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.es_vacia():
            self.inicio = nuevo_nodo
        else:
            self.fin.siguiente = nuevo_nodo
        self.fin = nuevo_nodo
        
    def desencolar(self):
        if self.es_vacia():
            return None
        else:
            valor = self.inicio.valor
            self.inicio = self.inicio.siguiente
            if self.inicio == None:
                self.fin = None
            return valor
        
    def imprimir(self):
        if self.es_vacia():
            print("Cola vacía.")
        else:
            actual = self.inicio
            while actual != None:
                print(actual.valor)
                actual = actual.siguiente
                
    def concatenar(self, otra_cola):
        if otra_cola.es_vacia():
            return
        elif self.es_vacia():
            self.inicio = otra_cola.inicio
            self.fin = otra_cola.fin
        else:
            self.fin.siguiente = otra_cola.inicio
            self.fin = otra_cola.fin
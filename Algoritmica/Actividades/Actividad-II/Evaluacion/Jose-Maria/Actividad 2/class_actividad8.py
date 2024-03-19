class Nodo:
    def __init__(self, valor, prioridad):
        self.valor = valor
        self.prioridad = prioridad
        self.siguiente = None
        
class ColaPrioridad:
    def __init__(self):
        self.inicio = None
        
    def es_vacia(self):
        return self.inicio == None
        
    def insertar(self, valor, prioridad):
        nuevo_nodo = Nodo(valor, prioridad)
        if self.es_vacia():
            self.inicio = nuevo_nodo
        elif self.inicio.prioridad < prioridad:
            nuevo_nodo.siguiente = self.inicio
            self.inicio = nuevo_nodo
        else:
            actual = self.inicio
            while actual.siguiente != None and actual.siguiente.prioridad >= prioridad:
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
            
    def eliminar(self):
        if self.es_vacia():
            return None
        else:
            valor = self.inicio.valor
            self.inicio = self.inicio.siguiente
            return valor
        
    def imprimir(self):
        if self.es_vacia():
            print("Cola de prioridad vacía.")
        else:
            actual = self.inicio
            while actual != None:
                print(actual.valor, " con prioridad ", actual.prioridad)
                actual = actual.siguiente
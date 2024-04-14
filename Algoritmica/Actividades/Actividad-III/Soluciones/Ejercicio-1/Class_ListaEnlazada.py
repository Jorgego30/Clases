class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def eliminar(self, dato):
        actual = self.cabeza
        if actual is None:
            return
        if actual.dato == dato:
            self.cabeza = actual.siguiente
            actual = None
            return
        while actual is not None:
            if actual.dato == dato:
                break
            previo = actual
            actual = actual.siguiente
        if actual is None:
            return
        previo.siguiente = actual.siguiente
        actual = None

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' ')
            actual = actual.siguiente
        print()

    def invertir_recursivamente(self, actual, previo=None):
        if actual is None:
            self.cabeza = previo
            return
        siguiente = actual.siguiente
        actual.siguiente = previo
        self.invertir_recursivamente(siguiente, actual)
class Nodo:
    def __init__(self, elemento, prioridad):
        self.elemento = elemento
        self.prioridad = prioridad
        self.siguiente = None

class ColaPrioridad:
    def __init__(self):
        self.cabeza = None

    def añade(self, elemento, prioridad):
        nuevo_nodo = Nodo(elemento, prioridad)
        if self.cabeza is None or prioridad < self.cabeza.prioridad:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None and actual.siguiente.prioridad <= prioridad:
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

    def primero(self):
        if self.cabeza is not None:
            return self.cabeza.elemento
        else:
            return None

    def extrae(self):
        if self.cabeza is not None:
            elemento_extraido = self.cabeza.elemento
            self.cabeza = self.cabeza.siguiente
            return elemento_extraido
        else:
            return None

    def tamaño(self):
        tamaño = 0
        actual = self.cabeza
        while actual is not None:
            tamaño += 1
            actual = actual.siguiente
        return tamaño

    def esta_vacia(self):
        return self.cabeza is None



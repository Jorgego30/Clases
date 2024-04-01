class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        return self.items.pop()

    def inspeccionar(self):
        return self.items[-1]

    def tamano(self):
        return len(self.items)
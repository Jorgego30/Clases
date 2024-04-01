class Cola:
    """ Representa a una cola, con operaciones de encolar y desencolar.
        El primero en ser encolado es también el primero en ser desencolado.
    """

    
    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa por una lista vacía
        self.items = []

    def __str__(self):
        cadena=''
        for elemento in self.items:
            cadena = cadena + str(elemento) + ' '
        return cadena
    
    def estaVacia(self):
        """ Devuelve True si la cola esta vacía, False si no."""
        return self.items == []

    def agregar(self, item):
        """ Agrega el elemento x como último de la cola. """
        self.items.insert(0,item)

    def avanzar(self):
        """ Elimina el primer elemento de la cola y devuelve su
        valor. 
        """
        return self.items.pop()

    def tamano(self):
        return len(self.items)

    def frente (self):
        return self.items[len(self.items)-1]

    def ultimo (self):
        if len(self.items)>0:
            return self.items[0]

    def encolar(self, item):
        self.items.append(item)

    def concatenar(self, otra_cola):
        for elemeneto in otra_cola.items:
            self.encolar(elemeneto)

cola1=Cola()
cola1.encolar(1)
cola1.encolar(2)

cola2=Cola()
cola2.encolar(3)
cola2.encolar(4)

print("Cola1: ",cola1.items)
print("Cola2:", cola2.items)

cola1.concatenar(cola2)
print("La cola concatenada es: ", cola1.items)

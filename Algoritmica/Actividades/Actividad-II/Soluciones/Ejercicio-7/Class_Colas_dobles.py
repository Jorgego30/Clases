#Colas_dobles.py
class ColaDoble:
    def __init__(self):
        """
            efecto: Crea una cola vacía. 
        """
        self.items = []

    def __str__(self):
        
        
        cadena=''
        for elemento in self.items:
            cadena = cadena + str(elemento) + ' '
        return cadena
    
    def estaVacia(self):
        """ 
            comprueba si la cola doble está vacía. Devuelve un valor booleano
        """
        return self.items == []

    def agregarFrente(self, item):
        """
            añade un nuevo ítem al frente de la cola doble. Necesita el ítem y no devuelve nada.
        """
        self.items.append(item)

    def agregarFinal(self, item):
        """
            añade un nuevo ítem en el final de la cola doble. Necesita el ítem y no devuelve nada.
        """
        self.items.insert(0,item)

    def borrarFrente(self):
        """
            elimina y devuelve el ítem que está en el frente de la cola doble. La cola doble se modifica.
        """
        return self.items.pop()

    def borrarFinal(self):
        """
            elimina y devuelve el ítem que está al final de la cola doble. La cola doble se modifica.
        """
        return self.items.pop(0)

    def tamano(self):
        """
            devuelve un entero que es el número de ítems en la cola doble.
        """
        return len(self.items)

    def frente (self):
        """
            Devuelve el primer elemento de la cola.
        """
        return self.items[len(self.items)-1]

    def ultimo (self):
        """
            Devuelve el ultimo elemento de la cola.
        """
        if len(self.items)>0:
            return self.items[0]
    
    def inspeccionar(self, index):
        """
            devuelve el ítem de la posición index de la cola, pero no lo elimina.
        """
        return self.items[index]

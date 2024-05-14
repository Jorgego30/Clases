"""8. Utilizando la clase MonticuloBinario, implementa una nueva clase llamada ColaPrioridad. Esta nueva
clase ColaPrioridad debe implementar el constructor, además de los métodos agregar y avanzar. """
from Clases8 import BinaryHeap

class PriorityQueue:
    def __init__(self):
        self.heap = BinaryHeap()

    def agregar(self, val):
        self.heap.insert(val)

    def avanzar(self):
        return self.heap.extract_max()

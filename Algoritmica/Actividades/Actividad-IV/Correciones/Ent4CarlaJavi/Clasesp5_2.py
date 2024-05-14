from Clasesp5 import BinaryHeap

class PriorityQueue:
    def __init__(self):
        self.heap = BinaryHeap()

    def agregar(self, clave, prioridad):
        self.heap.insert((clave, prioridad))

    def obtener_minimo(self):
        return self.heap.extract_max()

    def esta_vacia(self):
        return len(self.heap.heap) == 0

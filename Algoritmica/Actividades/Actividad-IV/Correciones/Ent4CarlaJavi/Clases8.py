"""8. Utilizando la clase MonticuloBinario, implementa una nueva clase llamada ColaPrioridad. Esta nueva
clase ColaPrioridad debe implementar el constructor, además de los métodos agregar y avanzar. """
class MonticuloBinario:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def max_heapify(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        largest = i
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

    def insert(self, key):
        self.heap.append(key)
        i = len(self.heap) - 1
        while i != 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.max_heapify(0)
        return max_value

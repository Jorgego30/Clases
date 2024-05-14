class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._percolate_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._percolate_down(0)
        return max_val

    def _percolate_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index][1] > self.heap[parent_index][1]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _percolate_down(self, index):
        while (2 * index) + 1 < len(self.heap):
            left_child_index = (2 * index) + 1
            right_child_index = (2 * index) + 2 if (2 * index) + 2 < len(self.heap) else None

            max_child_index = left_child_index
            if right_child_index is not None and self.heap[right_child_index][1] > self.heap[left_child_index][1]:
                max_child_index = right_child_index

            if self.heap[max_child_index][1] > self.heap[index][1]:
                self.heap[index], self.heap[max_child_index] = self.heap[max_child_index], self.heap[index]
                index = max_child_index
            else:
                break

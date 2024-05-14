class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self._insert_recursive(self.root, key, value)

    def _insert_recursive(self, root, key, value):
        if root is None:
            return Node(key, value)
        if key == root.key:
            root.value = value  # If key already exists, update the value
        elif key < root.key:
            root.left = self._insert_recursive(root.left, key, value)
        else:
            root.right = self._insert_recursive(root.right, key, value)
        return root

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)

    def inorder_traversal(self):
        self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, root):
        if root:
            self._inorder_traversal_recursive(root.left)
            print(f"Key: {root.key}, Value: {root.value}")
            self._inorder_traversal_recursive(root.right)

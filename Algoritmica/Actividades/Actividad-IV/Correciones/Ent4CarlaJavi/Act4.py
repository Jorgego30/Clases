from Clases4 import BinarySearchTree

# Creamos un árbol binario de búsqueda
bst = BinarySearchTree()

# Insertamos algunos elementos
bst.insert(10, "A")
bst.insert(5, "B")
bst.insert(15, "C")
bst.insert(3, "D")
bst.insert(7, "E")

# Imprimimos el árbol en orden
print("Árbol después de la inserción inicial:")
bst.inorder_traversal()

# Insertamos una clave existente con un nuevo valor
bst.insert(5, "F")

# Imprimimos el árbol después de la inserción de la clave existente
print("\nÁrbol después de la actualización de clave existente:")
bst.inorder_traversal()

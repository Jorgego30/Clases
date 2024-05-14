from Clases5 import Node, imprimirExpresion

# Creamos un árbol de expresión simple
#       +
#      / \
#     3   4
raiz = Node('+')
raiz.left = Node(3)
raiz.right = Node(4)

# Imprimimos la expresión
print("Expresión 1:")
imprimirExpresion(raiz)
print()

# Creamos otro árbol de expresión más complejo
#        +
#       / \
#      *   /
#     / \ / \
#    5  4 8  2
raiz2 = Node('+')
raiz2.left = Node('*')
raiz2.left.left = Node(5)
raiz2.left.right = Node(4)
raiz2.right = Node('/')
raiz2.right.left = Node(8)
raiz2.right.right = Node(2)

# Imprimimos la segunda expresión
print("Expresión 2:")
imprimirExpresion(raiz2)
print()

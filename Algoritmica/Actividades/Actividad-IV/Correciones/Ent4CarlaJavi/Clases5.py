class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def imprimirExpresion(root):
    if root is not None:
        # Si el nodo actual es un operador, agregamos paréntesis alrededor de los hijos
        if root.value in ['+', '-', '*', '/']:
            print("(", end="")
            imprimirExpresion(root.left)
            print(root.value, end="")
            imprimirExpresion(root.right)
            print(")", end="")
        else:
            # Si el nodo actual es un número, simplemente lo imprimimos sin paréntesis
            print(root.value, end="")

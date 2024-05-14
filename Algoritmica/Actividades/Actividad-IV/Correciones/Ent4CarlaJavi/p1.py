from Clasesp1 import ArbolBinario, Nodo

# Creamos un árbol binario de ejemplo
arbol = ArbolBinario()
arbol.raiz = Nodo(1)
arbol.raiz.izquierda = Nodo(2)
arbol.raiz.derecha = Nodo(3)
arbol.raiz.izquierda.izquierda = Nodo(4)
arbol.raiz.izquierda.derecha = Nodo(5)

# Verificamos las operaciones
print("Cantidad de nodos del árbol:", arbol.numNodos())
print("Número de hojas del árbol:", arbol.numHojas())
print("Profundidad del árbol:", arbol.profundidad())

# Creamos el espejo del árbol
arbol_espejo = arbol.espejo()

# Verificamos el árbol espejo
print("\nÁrbol original:")
print("         1")
print("       /   \\")
print("      2     3")
print("     / \\")
print("    4   5")

print("\nÁrbol espejo:")
print("         1")
print("       /   \\")
print("      3     2")
print("           / \\")
print("          5   4")

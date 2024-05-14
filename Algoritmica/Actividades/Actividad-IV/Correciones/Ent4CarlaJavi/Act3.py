'''Utilizando el método encontrarSucesor, escribe un recorrido inorden no recursivo para un árbol
binario de búsqueda.
'''

from Clases3 import Nodo, recorridoInordenNoRecursivo

# Crear el árbol binario de búsqueda
raiz = Nodo(10)
raiz.izquierda = Nodo(5)
raiz.derecha = Nodo(15)
raiz.izquierda.izquierda = Nodo(3)
raiz.izquierda.derecha = Nodo(7)
raiz.derecha.izquierda = Nodo(12)
raiz.derecha.derecha = Nodo(18)

# Realizar el recorrido inorden no recursivo
print("Recorrido Inorden No Recursivo:")
recorridoInordenNoRecursivo(raiz)



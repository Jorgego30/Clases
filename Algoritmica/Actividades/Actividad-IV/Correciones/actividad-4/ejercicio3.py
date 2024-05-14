'''Utilizando el método encontrarSucesor, escribe un recorrido inorden no recursivo para un árbol
binario de búsqueda'''

from class_Nodo import *

def encontrarSucesor(nodo):
    if nodo.derecha is not None:
        return encontrarMinimo(nodo.derecha)
    padre = nodo.padre
    while padre is not None and nodo == padre.derecha:
        nodo = padre
        padre = nodo.padre
    return padre

def encontrarMinimo(nodo):
    while nodo.izquierda is not None:
        nodo = nodo.izquierda
    return nodo

#Funcion que realiza un recorrido inorden no recursivo del árboly va metiendo todo en una pila

def inordenNoRecursivo(raiz):
    actual = raiz
    pila_principal = [] #Pila vacia 
    while True:
        while actual is not None:
            pila_principal.append(actual) #Introducimos en nuestra pila 
            actual = actual.izquierda
        if len(pila_principal) == 0:
            break
        actual = pila_principal.pop()
        print(actual.valor) #Printeamos en nuestra terminal 
        actual = actual.derecha

# Ejemplo de uso
raiz = Nodo(5)
raiz.izquierda = Nodo(3)
raiz.izquierda.padre = raiz
raiz.izquierda.izquierda = Nodo(2)
raiz.izquierda.izquierda.padre = raiz.izquierda
raiz.izquierda.derecha = Nodo(4)
raiz.izquierda.derecha.padre = raiz.izquierda
raiz.derecha = Nodo(8)
raiz.derecha.padre = raiz
raiz.derecha.izquierda = Nodo(6)
raiz.derecha.izquierda.padre = raiz.derecha
raiz.derecha.derecha = Nodo(9)
raiz.derecha.derecha.padre = raiz.derecha

#Mostramos nuestro resultado final

print("Recorrido inorden no recursivo:")


#Llamada a nuestra funcion inorden
inordenNoRecursivo(raiz)
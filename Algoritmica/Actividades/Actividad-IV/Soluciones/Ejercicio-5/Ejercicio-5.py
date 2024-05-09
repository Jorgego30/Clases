from Class_Arboles import *
from recorridos import *

arbol = ArbolBinario('+')
arbol.insertarIzquierdo('3')
arbol.insertarDerecho('*')
arbol.obtenerHijoDerecho().insertarIzquierdo('5')
arbol.obtenerHijoDerecho().insertarDerecho('2')

print("Expresión del árbol binario:", imprimirExpresion(arbol))

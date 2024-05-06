# Tema5_02
import arbol


r = arbol.ArbolBinario(3)
arbol.insertarIzquierdo(r, 4)
arbol.insertarIzquierdo(r, 5)
arbol.insertarDerecho(r, 6)
arbol.insertarDerecho(r, 7)
l = arbol.obtenerHijoIzquierdo(r)
print(l, "Hijo izdo")

arbol.asignarValorRaiz(l, 9)
print(r)
arbol.insertarIzquierdo(l, 11)
print(r)
print(arbol.obtenerHijoDerecho(arbol.obtenerHijoDerecho(r)))

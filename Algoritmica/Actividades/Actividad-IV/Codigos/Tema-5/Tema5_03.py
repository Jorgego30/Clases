# Tema5_03
import arbol


r = arbol.ArbolBinario('a')
arbol.insertarIzquierdo(r, 'd')
arbol.insertarIzquierdo(r, 'b')
arbol.insertarDerecho(arbol.obtenerHijoIzquierdo(r), 'e')
arbol.insertarDerecho(r, 'c')
arbol.insertarIzquierdo(arbol.obtenerHijoDerecho(r), 'f')

print(r)
l = arbol.obtenerHijoIzquierdo(r)
print("\nHijo izdo --> ", l)
print("\nRaiz --> ", arbol.obtenerValorRaiz(r))
l = arbol.obtenerHijoDerecho(r)
print("\nHijo dcho --> ", l)

from Class_Estructuras_lineales import Pila
from Class_Arboles import *
import operator  #versiones funcionales de muchos operadores utilizados comúnmente

def preorden(arbol):
    if arbol:
        print(arbol.obtenerValorRaiz())
        preorden(arbol.obtenerHijoIzquierdo())
        preorden(arbol.obtenerHijoDerecho())

def postorden(arbol):
    if arbol != None:
        postorden(arbol.obtenerHijoIzquierdo())
        postorden(arbol.obtenerHijoDerecho())
        print(arbol.obtenerValorRaiz())

def inorden(arbol):
    if arbol != None:
        inorden(arbol.obtenerHijoIzquierdo())
        print(arbol.obtenerValorRaiz())
        inorden(arbol.obtenerHijoDerecho())

def evalPostorden(arbol):
    operadores = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    res1 = None
    res2 = None
    if arbol:
        res1 = evalPostorden(arbol.obtenerHijoIzquierdo())
        res2 = evalPostorden(arbol.obtenerHijoDerecho())
    if res1 and res2:
        return operadores[arbol.obtenerValorRaiz()](res1,res2)
    else:
        return arbol.obtenerValorRaiz()

def imprimirExpresion(arbol):
    valorCadena = ""
    if arbol:
        # Si hay un hijo izquierdo, agrega paréntesis
        if arbol.obtenerHijoIzquierdo():
            valorCadena += "(" + imprimirExpresion(arbol.obtenerHijoIzquierdo())
        else:
            valorCadena += imprimirExpresion(arbol.obtenerHijoIzquierdo())

        # Agrega el valor de la raíz
        valorCadena += str(arbol.obtenerValorRaiz())

        # Si hay un hijo derecho, agrega paréntesis
        if arbol.obtenerHijoDerecho():
            valorCadena += imprimirExpresion(arbol.obtenerHijoDerecho()) + ")"
        else:
            valorCadena += imprimirExpresion(arbol.obtenerHijoDerecho())

    return valorCadena
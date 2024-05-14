"""Amplía la función construirArbolAnalisis para que pueda manejar expresiones matemáticas que no
tienen espacios entre cada carácter."""

from clase_2 import Pila
from Clase_1 import ArbolBinario

def normaliza(expr):#funcion que maneja expresiones sin espacios 3
    Nexpr = ""
    ant=""
    for c in expr:#concatenamos la expresion separando cada termino
        if c in "()*+/-":
            Nexpr = Nexpr+c+' '
            ant=' '
        elif c in "0123456789.,":
            if ant=="num":
                Nexpr=Nexpr.strip()

            Nexpr = Nexpr+c+' '
            ant="num"

    Nexpr=Nexpr.strip()
    return Nexpr


def construirArbolAnalisis(expresionAgrupada):#funcion que construye el arbol binario
    listaSimbolos = expresionAgrupada.split()#separamos la expresion
    print(listaSimbolos)
    pilaPadres = Pila()
    arbolExpresion = ArbolBinario('')
    pilaPadres.incluir(arbolExpresion)
    
    arbolActual = arbolExpresion
    for i in listaSimbolos:#creamos el arbol elemento a elemento
        if i == '(':
            arbolActual.insertarIzquierdo('')
            pilaPadres.incluir(arbolActual)
            arbolActual = arbolActual.obtenerHijoIzquierdo()
        elif i not in ['+', '-', '*', '/', ')']:
            arbolActual.asignarValorRaiz(float(i))
            padre = pilaPadres.extraer()
            arbolActual = padre
        elif i in ['+', '-', '*', '/']:
            arbolActual.asignarValorRaiz(i)
            arbolActual.insertarDerecho('')
            pilaPadres.incluir(arbolActual)
            arbolActual = arbolActual.obtenerHijoDerecho()
        elif i == ')':
            arbolActual = pilaPadres.extraer()
        else:
            raise ValueError
    return arbolExpresion

def preorden(arbol):#recorremos y mostramos el arbol
    if arbol:
        print(arbol.obtenerValorRaiz())
        preorden(arbol.obtenerHijoIzquierdo())
        preorden(arbol.obtenerHijoDerecho())


#llamamos a las funciones
miArbolAnalisis = construirArbolAnalisis (normaliza("((10+5.0 )*3.24)"))
preorden(miArbolAnalisis)
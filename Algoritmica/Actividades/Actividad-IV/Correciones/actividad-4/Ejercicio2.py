"""Modifica las funciones construirArbolAnalisis y evaluar para que puedan manejar las sentencias
booleanas (and, or, y not). Recuerda que “not” es un operador unario, por lo que esto complicará un poco
la realización del código."""

from clase_2 import Pila
from Clase_1 import ArbolBinario

def normaliza(expr):#funcion que maneja expresiones sin espacios
    Nexpr = ""
    ant=""
    for c in expr:#concatenamos la expresion separando cada termino
        if c in "()&|!":
            if ant == "letra":
                Nexpr = Nexpr + ' '
            Nexpr = Nexpr+c+' '
            ant=' '
        elif c.lower() in "abcdefghijklmnñopqrstuvwxyz":
            Nexpr=Nexpr+c
            ant = "letra"
    
    Nexpr = Nexpr.strip()
    return Nexpr


def construirArbolAnalisis(expresionAgrupada):#funcion que construye el arbol binario
    listaSimbolos = expresionAgrupada.split()#separamos la expresion
    print(listaSimbolos,"\n")
    pilaPadres = Pila()
    arbolExpresion = ArbolBinario('')
    pilaPadres.incluir(arbolExpresion)
    arbolActual = arbolExpresion
    for i in listaSimbolos:#creamos el arbol elemento a elemento
        if i == '(':
            arbolActual.insertarIzquierdo('')
            pilaPadres.incluir(arbolActual)
            arbolActual = arbolActual.obtenerHijoIzquierdo()
        elif i not in [')','&','|','!']:
            arbolActual.asignarValorRaiz((i))
            padre = pilaPadres.extraer()
            arbolActual = padre
        elif i in ['&','|']:
            arbolActual.asignarValorRaiz(i)
            arbolActual.insertarDerecho('')
            pilaPadres.incluir(arbolActual)
            arbolActual = arbolActual.obtenerHijoDerecho()
        elif i=='!':
            arbolActual.asignarValorRaiz(i)
            arbolActual.insertarIzquierdo('')
            pilaPadres.incluir(arbolActual)
            arbolActual = arbolActual.obtenerHijoIzquierdo()
        elif i == ')':
            arbolActual = pilaPadres.extraer()
        else:
            raise ValueError
    return arbolExpresion

def operator_and(izq,der):#Creamos una funcion que haga un and con los dos elementos que se le envian
    if izq=="True" and der=="True":
        return "True"
    else:
        return "False"
def operator_not(izq):#Creamos una funcion que haga devuelva el elemento contrario al recibido
    if izq=="True":
        return "False"
    else:
        return "True"
def operator_or(izq,der):#Creamos una funcion que haga un or con los dos elementos que se le envian
    if izq=="True" or der=="True":
        return "True"
    else:
        return "False"
  

def evaluar(arbolAnalisis):#funcion para operar los arboles 
    operadores = {'&':operator_and,'|':operator_or}#operadores binarios

    hijoIzquierdo = arbolAnalisis.obtenerHijoIzquierdo()#obtenemos el hijo izquierdo
        
    hijoDerecho = arbolAnalisis.obtenerHijoDerecho()#obtenemos el hijo derecho

    if hijoIzquierdo and hijoDerecho:
        fn = operadores[arbolAnalisis.obtenerValorRaiz()]
        return fn(evaluar(hijoIzquierdo),evaluar(hijoDerecho))#llamamos a las recuersiones y a las funciones para las operaciones binarias
    elif hijoIzquierdo:
        return operator_not(evaluar(hijoIzquierdo))        
    else:
        return arbolAnalisis.obtenerValorRaiz()#llamamos a la recuersion y a la funcion para la operacion unaria

def preorden(arbol):#recorremos y mostramos el arbol
    cadena = ''
    if arbol:
        cadena = arbol.obtenerValorRaiz()
        if arbol.obtenerHijoIzquierdo() != None:
            cadena = cadena + ' ' + preorden(arbol.obtenerHijoIzquierdo())
        if arbol.obtenerHijoDerecho() != None:
            cadena = cadena + ' ' + preorden(arbol.obtenerHijoDerecho())
    return cadena

miArbolAnalisis = construirArbolAnalisis (normaliza("((False & True) | !(False & True))"))#llamamos a las funciones pasandoles esta sentencia booleana
print("Resultado del arbol en preorden:", preorden(miArbolAnalisis))
print("\nEl resultado es:\n",evaluar(miArbolAnalisis))

miArbolAnalisis = construirArbolAnalisis (normaliza("((False & True) | !(True & False))"))#llamamos a las funciones pasandoles esta sentencia booleana
print("Resultado del arbol en preorden:", preorden(miArbolAnalisis))
print("\nEl resultado es:\n",evaluar(miArbolAnalisis))
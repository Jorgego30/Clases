'''Actividad 1:

Escribe una función recursiva para invertir una lista enlazada
'''

from Class_ListaEnlazada import *

# : 1 -> 2 -> 3 -> 4 -> 5
inicio = NodoListaEnlazada(1)
inicio.siguiente = NodoListaEnlazada(2)
inicio.siguiente.siguiente = NodoListaEnlazada(3)
inicio.siguiente.siguiente.siguiente = NodoListaEnlazada(4)
inicio.siguiente.siguiente.siguiente.siguiente = NodoListaEnlazada(5)

# Invertimos la lista enlazada
inicio = invertir_lista_enlazada(inicio)

# Imprimimos la lista invertida
while inicio:
    print(inicio.valor, end=",")
    inicio = inicio.siguiente

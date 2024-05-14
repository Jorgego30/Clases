#Modifica la función imprimirExpresion para que no incluya un par de paréntesis ‘extra’ alrededor de
#cada número.


""""
Está modificada la clase binaryTree.py

"""
from binaryTree import *

print("creamos el arbol con los operandos")
x = BinaryTree('*')
x.insertLeft('11')
x.insertRight('-')
r = x.getRightChild()
r.insertRight('13')
print("Imprimimos con el metodo imprimir expresion(modificada quitando los parentesis que sobran)")
printexp(x)
print()
#Implementa como un nuevo método de la clase, la concatenación de dos colas para
#constituir una nueva.

from class_ejercicio4 import *

cola1 = Cola()
cola2 = Cola()

cola1.encolar("A")
cola1.encolar("B")
cola1.encolar("C")
cola2.encolar("D")
cola2.encolar("E")

print("Cola 1:")
cola1.imprimir() # debería mostrar: A B C
print("Cola 2:")
cola2.imprimir() # debería mostrar: D E

cola1.concatenar(cola2)

print("Cola concatenada:")
cola1.imprimir() # debería mostrar: A B C D E

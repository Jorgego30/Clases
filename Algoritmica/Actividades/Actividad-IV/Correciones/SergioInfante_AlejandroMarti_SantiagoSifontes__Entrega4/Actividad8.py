'''
8. Utilizando la clase MonticuloBinario, implementa una nueva clase llamada ColaPrioridad. Esta nueva 
clase ColaPrioridad debe implementar el constructor, además de los métodos agregar y avanzar.
'''
from AlxColaPrioridad import ColaPrioridad
from AlxClass_Grafos import Vertice

# Los elementos entran como Tuplas en esta Cola de prioridad.
Listaelementos = [(i,Vertice(i)) for i in range(1,6)]

CP = ColaPrioridad()

for i in Listaelementos:
    CP.agregar(i)



print("Cola original: ", end='')
for i in range(1,CP.MB.tamanoActual+1):
    Var = CP.MB.listaMonticulo[i]
    print(f"({Var[0]}, {Var[1].id})", end='')

Avanzado = CP.avanzar()
print("\nAvanzamos el elemento minimo (Minheap): ", (Avanzado[0],Avanzado[1].id), end='')

print("\nCola restante: ", end='')
for i in range(1,CP.MB.tamanoActual+1):
    Var = CP.MB.listaMonticulo[i]
    print(f"({Var[0]}, {Var[1].id})", end='')
print("\nNota, es un arbol binario, por eso esta disposion y no 2345")
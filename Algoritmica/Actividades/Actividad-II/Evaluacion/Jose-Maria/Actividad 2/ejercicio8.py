#Implementar el TAD Colas de Prioridad, usando listas enlazadas ordenadas.

from class_actividad8 import *


cola = ColaPrioridad()

cola.insertar("Tarea 1", 3)
cola.insertar("Tarea 2", 2)
cola.insertar("Tarea 3", 1)

cola.imprimir() # debería mostrar: Tarea 3 con prioridad 1, Tarea 2 con prioridad 2, Tarea 1 con prioridad 3

cola.eliminar()

cola.imprimir() # debería mostrar: Tarea 2 con prioridad 2, Tarea 1 con prioridad 3
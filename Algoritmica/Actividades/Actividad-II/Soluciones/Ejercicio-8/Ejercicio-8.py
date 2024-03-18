from Class_Colas_prioridad import *

cola = ColaPrioridad()
cola.añade("Tarea 1", 3)
cola.añade("Tarea 2", 1)
cola.añade("Tarea 3",'a')

while not cola.esta_vacia():
    print(cola.extrae())
# Importamos la clase ColaPrioridad del código proporcionado
from Class_Monticulos import ColaPrioridad

# Creamos una instancia de ColaPrioridad
cola_prioridad = ColaPrioridad()

# Agregamos elementos a la cola con su respectiva prioridad
cola_prioridad.agregar("Tarea 1", 3)
cola_prioridad.agregar("Tarea 2", 1)
cola_prioridad.agregar("Tarea 3", 2)

# Avanzamos en la cola y obtenemos los elementos en orden de prioridad
print("Elementos en la cola de prioridad:")
print(cola_prioridad.avanzar())  # Avanza y devuelve "Tarea 2" (prioridad 1)
print(cola_prioridad.avanzar())  # Avanza y devuelve "Tarea 3" (prioridad 2)
print(cola_prioridad.avanzar())  # Avanza y devuelve "Tarea 1" (prioridad 3)

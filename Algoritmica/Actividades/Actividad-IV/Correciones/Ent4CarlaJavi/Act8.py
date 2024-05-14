"""8. Utilizando la clase MonticuloBinario, implementa una nueva clase llamada ColaPrioridad. Esta nueva
clase ColaPrioridad debe implementar el constructor, además de los métodos agregar y avanzar. """
from cola_prioridad import ColaPrioridad

# Crear una cola de prioridad y agregar elementos
cola = ColaPrioridad()
cola.agregar(30)
cola.agregar(50)
cola.agregar(10)

# Extraer elementos de la cola de prioridad y mostrarlos
print("Elemento con mayor prioridad extraído:", cola.avanzar())  # Salida esperada: 50
print("Elemento con mayor prioridad extraído:", cola.avanzar())  # Salida esperada: 30
print("Elemento con mayor prioridad extraído:", cola.avanzar())  # Salida esperada: 10

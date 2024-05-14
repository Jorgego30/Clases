from Clasesp5_2 import PriorityQueue

# Creamos una cola de prioridad
cola_prioridad = PriorityQueue()

# Agregamos algunas tuplas (clave, prioridad)
cola_prioridad.agregar('A', 10)
cola_prioridad.agregar('B', 5)
cola_prioridad.agregar('C', 15)
cola_prioridad.agregar('D', 3)

# Extraemos elementos y verificamos el orden
print("Extracción de elementos en orden de prioridad:")
while not cola_prioridad.esta_vacia():
    clave, prioridad = cola_prioridad.obtener_minimo()
    print(f"Clave: {clave}, Prioridad: {prioridad}")

# Agregamos más elementos
cola_prioridad.agregar('E', 20)
cola_prioridad.agregar('F', 7)

# Extraemos elementos nuevamente y verificamos el orden
print("\nExtracción de elementos después de agregar más elementos:")
while not cola_prioridad.esta_vacia():
    clave, prioridad = cola_prioridad.obtener_minimo()
    print(f"Clave: {clave}, Prioridad: {prioridad}")

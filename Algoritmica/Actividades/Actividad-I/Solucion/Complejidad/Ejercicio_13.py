import time
import random

def experimento_obtencion(diccionario, keys):
    inicio = time.time()
    for key in keys:
        value = diccionario[key]
    fin = time.time()
    tiempo_obtencion = fin - inicio
    print(f"Tiempo de obtención: {tiempo_obtencion:.10f} segundos")

def experimento_asignacion(diccionario, keys, values):
    inicio = time.time()
    for key, value in zip(keys, values):
        diccionario[key] = value
    fin = time.time()
    tiempo_asignacion = fin - inicio
    print(f"Tiempo de asignación: {tiempo_asignacion:.10f} segundos")

# Crear un diccionario grande para el experimento
tamanio_diccionario = 10000
diccionario = {i: random.randint(1, 100) for i in range(tamanio_diccionario)}

# Crear claves y valores para el experimento
claves = random.sample(range(tamanio_diccionario), 1000)
valores = random.sample(range(1000), 1000)

# Realizar experimento de obtención
experimento_obtencion(diccionario, claves)

# Realizar experimento de asignación
experimento_asignacion(diccionario, claves, valores)

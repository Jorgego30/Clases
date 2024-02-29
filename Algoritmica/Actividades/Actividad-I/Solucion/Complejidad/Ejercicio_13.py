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


tamanio_diccionario = 10000
diccionario = {i: random.randint(1, 100) for i in range(tamanio_diccionario)}

 
claves = random.sample(range(tamanio_diccionario), 1000)
valores = random.sample(range(1000), 1000)


experimento_obtencion(diccionario, claves)


experimento_asignacion(diccionario, claves, valores)

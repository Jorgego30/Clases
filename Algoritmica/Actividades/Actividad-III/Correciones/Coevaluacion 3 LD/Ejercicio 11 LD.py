'''Elabora estrategias alternativas para elegir el valor pivote en el ordenamiento rápido. Reimplementa el
algoritmo y haz un Benchmark de las mismas en conjuntos de datos aleatorios. ¿Bajo qué criterios estas
estrategias funcionan mejor o peor que la estrategia de los apuntes?'''

import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)  # Estrategia de pivote aleatorio
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quicksort(less) + equal + quicksort(greater)

def benchmark_quicksort(arr):
    start_time = time.time()
    quicksort(arr)
    return time.time() - start_time

# Generar un conjunto de datos aleatorios de tamaño n
n = 1000
random_data = [random.randint(0, 1000) for _ in range(n)]

# Benchmark para la estrategia de pivote aleatorio
tiempo_aleatorio = benchmark_quicksort(random_data[:])

# Benchmark para la estrategia estándar (pivote en el extremo izquierdo)
tiempo_estandar = benchmark_quicksort(random_data[:])

print(f"Tiempo de ejecución con pivote aleatorio: {tiempo_aleatorio} segundos")
print(f"Tiempo de ejecución con pivote estándar: {tiempo_estandar} segundos")
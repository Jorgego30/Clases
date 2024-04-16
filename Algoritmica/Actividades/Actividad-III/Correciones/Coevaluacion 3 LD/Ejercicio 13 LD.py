'''Diseña un experimento aleatorio (Benchmark ) para probar la diferencia entre una búsqueda secuencial y
una búsqueda binaria, en todas sus variantes, en una lista de 200 enteros.'''

import random
import time

# Generar una lista ordenada de 200 enteros
sorted_list = sorted(random.sample(range(1, 1000), 200))

# Búsqueda secuencial
def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Búsqueda binaria
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Benchmark para la búsqueda secuencial
def benchmark_sequential_search(arr, target):
    start_time = time.time()
    sequential_search(arr, target)
    return time.time() - start_time

# Benchmark para la búsqueda binaria
def benchmark_binary_search(arr, target):
    start_time = time.time()
    binary_search(arr, target)
    return time.time() - start_time

# Realizar el experimento varias veces
num_experiments = 10
target = random.choice(sorted_list)
sequential_times = []
binary_times = []

for _ in range(num_experiments):
    sequential_time = benchmark_sequential_search(sorted_list, target)
    binary_time = benchmark_binary_search(sorted_list, target)
    sequential_times.append(sequential_time)
    binary_times.append(binary_time)

# Calcular el tiempo promedio de cada búsqueda
avg_sequential_time = sum(sequential_times) / num_experiments
avg_binary_time = sum(binary_times) / num_experiments

print(f"Tiempo promedio de búsqueda secuencial: {avg_sequential_time} segundos")
print(f"Tiempo promedio de búsqueda binaria: {avg_binary_time} segundos")
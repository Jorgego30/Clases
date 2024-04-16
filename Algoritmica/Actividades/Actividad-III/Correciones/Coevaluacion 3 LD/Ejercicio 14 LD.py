'''Utiliza todas las funciones de búsqueda binaria (recursiva e iterativa). Genera una lista ordenada aleatoria de
números enteros y realiza una prueba de referencia (Benchmark) para cada función. ¿Cuáles son sus
resultados? ¿Puedes explicarlos?'''

import random
import time

# Generar una lista ordenada aleatoria de números enteros
sorted_list = sorted(random.sample(range(1, 1000), 200))
target = random.choice(sorted_list)

# Búsqueda binaria recursiva
def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

# Búsqueda binaria iterativa
def binary_search_iterative(arr, target):
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

# Benchmark para la búsqueda binaria recursiva
def benchmark_binary_search_recursive(arr, target):
    start_time = time.time()
    binary_search_recursive(arr, target, 0, len(arr) - 1)
    return time.time() - start_time

# Benchmark para la búsqueda binaria iterativa
def benchmark_binary_search_iterative(arr, target):
    start_time = time.time()
    binary_search_iterative(arr, target)
    return time.time() - start_time

# Realizar la prueba de referencia
recursive_time = benchmark_binary_search_recursive(sorted_list, target)
iterative_time = benchmark_binary_search_iterative(sorted_list, target)

print(f"Tiempo de búsqueda binaria recursiva: {recursive_time} segundos")
print(f"Tiempo de búsqueda binaria iterativa: {iterative_time} segundos")

'''Búsqueda Binaria Recursiva:

La búsqueda binaria recursiva es una técnica en la que se divide repetidamente la lista en dos mitades y se busca en la mitad donde se espera que se encuentre el elemento deseado.
La implementación recursiva implica la llamada a la misma función de búsqueda con subconjuntos más pequeños de la lista hasta encontrar el elemento deseado.
La desventaja de la recursión es que implica el uso de la pila de llamadas, lo que puede consumir más recursos y tiempo de ejecución en comparación con la implementación iterativa.
Búsqueda Binaria Iterativa:

La búsqueda binaria iterativa sigue un enfoque similar al de la recursiva, pero se realiza a través de un bucle while en lugar de llamadas recursivas.
Al no utilizar la pila de llamadas, la implementación iterativa tiende a ser más eficiente en términos de uso de recursos y tiempo de ejecución.
Por lo tanto, la búsqueda binaria iterativa suele ser más rápida y consume menos recursos en comparación con la búsqueda binaria recursiva.'''
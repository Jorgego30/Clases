import random
import time

def binary_search_recursive(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, high)
        else:
            return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return -1

def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def benchmark_search_functions(arr, target):
    start_time = time.time()
    result_recursive = binary_search_recursive(arr, target, 0, len(arr) - 1)
    end_time_recursive = time.time()
    result_iterative = binary_search_iterative(arr, target)
    end_time_iterative = time.time()

    print("Resultado búsqueda binaria recursiva:", result_recursive)
    print("Tiempo de ejecución búsqueda binaria recursiva:", end_time_recursive - start_time)

    print("Resultado búsqueda binaria iterativa:", result_iterative)
    print("Tiempo de ejecución búsqueda binaria iterativa:", end_time_iterative - end_time_recursive)

# Generar una lista ordenada aleatoria de números enteros
lista_ordenada = sorted(random.sample(range(1, 1000000), 100000))

# Realizar la prueba de referencia (Benchmark)
benchmark_search_functions(lista_ordenada, random.randint(1, 1000000))

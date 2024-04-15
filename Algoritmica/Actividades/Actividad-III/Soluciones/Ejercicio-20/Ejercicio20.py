import time
from random import randint

def crearVector(n):
    vector = []
    for i in range(n):
        vector.append(randint(1, 100))
    return vector

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubbleSortBidireccional(arr):
    n = len(arr)
    izquierda = 0
    derecha = n - 1
    while izquierda < derecha:
        for i in range(izquierda, derecha):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        derecha -= 1
        for i in range(derecha, izquierda, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        izquierda += 1
    return arr

# Benchmark para el algoritmo de ordenamiento burbuja tradicional
def benchmark_bubble_sort(arr):
    start_time = time.time()
    sorted_arr = bubbleSort(arr)
    end_time = time.time()
    return end_time - start_time

# Benchmark para el algoritmo de ordenamiento burbuja bidireccional
def benchmark_bidirectional_bubble_sort(arr):
    start_time = time.time()
    sorted_arr = bubbleSortBidireccional(arr)
    end_time = time.time()
    return end_time - start_time

# Realizar el benchmark para diferentes tamaños de lista
for n in [100, 1000, 10000]:
    arr = crearVector(n)
    time_bubble = benchmark_bubble_sort(arr)
    time_bidirectional = benchmark_bidirectional_bubble_sort(arr)
    print(f"Tamaño de la lista: {n}")
    print(f"Tiempo de ejecución de bubble sort: {time_bubble} segundos")
    print(f"Tiempo de ejecución de bubble sort bidireccional: {time_bidirectional} segundos")
    print()

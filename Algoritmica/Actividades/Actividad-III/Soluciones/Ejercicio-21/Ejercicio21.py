
import time

def shellSort(arr, increments):
    n = len(arr)
    for inc in increments:
        for i in range(inc, n):
            temp = arr[i]
            j = i
            while j >= inc and arr[j - inc] > temp:
                arr[j] = arr[j - inc]
                j -= inc
            arr[j] = temp
    return arr

def benchmarkShellSort(arr, increments):
    start_time = time.time()
    sorted_arr = shellSort(arr, increments)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time, sorted_arr

# Lista de números aleatorios
random_list = [21, 13, 5, 9, 17, 2, 20, 8, 24, 16]

# Conjuntos de incrementos a probar
increments_sets = [
    [5, 3, 1],   # Conjunto de incrementos original
    [9, 5, 3, 1],  # Nuevo conjunto de incrementos
    [7, 3, 1],   # Otro conjunto de incrementos
    # Agrega otros conjuntos de incrementos que desees probar
]

# Realizar el benchmark para cada conjunto de incrementos
for i, increments in enumerate(increments_sets):
    execution_time, sorted_arr = benchmarkShellSort(random_list.copy(), increments)
    print(f"Conjunto de incrementos {i + 1}:")
    print("Lista ordenada:", sorted_arr)
    print("Tiempo de ejecución:", execution_time, "segundos")
    print()

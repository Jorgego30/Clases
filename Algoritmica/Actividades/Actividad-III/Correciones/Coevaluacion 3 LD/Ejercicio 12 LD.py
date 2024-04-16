'''Genera una pequeña lista aleatoria de números enteros. Muestra paso a paso cómo es ordenada dicha lista
por los siguientes algoritmos:
ordenamiento burbuja, en todas sus variantes
ordenamiento por selección
ordenamiento por inserción
ordenamiento de Shell (con distintos valores de los incrementos)
ordenamiento por mezcla
ordenamiento rápido (decide sobre el valor pivote)'''

import random

# Generar una lista aleatoria de números enteros
random_list = [random.randint(1, 100) for _ in range(10)]
print("Lista original:")
print(random_list)

# Función para mostrar el estado de la lista en cada paso
def print_step(sort_func, sort_name):
    sorted_list = sort_func(random_list.copy())
    print(f"\n{sort_name}:")
    print(sorted_list)

# Algoritmo de ordenamiento burbuja (variante clásica)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print_step(bubble_sort, "Ordenamiento Burbuja (Clásico)")

# Algoritmo de ordenamiento por selección
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print_step(selection_sort, "Ordenamiento por Selección")

# Algoritmo de ordenamiento por inserción
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print_step(insertion_sort, "Ordenamiento por Inserción")

# Algoritmo de ordenamiento de Shell
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

print_step(shell_sort, "Ordenamiento de Shell")

# Algoritmo de ordenamiento por mezcla
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

print_step(merge_sort, "Ordenamiento por Mezcla")

# Algoritmo de ordenamiento rápido (con selección de pivote)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

print_step(quick_sort, "Ordenamiento Rápido")
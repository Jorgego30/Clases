'''Realiza una prueba de referencia (Benchmark) para un ordenamiento de Shell, utilizando diferentes
conjuntos de incrementos en la misma lista (los expresados en los apuntes y dos más…)'''

import time
import random

def shell_sort(lista, incrementos):
    n = len(lista)
    for h in incrementos:
        for i in range(h, n):
            temp = lista[i]
            j = i
            while j >= h and lista[j - h] > temp:
                lista[j] = lista[j - h]
                j -= h
            lista[j] = temp
    return lista

# Generar lista de números aleatorios
random.seed(42)
lista = [random.randint(1, 1000) for _ in range(1000)]

# Diferentes conjuntos de incrementos para Shell Sort
incrementos_set1 = [5, 3, 1]
incrementos_set2 = [8, 4, 2, 1]
incrementos_set3 = [10, 5, 1]

# Benchmark de Shell Sort con diferentes conjuntos de incrementos
start_time = time.time()
shell_sort(lista.copy(), incrementos_set1)
time_set1 = time.time() - start_time

start_time = time.time()
shell_sort(lista.copy(), incrementos_set2)
time_set2 = time.time() - start_time

start_time = time.time()
shell_sort(lista.copy(), incrementos_set3)
time_set3 = time.time() - start_time

print("Tiempo de ejecución con incrementos [5, 3, 1]:", time_set1)
print("Tiempo de ejecución con incrementos [8, 4, 2, 1]:", time_set2)
print("Tiempo de ejecución con incrementos [10, 5, 1]:", time_set3)
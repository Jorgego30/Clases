'''Utilizando un generador de números aleatorios, crea una lista de 500 enteros. Realiza una prueba de
referencia usando al menos 3 de los algoritmos de ordenamiento de los apuntes. ¿Cuál es la diferencia en la
velocidad de ejecución? ¿Cuáles son tus conclusiones?'''

import random
import time

# Generar una lista de 500 enteros aleatorios
lista = [random.randint(1, 1000) for _ in range(500)]

# Algoritmo de ordenamiento de selección
def seleccion_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Algoritmo de ordenamiento de burbuja
def burbuja_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Algoritmo de ordenamiento quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# Función para medir el tiempo de ejecución de un algoritmo de ordenamiento
def medir_tiempo(algoritmo, lista):
    inicio = time.time()
    resultado = algoritmo(lista)
    tiempo_ejecucion = time.time() - inicio
    return resultado, tiempo_ejecucion

# Realizar la prueba de referencia
algoritmos = [seleccion_sort, burbuja_sort, quicksort]
for algoritmo in algoritmos:
    lista_copia = lista.copy()
    resultado, tiempo = medir_tiempo(algoritmo, lista_copia)
    print(f"Algoritmo: {algoritmo.__name__}, Tiempo de ejecución: {tiempo} segundos")

'''Para sacar conclusiones, analiza los tiempos de ejecución impresos y observa cuál algoritmo 
es más eficiente para ordenar una lista de 500 enteros. Puedes repetir el experimento con 
diferentes tamaños de listas para obtener más información sobre el rendimiento de los 
algoritmos de ordenamiento.'''
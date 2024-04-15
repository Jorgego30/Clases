import random
import time

def ordenamiento_rapido(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menores = [x for x in arr[1:] if x <= pivote]
        mayores = [x for x in arr[1:] if x > pivote]
        return ordenamiento_rapido(menores) + [pivote] + ordenamiento_rapido(mayores)

def pivote_aleatorio(arr):
    indice_pivote = random.randint(0, len(arr) - 1)
    arr[0], arr[indice_pivote] = arr[indice_pivote], arr[0]
    return ordenamiento_rapido(arr)

def pivote_medio_de_tres(arr):
    primero = arr[0]
    medio = arr[len(arr)//2]
    ultimo = arr[-1]
    indice_pivote = 0
    if primero < medio < ultimo or ultimo < medio < primero:
        indice_pivote = len(arr)//2
    elif medio < primero < ultimo or ultimo < primero < medio:
        indice_pivote = 0
    arr[0], arr[indice_pivote] = arr[indice_pivote], arr[0]
    return ordenamiento_rapido(arr)

def generar_arreglo(tamano):
    return [random.randint(0, 1000000) for _ in range(tamano)]

def benchmark(estrategia, tamano_arreglo):
    arr = generar_arreglo(tamano_arreglo)
    inicio = time.time()
    estrategia(arr)
    fin = time.time()
    return fin - inicio

tamano_arreglos = [1000, 5000, 10000, 50000, 100000]
for tamano in tamano_arreglos:
    tiempo_aleatorio = benchmark(pivote_aleatorio, tamano)
    tiempo_medio_tres = benchmark(pivote_medio_de_tres, tamano)
    print(f"Tamaño del arreglo: {tamano}")
    print(f"Tiempo con pivote aleatorio: {tiempo_aleatorio:.6f} segundos")
    print(f"Tiempo con pivote medio de tres: {tiempo_medio_tres:.6f} segundos")
    print()


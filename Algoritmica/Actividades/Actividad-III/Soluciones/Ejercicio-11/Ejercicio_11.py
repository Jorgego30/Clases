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


"""
Las estrategias alternativas de selección de pivote pueden funcionar mejor o peor que la estrategia estándar dependiendo de varios factores:

Distribución de los datos: La estrategia estándar de selección de pivote toma el primer elemento como pivote. Funciona bien cuando los datos están uniformemente distribuidos. Sin embargo, si los datos están ordenados o casi ordenados, esta estrategia puede llevar a un rendimiento deficiente. Las estrategias alternativas, como elegir un pivote aleatorio o el pivote medio de tres, pueden ayudar a mitigar este problema.

Eficiencia en el peor de los casos: La estrategia del pivote medio de tres es especialmente útil para mejorar el rendimiento en el peor de los casos del algoritmo de ordenamiento rápido. Al seleccionar un pivote que esté más cerca del valor medio del conjunto de datos, se reduce la probabilidad de que el algoritmo tenga un rendimiento deficiente en conjuntos de datos específicos.

Complejidad de implementación: Algunas estrategias pueden ser más simples de implementar que otras. La estrategia estándar de selección de pivote es simple y directa, ya que simplemente selecciona el primer elemento como pivote. En contraste, el pivote medio de tres requiere una comparación adicional para seleccionar el pivote medio. La complejidad de implementación puede ser un factor importante dependiendo del contexto.

Costo de cálculo del pivote: La selección de un pivote aleatorio puede ser más costosa computacionalmente que simplemente seleccionar el primer elemento como pivote. Sin embargo, en conjuntos de datos grandes, el beneficio de una distribución más uniforme de los pivotes puede superar el costo adicional de calcular un pivote aleatorio.

En resumen, las estrategias alternativas pueden ser preferibles a la estrategia estándar en casos donde los datos no están uniformemente distribuidos, se desea mejorar el rendimiento en el peor de los casos o se necesita una implementación más robusta. Sin embargo, es importante evaluar el rendimiento de cada estrategia en el contexto específico de la aplicación y los datos que se están ordenando.

"""
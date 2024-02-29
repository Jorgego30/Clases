import random,numpy as np,time

def contar(vector):
    vistos = []
    repes = []
    contador = 0
    inicio = time.time()
    for value in vector:
        if value in vistos:
            if value not in repes:
                contador += 1
            repes.append(value)
        else:
            vistos.append(value)
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    return contador, tiempo_ejecucion

vector = np.array([random.randint(0, 100000) for _ in range(10000)])

contador,tiempo = contar(vector)

print(f"El numero de elementos del vector aleatorio que se repiten dos o mas veces es: {contador}\nEsto se hace en {tiempo}, lo que nos deja con una complejidad de O(n²)")
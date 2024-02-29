import random,numpy as np,time


def suma_vector(vector):
    inicio = time.time()
    suma = 0
    for elemento in vector:
        suma += elemento
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    return suma, tiempo_ejecucion

mi_vector = np.array([random.randint(0, 100000) for _ in range(10000)])

resultado, tiempo = suma_vector(mi_vector)

print(f"La suma de los elementos del vector es: {resultado}")
print(f"Tiempo de ejecución: {tiempo:.10f} segundos")

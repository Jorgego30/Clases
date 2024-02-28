import time

def suma_vector(vector):
    inicio = time.time()
    suma = 0
    for elemento in vector:
        suma += elemento
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    return suma, tiempo_ejecucion

# Ejemplo de uso
mi_vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado, tiempo = suma_vector(mi_vector)

print(f"La suma de los elementos del vector es: {resultado}")
print(f"Tiempo de ejecución: {tiempo:.10f} segundos")

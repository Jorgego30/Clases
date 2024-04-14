from random import randint

def crearVector(n):
    vector = []
    for i in range(n):
        vector.append(randint(1, 100))
    return vector

def bubbleSortBidireccional(arr):
    n = len(arr)
    izquierda = 0
    derecha = n - 1
    while izquierda < derecha:
        # Pasada hacia adelante
        for i in range(izquierda, derecha):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        derecha -= 1

        # Pasada hacia atrás
        for i in range(derecha, izquierda, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        izquierda += 1

    return arr

# Ejemplo de uso
longitud = int(input("Introduzca la longitud del vector: "))
vector = crearVector(longitud)
print("Lista original:", vector)
print("Lista ordenada:", bubbleSortBidireccional(vector))

"""
Pros:

Puede ser más eficiente que el bubble sort tradicional en ciertos casos, ya que puede mover los elementos más grandes o más pequeños hacia sus posiciones correctas más rápidamente.
Funciona bien con listas que tienen elementos desordenados tanto al principio como al final.
Contras:

Aunque puede ser más eficiente en ciertas situaciones, el bubble sort bidireccional sigue siendo un algoritmo de complejidad temporal cuadrática y puede ser lento en listas grandes o cuando la lista está completamente desordenada.
La implementación es más compleja que el bubble sort tradicional, lo que puede dificultar su comprensión y mantenimiento.
"""

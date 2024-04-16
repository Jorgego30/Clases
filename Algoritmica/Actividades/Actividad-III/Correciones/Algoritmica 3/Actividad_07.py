'''Actividad 7:

Dado un vector V de longitud n, aplicando el esquema de diseño Divide y vencerás y sin modificar V,
escribir una función que devuelva el valor que ocuparía la posición k (p.e. posición de la mediana) si el
vector V estuviera ordenado. Calcular su complejidad temporal en función de n y expresarla en notación
asintótica
'''


import random

def seleccion_rapida(V, izq, der, k):
    # Caso base: Si solo hay un elemento en el subvector, se devuelve ese elemento
    if izq == der:
        return V[izq]

    # Se elige un pivote aleatorio y se particiona el subvector en dos partes
    pivote = particion(V, izq, der)

    # Si el índice del pivote es igual al índice buscado, se devuelve el valor del pivote
    if k == pivote:
        return V[k]
    # Si el índice buscado es menor que el índice del pivote, se busca en el subvector izquierdo
    elif k < pivote:
        return seleccion_rapida(V, izq, pivote - 1, k)
    # Si el índice buscado es mayor que el índice del pivote, se busca en el subvector derecho
    else:
        return seleccion_rapida(V, pivote + 1, der, k)

def particion(V, izq, der):
    # Se elige un pivote aleatorio y se intercambia con el último elemento del subvector
    pivote = random.randint(izq, der)
    V[pivote], V[der] = V[der], V[pivote]
    i = izq - 1

    # Se recorre el subvector desde izq hasta der - 1
    for j in range(izq, der):
        # Si el elemento actual es menor o igual que el pivote, se intercambia con el siguiente elemento después del último encontrado menor que el pivote
        if V[j] <= V[der]:
            i += 1
            V[i], V[j] = V[j], V[i]

    # Se coloca el pivote en su posición final, después de todos los elementos menores que él
    V[i + 1], V[der] = V[der], V[i + 1]
    return i + 1

# Función para encontrar la mediana de un vector V
def mediana(V):
    n = len(V)
    # Si la longitud del vector es impar, se busca el elemento central
    if n % 2 == 1:
        return seleccion_rapida(V, 0, n - 1, n // 2)
    # Si la longitud del vector es par, se promedian los dos elementos centrales
    else:
        return (seleccion_rapida(V, 0, n - 1, n // 2 - 1) + seleccion_rapida(V, 0, n - 1, n // 2)) / 2


vector = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] #Modificar para ver el funcionamiento
print("El valor de la mediana es:", mediana(vector))

